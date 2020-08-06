import logging
import os
import platform
import shutil
import sys
import tarfile
import tempfile
import urllib.request

logger = logging.getLogger('install')

def install(client, install_dir, version):
  urls = list(__compatible_urls(__downloadable_urls(client, version)))
  logger.info(f'Available sources {urls}')
  return __install_static(install_dir, urls) or __install_dynamic(install_dir, urls)

def __downloadable_urls(client, version):
  assets = client.get_release_by_name('commercialhaskell', 'stack', f'v{version}')['assets']
  return map(lambda asset: asset['browser_download_url'], assets)

def __compatible_urls(urls):
  os = sys.platform
  arch = platform.machine()
  return filter(lambda url: f'{os}-{arch}' in url and url.endswith('tar.gz'), urls)

def __install_static(install_dir, urls):
  logger.info('Installing static binary')
  url = next((url for url in urls if 'static' in url), None)
  return __install_from_url(install_dir, url)

def __install_dynamic(install_dir, urls):
  logger.info('Installing dynamic binary')
  url = next((url for url in urls if not 'gmp4' in url), None)
  return __install_from_url(install_dir, url)

def __install_from_url(install_dir, url):
  if not url:
    logger.info('No source available')
    return False

  with tempfile.TemporaryDirectory() as download_dir:
    logger.info(f'Downloading {url} to {download_dir}')
    path, _ = urllib.request.urlretrieve(url, f"{download_dir}/stack.tar.gz")
    with tarfile.open(path) as tar:
      tar.extractall(download_dir)
      dirname = url.rsplit('/', 1)[1].rstrip('tar.gz')
      os.mkdir(f"{install_dir}/bin")
      __copy_file(f'{download_dir}/{dirname}/stack', f'{install_dir}/bin/stack')
      return True

def __copy_file(src, dest):
  logger.info(f'Copying {src} to {dest}')
  shutil.copy(src, dest)
