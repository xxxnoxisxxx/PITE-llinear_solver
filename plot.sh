#!/bin/bash

gnuplot <<- EOF
    set term png
    set out 'solution.png'
    set grid
    set xrange [-$3-$3-0.1:$3+$3+0.1]
    f(x)= $1
    g(x) = $2
    plot f(x) t 'f(x)='.'$1', g(x) t 'g(x)='.'$2', '+' using ($3):($4) t '('.'$3'.','.'$4'.')'
EOF
