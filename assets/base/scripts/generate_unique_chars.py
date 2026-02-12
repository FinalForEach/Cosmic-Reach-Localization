import os
import json
import re
import click

@click.command()
@click.option('--lang', type=str, default=None, help='Optional language code to check a specific folder. E.g., en_us. Defaults to None to check all folders.')
def find_unique_characters(lang: str):
    lang_dir = os.path.join("..", "lang")
    output_file = "unique_chars.txt"
    unique_chars = set()

    folders_to_check = []
    if lang:
        specific_folder_path = os.path.join(lang_dir, lang)
        if os.path.isdir(specific_folder_path):
            folders_to_check.append(lang)
        else:
            print(f"Error: Language folder '{lang}' not found.")
            return
    else:
        folders_to_check = [f for f in os.listdir(lang_dir) if os.path.isdir(os.path.join(lang_dir, f))]

    for lang_folder in folders_to_check:
        lang_folder_path = os.path.join(lang_dir, lang_folder)
        for filename in os.listdir(lang_folder_path):
            if filename.endswith(".json"):
                filepath = os.path.join(lang_folder_path, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    for line in f:
                        # Find all string literals in the line
                        for match in re.finditer(r'":\s*"(.*?)"', line):
                            for char in match.group(1):
                                unique_chars.add(char)


    with open(output_file, "w", encoding="utf-8") as f:
        for char in sorted(list(unique_chars)):
            f.write(char)

    print(f"Unique characters saved to {output_file}")

if __name__ == "__main__":
    # The script is expected to be run from the `scripts` directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    find_unique_characters()
