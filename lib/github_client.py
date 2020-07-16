class GithubClient:
  BASE_URL = 'https://api.github.com'

  def __init__(self, token = None):
    self.token = token

  def list_repo_tags(self, owner, repo):
    url = f'{BASE_URL}/repos/{owner}/{repo}/tags'
    return __get_request(url)

  def get_release_by_name(self, owner, repo, tag):
    url = f'{BASE_URL}/repos/{owner}/{repo}/releases/tags/{tag}'
    return __get_request(url)

  def __get_request(url):
    request = urllib.request.Request(url)
    if not self.token:
      request.headers = { 'Authorization': f'token {self.token}' }
    with urllib.request.urlopen(request) as response:
      return json.loads(response.read())
