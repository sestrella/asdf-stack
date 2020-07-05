load 'test-helper'
load '../lib/install'

setup() {
  ASDF_DIR=$(mktemp -dt asdf.XXXX)
}

teardown() {
  rm -rf "$ASDF_DIR"
}

@test 'installs stack version 2.3.1' {
  ASDF_INSTALL_PATH="$ASDF_DIR/installs/stack/2.3.1"
  mkdir -p "$ASDF_INSTALL_PATH"
  ASDF_INSTALL_VERSION="2.3.1"
  run main
  assert_success
  assert [ -x "$ASDF_INSTALL_PATH/bin/stack" ]
}

@test 'installs stack version 1.3.2' {
  ASDF_INSTALL_PATH="$ASDF_DIR/installs/stack/1.3.2"
  mkdir -p "$ASDF_INSTALL_PATH"
  ASDF_INSTALL_VERSION="1.3.2"
  run main
  assert_success
  assert [ -x "$ASDF_INSTALL_PATH/bin/stack" ]
}
