import json
import urllib.request

def list_all():
    tags = list_tags()
    print(tags_to_versions(tags))

def list_tags():
    url = 'https://api.github.com/repos/commercialhaskell/stack/tags'
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

def tags_to_versions(tags):
    names = map(lambda tag: tag['name'][1:], tags)
    return ' '.join(names)

if __name__ == '__main__':
    list_all()
