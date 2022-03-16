#!/bin/bash

# remove empty lines
cat root/001.txt | grep -v -e "^$" | grep -v -e "^ " | grep -v -e "^  " > temp.txt
mv temp.txt root/001_v2.txt

# prepare into .po format 
python3 scripts/sentences_to_transifex.py 001_v2

# create directory structure folder
mkdir stats
mkdir wip
mkdir wip/en
mkdir wip/bo

# add english file
touch wip/en/001.po

# clean up
mv root/001_v2.po wip/bo/001.po

# word_segment statistics
python3 scripts/token_statistics.py
