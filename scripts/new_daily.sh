#!/bin/bash
# Create a new daily with the given title

set -e # Exit immediately if a command exits with a non-zero status.
set -u # Treat unset variables as an error when substituting.

help_text() {
    echo "Usage:"
    echo "  $0 [title]"
    echo "    - Creates new daily with title"
    echo "  $0 [title] --tmr"
    echo "    - Creates a new daily for tomorrow with the given title"
    exit 0
}

if [[ $# -eq 0 || $# -gt 2 ]]; then
    help_text
fi

title="$1"
create_for_tomorrow=false
if [[ $# -eq 2 &&  "$2" = "--tmr" ]]; then
    create_for_tomorrow=true
fi

escaped_title=$( echo "$title" | tr ' ' '_' )
unique_id=$( echo "$escaped_title" | tr '[:upper:]' '[:lower:]' )

if [[ $create_for_tomorrow = "true" ]]; then
    date_prefix=$( date -v+1d +%F )
else
    date_prefix=$( date +%F )
fi

new_daily=../_daily/"$date_prefix"-"$escaped_title".md

if [[ -e "$new_daily" ]]; then
    echo "File $new_daily already exists"
else
    cp daily_template.md "$new_daily"
    sed -i .tmp "s/__title__/$title/g" "$new_daily"
    sed -i .tmp "s/__unique_id__/$unique_id/g" "$new_daily"
    rm "$new_daily".tmp
fi

emacs "$new_daily"

echo "Created: $new_daily"