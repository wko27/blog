#!/bin/bash
# Create a new daily with the given title

if [[ $# -eq 0 ]]; then
    echo "Usage: ./new_daily.sh (title)" 1>&2
    exit 1
fi

new_daily=../_daily/"$( date +%F )"-"$1".md

if [[ -e "$new_daily" ]]; then
    echo "File $new_daily already exists"
else
    cp daily_template.md "$new_daily"
    sed -i .tmp "s/__title__/$1/g" "$new_daily"
    rm "$new_daily".tmp
fi

emacs "$new_daily"