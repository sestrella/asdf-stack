load "${BATS_TEST_DIRNAME}/../bin/list-all"
load "helper"

@test "print available versions" {
  run main
  assert_success
  assert_output --partial "1.7.1"
  assert_output --partial "1.9.3"
  assert_output --partial "2.1.3"
  assert_output --partial "2.3.3"
  assert_output --partial "2.5.1"
}
