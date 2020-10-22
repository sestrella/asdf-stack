import json
import os
import urllib.request

def list_all(printer = print):
  token = os.getenv('GITHUB_API_TOKEN')
  tags = get_tags('https://api.github.com/repos/commercialhaskell/stack/tags', token)
  printer(' '.join(tags[::-1]))
  return tags

def get_tags(url, token):
  request = urllib.request.Request(url)
  if token:
    request.headers = { 'Authorization': f'token {token}' }

  with urllib.request.urlopen(request) as response:
    next_link = parse_links(response.headers['link']).get('next')
    if next_link:
      return parse_tags(response) + get_tags(next_link, token)

    return parse_tags(response)

def parse_links(links):
  def parse_link(link):
    return (link[1][6:-1], link[0][1:-1])

  return dict(map(
    lambda link: parse_link(link.split(';')),
    links.split(',')
  ))

def parse_tags(response):
  tags = json.loads(response.read())
  return list(map(lambda tag: tag['name'][1:], tags))

if __name__ == '__main__':
  list_all()
