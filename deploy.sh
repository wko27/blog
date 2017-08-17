#!/bin/bash
# Commit and push all changes

# Do some validation checks
for post in $( git status | grep modified:.*_posts | sed 's/modified://g' | tr -d '[:space:]' ); do
    echo "Verifying post: $post"
    expectedTitle=$( echo "${post%.*}" | cut -d '-' -f 4- )
    actualTitle=$( cat "$post" | grep "title" | head -n 1 | sed 's/title: //' )
    if [[ "$expectedTitle" != "$actualTitle" ]]; then
	echo "Expected title to be $expectedTitle but found $actualTitle"
	exit 1
    fi
done

# Commit and push
git add . && git commit -m 'update site' && git push
rm -f */*~
rm -f *~