#!/bin/bash
# Create a new post with the given title

if [[ $# -eq 0 ]]; then
    echo "Usage: ./new_post.sh (title)" 1>&2
    exit 1
fi

title="$1"
escaped_title=$( echo "$title" | tr ' ' '_' )

new_post=../_posts/"$( date +%F )"-"$escaped_title".md

if [[ -e "$new_post" ]]; then
    echo "File $new_post already exists"
else
    cp post_template.md "$new_post"
    sed -i .tmp "s/__title__/$title/g" "$new_post"
    rm "$new_post".tmp
fi

emacs "$new_post"