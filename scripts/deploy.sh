#!/bin/bash
# Commit and push all changes

# Move to root of directory
cd $( git rev-parse --show-toplevel )

# Do some validation checks
echo "-- Checking unique ids"
duplicates=$( find _posts/ -name "*.md" -type f -exec grep -m 1 unique_id {} \; | sed 's/unique_id: //g' | sort | uniq -d )
if [[ -n "$duplicates" ]]; then
    echo "Found duplicate unique ids: $duplicates"
    for duplicate in $duplicates; do
	grep "$duplicate" _posts/*.md
    done
    exit 1
fi

for post in $( git status | grep modified:.*_posts | sed 's/modified://g' | xargs -n1 echo ); do
    echo "-- Validating post: $post"
    if ! cat "$post" | grep -q "unique_id"; then
	echo "Missing unique_id for $post"
	exit 1
    fi
done

echo "-- Validation complete, pushing"

# Commit and push
if [[ $# -eq 0 ]]; then
    commit_msg="update site"
else
    commit_msg="$1"
fi
git add . && git commit -m "$commit_msg" && git push

echo "-- Pushed, removing tmp files"

rm -f */*~
rm -f *~

echo "-- Latest version deployed!"