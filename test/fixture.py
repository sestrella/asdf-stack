import json

def read_fixture(fixture):
  with open(f'test/fixtures/{fixture}', 'r') as file:
    return json.loads(file.read())
