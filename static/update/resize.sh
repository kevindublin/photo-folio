#!/bin/bash
# Resize jpg directory to 25% in a subdirectory named resized


mkdir -p resized/

for f in *; do mv "$f" `echo $f | tr ' ' '_'`; done
for f in *; do mv "$f" `echo $f | tr -s '-' '_'`; done

for i in $( ls *.jpg); do convert -resize 25% $i ./resized/$i; done
