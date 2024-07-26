# d4k-womad-arcade
Devoxx4Kids Arcade Workshop for WOMAD 2024

You can find the [presentation slides use here](https://docs.google.com/presentation/d/1EHGkN8ul7OWdhdEO8XYA_rpwDMqGccS7/edit#slide=id.p1).

**If you would like help, please open up a GitHub Issue, or email uk@devoxx4kids.org and we'll try to point you in the right direction.**

1. Install `Python 3.8` (not the latest)
  * See `Installing Python` below
2. Install `Pygame Zero`
  * `pip install pgzero`

Slides are here: https://docs.google.com/presentation/d/1EHGkN8ul7OWdhdEO8XYA_rpwDMqGccS7/edit?usp=sharing&ouid=113316425877426317108&rtpof=true&sd=true

### Installing Python

There are many ways to install Python 3.8.
You can check which version of Python you have with `python --version`.

#### Mac using Homebrew

```zsh
brew update
brew install pyenv
# Follow: https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv
pyenv install --list # check pyenv is working
pyenv install -v 3.8 # install the latest 3.8 version (3.8.19 at the time of writing)
pyenv local 3.8 # use this version whenever in this directory tree
```
