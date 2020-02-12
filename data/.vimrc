set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'psf/black'
Plugin 'fisadev/vim-isort'
Plugin 'vim-syntastic/syntastic'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-dispatch'
Plugin 'hashivim/vim-terraform'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" Put your non-Plugin stuff after this line

execute pathogen#infect()

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 1

let g:black_fast=1

set nocompatible

set backspace=indent,eol,start

set autoindent

set history=50
set ruler
set showcmd
set incsearch
syntax on
set hlsearch
" : filetype plugin indent off

" trial no => set hidden

set ic
set textwidth=80
set nowrap
set tabstop=8
set foldmethod=marker

set shiftwidth=4
set softtabstop=4
set expandtab

set background=dark

" Make p in Visual mode replace the selected text with the "" register.
vnoremap p <Esc>:let current_reg = @"<CR>gv"zdi<C-R>=current_reg<CR><Esc>

if &term == "rxvt-cygwin-native"
    map <Esc>[7~ 0
    imap <Esc>[7~ <C-o>0
    map <Esc>[8~ $
    imap <Esc>[8~ <C-o>$
endif

