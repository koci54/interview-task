#!/bin/bash

tail -n +2 data-bash.txt | sort -V | sed "s/\t[^\t]*$/\t$(date +'%d\/%m\/%Y %H\:%M')/" > updated-data.txt