import glob;
import json;
import os;
import platform;
import shutil;
import tarfile;
import urllib.request;

version = os.environ['ASDF_INSTALL_VERSION'];
url = f"https://api.github.com/repos/commercialhaskell/stack/releases/tags/v{version}";

system = platform.system().lower();
machine = platform.machine();

path = os.environ['ASDF_INSTALL_PATH'];

with urllib.request.urlopen(url) as response:
    release = json.loads(response.read());
    asset_urls = map(lambda asset: asset['browser_download_url'], filter(lambda asset: asset['content_type'] == 'application/x-tgz', release['assets']));

    filtered_urls = filter(lambda url: f"{system}-{machine}" in url, asset_urls);
    url = next(filter(lambda url: 'static' in url, filtered_urls));

    tar_path, _ = urllib.request.urlretrieve(url, f"{path}/stack.tar.gz");
    with tarfile.open(tar_path) as tar:
        tar.extractall(path);

    os.remove(tar_path); 
    os.mkdir(f"{path}/bin");

    stack_bin = next(iter(glob.glob(f"{path}/stack-{version}-*/stack")));
    shutil.copy(stack_bin, f"{path}/bin/stack");
