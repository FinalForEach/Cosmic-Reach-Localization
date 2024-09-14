#!/bin/bash

# Loop through each directory
for dir in */; do
  # Check if "odd-tips.json" exists in the directory
  if [ -f "$dir/odd-tips.json" ]; then
    # Create the "spoilers" subfolder if it doesn't exist
    mkdir -p "$dir/spoilers"
    
    # Move the "odd-tips.json" file to the "spoilers" folder
    mv "$dir/odd-tips.json" "$dir/spoilers/"
    
    echo "Moved odd-tips.json to $dir/spoilers/"
  fi
done