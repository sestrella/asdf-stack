source "${BASH_SOURCE%/*}/helper.bash"

main() {
  echo $(list_tags | select_versions)
}

list_tags() {
  github_api "repos/commercialhaskell/stack/tags"
}

select_versions() {
  jq -r .[].name | sed s/^v//
}
