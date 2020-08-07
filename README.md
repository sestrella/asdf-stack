# asdf-stack

![build](https://github.com/sestrella/asdf-stack/workflows/build/badge.svg?branch=master)

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

Run tests:

```
python -m unittest
```

[asdf]: https://github.com/asdf-vm/asdf
[stack]: https://docs.haskellstack.org/en/stable/README
