from lib.github_client import GithubClient

def list_all(client, printer=print):
  tags = list_tags(client)
  printer(tags_to_versions(tags))

def list_tags(client):
  return client.list_repo_tags('commercialhaskell', 'stack')

def tags_to_versions(tags):
  names = list(map(lambda tag: tag['name'][1:], tags))
  return ' '.join(names[::-1])

if __name__ == '__main__':
  client = GithubClient('token')
  list_all(client)
