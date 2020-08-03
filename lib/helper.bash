github_api() {
  local cmd="curl -s"
  if [ -n "$GITHUB_API_TOKEN" ]; then
    cmd="$cmd -H 'Authorization: token $GITHUB_API_TOKEN'"
  fi
  $cmd "https://api.github.com/$1"
}
