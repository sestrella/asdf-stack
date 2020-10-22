# asdf-stack

![CI](https://github.com/sestrella/asdf-stack/workflows/CI/badge.svg?branch=master)

[Stack][stack] plugin for [asdf][asdf] version manager.

## Requirements

- Python 3

## Install

Run the following command:

```
asdf plugin-add stack https://github.com/sestrella/asdf-stack.git
```

## Test

Install Python:

```
asdf plugin-add python
asdf install
```

Create a virtual environment:

```
python -m venv .venv
```

Active the virtual environment:

```
source .venv/bin/activate (bash or zsh)
# or
source .venv/bin/activate.fish (fish)
```

Install dependencies:

```
pip install -r requirements.txt
```

Run lint:

```
python -m flake8 lib/ test/
```

Run tests:

```
python -m unittest
```

[asdf]: https://github.com/asdf-vm/asdf
[stack]: https://docs.haskellstack.org/en/stable/README
