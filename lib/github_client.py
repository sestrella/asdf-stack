class GithubClient:
  URL = 'https://api.github.com'

  def __init__(self, api_token):
    self.api_token = api_token

  def list_repo_tags(self, owner, repo):
    with urllib.request.urlopen(f'{URL}/repos/{owner}/{repo}/tags') as response:
      return json.loads(response.read())
