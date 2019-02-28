#!/bin/sh
# Name:
# By Robbert Gurdeep Singh
################################################################################
echo "" > /tmp/score.txt
for g in in/*.txt
    do
    name="${g#in}"
    python3 start.py "$g" > /tmp$name 2>> /tmp/score.txt
done

score=$(cat /tmp/score.txt | grep -o '^[0-9]*' | tr '\n' '+' | sed 's/$/0\n/' | bc)

rm /tmp/hc-*.zip
zip -r /tmp/hc-$score.zip *.py

echo "$score points"

