load 'test_helper'

source "$BATS_TEST_DIRNAME/../lib/list-all.bash"

print_versions() {
  cat "$BATS_TEST_DIRNAME/tags.json" | select_versions
}

@test "list_tags" {
  run list_tags
  assert_success
}

@test "select_versions" {
  run print_versions
  assert_success
  assert_output --partial '2.3.1'
  assert_output --partial '1.1.2'
}
