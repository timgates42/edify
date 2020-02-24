#!/bin/bash

export GHR=ssh://git@github.com
export GH=ssh://git@github.com/oneiress
export GHTG=ssh://git@github.com/timgates42
export EDITOR=vim
export BROWSER=links
export GIT_EDITOR=vim
export GPG_TTY=$(tty)

if [[ -n "$PS1" ]] && [[ -z "$TMUX" ]] && [[ -n "$SSH_CONNECTION" ]]; then
  tmux attach-session -t ssh_tmux || tmux new-session -s ssh_tmux
fi
