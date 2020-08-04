source "${BASH_SOURCE%/*}/helper.bash"

main() {
  local assets=$(available_assets | download_urls | compatible_urls)
  install "$assets"
}

available_assets() {
  github_api "repos/commercialhaskell/stack/releases/tags/v$ASDF_INSTALL_VERSION"
}

download_urls() {
  jq -r .assets[].browser_download_url
}

compatible_urls() {
  local os=$(get_os)
  local arch=$(uname -m)
  grep "$os" | grep "$arch" | grep 'tar\.gz$'
}

get_os() {
  local os=$(uname)
  case "$os" in
    "Darwin")
      echo "osx"
      ;;
    "Linux")
      echo "linux"
      ;;
    *)
      echo "Unsupported OS $os"
      exit 1
  esac
}

install() {
  install_static "$1" || install_dynamic "$1"
}

install_static() {
  local assets=$(echo "$1" | grep static)

  if [ -z "$assets" ]; then
    echo "No static binary found"
    return 1
  fi

  download_and_copy "${assets[0]}"
}

install_dynamic() {
  local assets=$(echo "$1" | grep -v gmp)

  if [ -z "$assets" ]; then
    echo "No dynamic binary found"
    return 1
  fi

  download_and_copy "${assets[0]}"
}

download_and_copy() {
  local download_url=$1
  local download_path=$(mktemp -dt asdf-stack.XXXX)

  echo "Downloading $download_url to $download_path"
  trap "rm -rf $download_path" EXIT
  curl -sL $download_url | tar -xz -C $download_path --strip-components 1
  echo $download_path

  echo "Copying binary from $download_path to $ASDF_INSTALL_PATH"
  mkdir "$ASDF_INSTALL_PATH/bin"
  cp "$download_path/stack" "$ASDF_INSTALL_PATH/bin"
}
