#!/bin/bash

source .languages

# remove empty lines
cat root/001.txt | grep -v -e "^$" | grep -v '^ *$' > temp.txt
mv temp.txt root/001_v2.txt

# prepare into .po format 
python3 scripts/sentences_to_transifex.py 001_v2

# create directory structure folder
mkdir stats
mkdir wip
mkdir wip/$SOURCE_LANGUAGE
mkdir wip/$TARGET_LANGUAGE

# add add language files
touch wip/$TARGET_LANGUAGE/001.po
mv root/001_v2.po wip/$SOURCE_LANGUAGE/001.po

# create transifex config file
cat transifex.yml | sed s'/_source_language_/'"$SOURCE_LANGUAGE"'/'g > transifex_temp.yml
mv transifex_temp.yml transifex.yml

# word_segment statistics
python3 scripts/token_statistics.py
