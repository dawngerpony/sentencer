#!/usr/bin/env bash
## Sort the vocabulary file in-place.

filename=vocabulary.csv
timestamp=$(date +%s)
tmp_filename=/tmp/${filename}.sorted

cp $filename "${filename}.bak.${timestamp}"
sort -t , -k 1,1 -n ${filename} > ${tmp_filename}
mv ${tmp_filename} $filename
