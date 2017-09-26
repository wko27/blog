#!/bin/bash
#  Edit the last daily

last=$( ls -1r ../_posts/*.md | head -n 1 )
emacs "$last"
