source "$BATS_TEST_DIRNAME/../lib/list-all.bash"

print_versions() {
  cat "$BATS_TEST_DIRNAME/tags.json" | select_versions
}

@test "list_tags" {
  run list_tags
  [ "$status" -eq 0 ]
}

@test "select_versions" {
  run print_versions
  [ "$status" -eq 0 ]
  [ "${lines[0]}" = "2.3.1" ]
  [ "${lines[29]}" = "1.1.2" ]
}
