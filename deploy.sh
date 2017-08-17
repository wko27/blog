#!/bin/bash
# Commit and push all changes

# Do some validation checks
for post in $( git status | grep modified:.*_posts | sed 's/modified://g' | tr -d '[:space:]' ); do
    echo "-- Validating post: $post"
    expectedTitle=$( echo "${post%.*}" | cut -d '-' -f 4- | sed 's/[^a-z]//g' )
    actualTitle=$( cat "$post" | grep "title" | head -n 1 | sed 's/title: //' | sed 's/[^a-z]//g' )
    if [[ "$expectedTitle" != "$actualTitle" ]]; then
	echo "Expected title to be $expectedTitle but found $actualTitle"
	exit 1
    fi
done

echo "-- Validation complete, pushing"

# Commit and push
git add . && git commit -m 'update site' && git push

echo "-- Pushed, removing tmp files"

rm -f */*~
rm -f *~

echo "-- Latest version deployed!"