# PytonFace
Project on Face Recognition

# this is to install new package/module using pip and using that package/module#

## Configuration before any pipx ##
mkdir -p $HOME/.venvs; python3 -m venv $HOME/.venvs/MyEnv 
##

## installing using PIPX ##
vi /usr/bin/pipy
##

#--insert--#

" #!/bin/bash

$HOME/.venvs/MyEnv/bin/python -m pip install $1
"
## Install using pipy
pipy [packge_name]
##

## Make Alias ##
#This is going to be on $HOME/.bashrc#

alias torchvm="source$HOME/.venvs/MyEnv/bin/activate"
##

## Deactivate ##
deactivate
##
