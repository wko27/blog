#!/bin/bash
#  Edit the last daily

last=$( ls -1r ../_daily/*.md | head -n 1 )
emacs "$last"
