load 'test_helper'
load '../lib/list-all'

@test "main - prints all stack versions available" {
  run main
  assert_success
  assert_output --partial '2.3.1'
  assert_output --partial '1.1.2'
}
