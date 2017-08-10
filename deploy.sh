#!/bin/bash

git add . && git commit -m 'update site' && git push
rm -f */*~
rm -f *~