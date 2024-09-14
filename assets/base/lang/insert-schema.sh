#!/bin/bash

BASE_DIR="."
REGEX="^\s*\"\$schema"
FILE_NAME="game.json"
# The line to be inserted
insert_line='  "$schema": "https://raw.githubusercontent.com/FinalForEach/Cosmic-Reach-Localization/master/assets/base/lang/game.schema.json",'

# Loop through each game.json file in the subdirectories
find "$BASE_DIR" -type f -name "$FILE_NAME" | while read -r file; do
    # Delete lines matching the regex pattern
    sed -i "/$REGEX/d" "$file"
    echo "Processed $file"
done

# Loop through each folder and find game.json files
find . -type f -name "$FILE_NAME" | while read -r file; do
  # Insert the line at line 2 using sed
  sed -i '2i\'"$insert_line" "$file"
done
