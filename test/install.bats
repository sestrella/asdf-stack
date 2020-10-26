load "${BATS_TEST_DIRNAME}/../bin/install"
load "helper"

setup() {
  ASDF_INSTALL_PATH=$(mktemp -dt asdf-XXXX)
}

teardown() {
  rm -rf "$ASDF_INSTALL_PATH"
}

@test "downloads and install version 2.5.1" {
  ASDF_INSTALL_VERSION="2.5.1"
  main
  run "${ASDF_INSTALL_PATH}/bin/stack" --version
  assert_success
  assert_output --partial "2.5.1"
}

@test "downloads and install version 2.3.3" {
  ASDF_INSTALL_VERSION="2.3.3"
  main
  run "${ASDF_INSTALL_PATH}/bin/stack" --version
  assert_success
  assert_output --partial "2.3.3"
}
