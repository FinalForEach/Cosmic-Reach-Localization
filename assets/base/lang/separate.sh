#!/bin/bash

# Base directory where folders are located
BASE_DIR="."

# Loop through all subdirectories
for dir in "$BASE_DIR"/*/; do
    # Path to game.json
    GAME_JSON="${dir}game.json"
    
    # Path to tip.json
    TIP_JSON="${dir}tip.json"

    # Check if game.json exists in the folder
    if [ -f "$GAME_JSON" ]; then
        # Extract lines starting with "Tip"
        grep '^\s*\"Tip' "$GAME_JSON" > tips_temp.txt

        # Start writing to tip.json, wrapping in valid JSON
        echo "{" > "$TIP_JSON"
        
        # Initialize a flag to check if it's the first tip
        first=true

        # Read the tips from the temporary file
        while IFS= read -r line; do
            # Escape quotes in the line using sed
            escaped_line=$(echo "$line" | sed 's/"/\\"/g')

            # Add the line formatted as a JSON key-value pair
            echo "$line" >> "$TIP_JSON"

            # Set first to false after the first line
            first=false
        done < tips_temp.txt
        
        # Close the JSON object
        echo "}" >> "$TIP_JSON"
        
        # Remove the temporary file
        rm tips_temp.txt

        echo "tip.json created in $dir"
    else
        echo "No game.json found in $dir"
    fi
done