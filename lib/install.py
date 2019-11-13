from functools import reduce

import glob
import json
import os
import platform
import re
import shutil
import sys
import tarfile
import urllib.request

def release_by_tag(owner, repo, tag):
  url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"
  with urllib.request.urlopen(url) as f:
    return json.loads(f.read())

def assets_by_content_type(assets, content_type='application/x-tgz'):
  return map(
    lambda asset: asset['browser_download_url'],
    filter(
      lambda asset: asset['content_type'] == content_type,
      assets
    )
  )

def urls_by_type(urls, system = platform.system(), machine = platform.machine()):
    def boom(result, url):
        key = re.search('\-(\w+)\.tar\.gz$', url)[1]
        result['default' if key == machine else key] = url
        return result

    filtered_urls = filter(lambda url: f"{system}-{machine}".lower() in url, urls)
    return reduce(boom, filtered_urls, {})

# TODO: Rename this function
def foo(urls):
    return urls.get('static', urls['default'])

def download_and_extract(url, path):
    tar_path, _ = urllib.request.urlretrieve(url, f"{path}/stack.tar.gz")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path)

    os.remove(tar_path) 
    return next(iter(glob.glob(f"{path}/stack-*")))

def main():
    path = os.environ['ASDF_INSTALL_PATH']
    version = os.environ['ASDF_INSTALL_VERSION']

    release = release_by_tag('commercialhaskell', 'stack', f"v{version}")
    urls = urls_by_type(asset_by_content_type(release['assets']))
    url = foo(urls_by_type(urls))
    stack_dir = download_and_extract(url, path)
    shutil.copy(stack_bin, f"{stack_dir}/bin/stack")
