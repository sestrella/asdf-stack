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

def install(path, version):
    release = release_by_tag(f"v{version}")
    url = url_by_type(tarball_assets(release['assets']))
    stack_dir = download_and_extract(url, path)
    os.mkdir(f"{path}/bin")
    shutil.copy(f"{stack_dir}/stack", f"{path}/bin/stack")
    return f"{path}/bin/stack"

def release_by_tag(tag):
  url = f"https://api.github.com/repos/commercialhaskell/stack/releases/tags/{tag}"
  with urllib.request.urlopen(url) as f:
    return json.loads(f.read())

def tarball_assets(assets):
  return map(
    lambda asset: asset['browser_download_url'],
    filter(
      lambda asset: asset['content_type'] == 'application/x-tgz',
      assets
    )
  )

def url_by_type(urls, system = platform.system(), machine = platform.machine()):
    def by_type(result, url):
        key = re.search('\-(\w+)\.tar\.gz$', url)[1]
        result['dynamic' if key == machine else key] = url
        return result

    filtered_urls = filter(lambda url: f"{system}-{machine}".lower() in url, urls)
    urls_by_type = reduce(by_type, filtered_urls, {})
    return urls_by_type.get('static', urls_by_type['dynamic'])

def download_and_extract(url, path):
    tar_path, _ = urllib.request.urlretrieve(url, f"{path}/stack.tar.gz")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path)

    os.remove(tar_path) 
    return next(iter(glob.glob(f"{path}/stack-*")))

if __name__ == '__main__':
    path = os.environ['ASDF_INSTALL_PATH']
    version = os.environ['ASDF_INSTALL_VERSION']
    install(path, version)
