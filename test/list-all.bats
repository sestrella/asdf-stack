load 'test-helper'
load '../lib/list-all'

@test 'prints all stack versions available' {
  run main
  assert_success
  assert_output --partial '2.3.1'
  assert_output --partial '1.1.2'
}
