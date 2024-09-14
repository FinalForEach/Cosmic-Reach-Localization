#!/bin/bash

# Define the base directory and the regex pattern
BASE_DIR="."
REGEX="^\s*\"\$schema"

# Loop through each game.json file in the subdirectories
find "$BASE_DIR" -type f -name "tip.json" | while read -r file; do
    # Delete lines matching the regex pattern
    sed -i "/$REGEX/d" "$file"
    echo "Processed $file"
done