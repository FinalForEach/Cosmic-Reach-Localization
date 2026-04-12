
import os
import math

def check_font_files():
    unique_chars_file = "unique_chars.txt"
    font_dir = os.path.join("..", "font")
    
    with open(unique_chars_file, "r", encoding="utf-8") as f:
        unique_chars = set(f.read())

    # Group characters by unicode block
    char_groups = {}
    for char in unique_chars:
        block = math.floor(ord(char) / 256)
        if block not in char_groups:
            char_groups[block] = set()
        char_groups[block].add(char)

    # Check for missing font files
    existing_font_files = os.listdir(font_dir)
    missing_files = {}

    for block in sorted(char_groups.keys()):
        expected_filename = f"cosmic-reach-font-{hex(block)[2:].upper().zfill(2)}00.png"
        if expected_filename not in existing_font_files:
            missing_files[block] = expected_filename

    if not missing_files:
        print("Success: All character groups have an associated font image.")
    else:
        print("Failure: Missing font image files found.")
        for block, filename in missing_files.items():
            print(f"Missing file: {filename}")
            print("Character grid (16x16):")
            for i in range(16):
                line = ""
                for j in range(16):
                    char_code = block * 256 + i * 16 + j
                    char = chr(char_code)
                    if char in unique_chars:
                        line += char
                    else:
                        line += "■"
                print(line)
            print("-" * 20)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    check_font_files()
