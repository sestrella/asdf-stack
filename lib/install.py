from lib.github_client import GithubClient

import platform
import sys

def install(client, install_dir, version):
  urls = __compatible_assets(assets_by_version(client, version))
  print(list(urls))
  return None

def assets_by_version(client, version):
  assets = client.get_release_by_name('commercialhaskell', 'stack', f'v{version}')['assets']
  return map(lambda asset: asset['browser_download_url'], assets)

def __compatible_assets(urls):
  os = sys.platform
  arch = platform.machine()
  return filter(lambda url: f'{os}-{arch}' in url, urls)
