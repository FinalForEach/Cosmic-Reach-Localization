#!/bin/bash

# The line to be inserted
insert_line='  "$schema": "https://https://raw.githubusercontent.com/FinalForEach/Cosmic-Reach-Localization/master/assets/base/lang/game.schema.json",'

# Loop through each folder and find game.json files
find . -type f -name "game.json" | while read -r file; do
  # Insert the line at line 2 using sed
  sed -i '2i\'"$insert_line" "$file"
done
