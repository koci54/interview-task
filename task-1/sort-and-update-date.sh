#!/bin/bash

tail -n +2 data-bash.txt | sort -V | sed "s/\t[^\t]*$/\t$(date +'%d\/%m\/%Y %H\:%M')/" > updated-data.txt

# from tldr tail:
# -show all file since line 'num'
# tail -n {{num}} {{file}}

# from man sort:
# -V natural sort of (version) numbers within text

# from tldr sed - Edit text in a scriptable manner.
# sed 's/{{regex}}/{{replace}}/' {{filename}}

# $(date +'%d\/%m\/%Y %H\:%M') - date format we want output

# * matches for zero or more of the preceding expression
# $ matches expression at end of line
# [^ ] matches characters not in the range of a list
# \t matches a tab character
