from lib.github_client import GithubClient

import os

def list_all(client, printer=print):
  tags = __list_tags(client)
  printer(__tags_to_versions(tags))

def __list_tags(client):
  return client.list_repo_tags('commercialhaskell', 'stack')

def __tags_to_versions(tags):
  names = list(map(lambda tag: tag['name'][1:], tags))
  return ' '.join(names[::-1])

if __name__ == '__main__':
  token = os.getenv('GITHUB_API_TOKEN')
  client = GithubClient(token)
  list_all(client)
