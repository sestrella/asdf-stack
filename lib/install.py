from urllib.error import HTTPError

import os
import platform
import shutil
import sys
import tarfile
import tempfile
import urllib.request

def install(install_dir, version):
  with tempfile.TemporaryDirectory() as download_dir:
    filename = f'stack-{version}-{sys.platform}-{platform.machine()}'
    try:
      return get_stack(install_dir, version, download_dir, f'{filename}-static')

    except HTTPError as e:
      if e.code == 404:
        return get_stack(install_dir, version, download_dir, filename)

      raise e

def get_stack(install_dir, version, download_dir, filename):
  url = f'https://github.com/commercialhaskell/stack/releases/download/v{version}/{filename}.tar.gz'
  path, _ = urllib.request.urlretrieve(url, f'{download_dir}/stack.tar.gz')
  with tarfile.open(path) as tar:
    tar.extractall(download_dir)
    install_bin_dir = f'{install_dir}/bin'
    stack_bin = f'{install_bin_dir}/stack'
    os.mkdir(install_bin_dir)
    shutil.copy(f'{download_dir}/{filename}/stack', stack_bin)
    return stack_bin

if __name__ == '__main__':
  install_dir = os.environ['ASDF_INSTALL_PATH']
  version = os.environ['ASDF_INSTALL_VERSION']
  install(install_dir, version)
