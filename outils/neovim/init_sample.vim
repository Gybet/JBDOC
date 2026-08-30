" =========================
" Configuration générale
" =========================

" Afficher les numéros de lignes
set number

" Recherche sensible si une majuscule est utilisée
set smartcase

" Indentation
set tabstop=4
set shiftwidth=4
set expandtab

" =========================
" Raccourcis clavier
" =========================

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l


" =========================
" Plugins
" =========================

call plug#begin()

Plug 'tpope/vim-surround'

call plug#end()