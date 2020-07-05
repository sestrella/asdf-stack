list_tags() {
  local cmd="curl -s"
  if [ -n "$GITHUB_API_TOKEN" ]; then
    cmd="$cmd -H 'Authorization: token $GITHUB_API_TOKEN'"
  fi
  $cmd https://api.github.com/repos/commercialhaskell/stack/tags
}

select_versions() {
  jq -r .[].name | sed s/^v//
}

main() {
  echo $(list_tags | select_versions)
}
