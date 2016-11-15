;; From: https://www.emacswiki.org/emacs/BNFMode
(define-generic-mode 'bnf-mode
  () ;; comment char: inapplicable because # must be at start of line
  nil ;; keywords
  '(
    ("^#.*" . 'font-lock-comment-face) ;; comments at start of line
    ("^<[-a-zA-Z0-9 ]+>" . 'font-lock-function-name-face) ;; LHS nonterminals
    ("<[-a-zA-Z0-9 ]+>" . 'font-lock-builtin-face) ;; other nonterminals
    ("::=" . 'font-lock-const-face) ;; "goes-to" symbol
    ("\|" . 'font-lock-warning-face) ;; "OR" symbol
    )
  '("\\.bnf\\'") ;; filename suffixes
  nil ;; extra function hooks
  "Major mode for BNF highlighting.")
