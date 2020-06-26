# asdf-stack

![build](https://github.com/sestrella/asdf-stack/workflows/.github/workflows/build.yml/badge.svg?branch=master)

[Stack][stack] plugin for [asdf][asdf] version manager.

## Requirements

- curl
- jq
- tar

## Install

Run the following command:

```
asdf plugin-add stack https://github.com/sestrella/asdf-stack.git
```

# Test

Install Node.js via asdf:

```
asdf install
```

Install dependencies:

```
npm install
```

Run tests:

```
npm test
```

[asdf]: https://github.com/asdf-vm/asdf
[stack]: https://docs.haskellstack.org/en/stable/README
