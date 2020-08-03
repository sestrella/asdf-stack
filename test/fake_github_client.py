import json

class FakeGithubClient:
  def list_repo_tags(self, owner, repo):
      return self.__read_fixture('tags.json')

  def get_release_by_name(self, owner, repo, tag):
      return self.__read_fixture(f'{tag}.json')

  def __read_fixture(self, fixture):
    with open(f'test/fixtures/{fixture}', 'r') as file:
      return json.loads(file.read())
