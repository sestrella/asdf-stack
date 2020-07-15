import json
import urllib.request

URL = 'https://api.github.com/repos/commercialhaskell/stack/tags'

def list_all(printer=print):
  tags = list_tags()
  printer(tags_to_versions(tags))

def list_tags():
  with urllib.request.urlopen(URL) as response:
    return json.loads(response.read())

def tags_to_versions(tags):
  names = list(map(lambda tag: tag['name'][1:], tags))
  return ' '.join(names[::-1])

if __name__ == '__main__':
  list_all()
