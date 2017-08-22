#!/bin/bash
# Create a new post with the given title

if [[ $# -eq 0 ]]; then
    echo "Usage: ./new_post.sh (title)" 1>&2
    exit 1
fi

new_post=../_posts/"$( date +%F )"-"$1".md

if [[ -e "$new_post" ]]; then
    echo "File $new_post already exists"
else
    cp post_template.md "$new_post"
    sed -i .tmp "s/__title__/$1/g" "$new_post"
    rm "$new_post".tmp
fi

emacs "$new_post"