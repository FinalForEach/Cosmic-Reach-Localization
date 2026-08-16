import json
import os
import sys
import click

def validate_json_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True, None, "Success"
    except json.JSONDecodeError as e:
        return False, e.lineno, str(e)
    except FileNotFoundError:
        return False, None, "File not found"

def validate_json_in_directory(directory):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                success, line, reason = validate_json_from_file(file_path)
                if not success:
                    results[file_path] = (line, reason)
    return results

@click.command()
@click.argument('directory_path', default='.')
@click.option('--github', is_flag=True, default=False, help="Emit GitHub Actions error annotations")
def main(directory_path, github):
    results = validate_json_in_directory(directory_path)
    if len(results) == 0:
        print("Language files are valid!")
    else:
        for path, (line, reason) in results.items():
            rel_path = os.path.relpath(path)
            if github:
                if line:
                    print(f"::error file={rel_path},line={line}::{reason}")
                else:
                    print(f"::error file={rel_path}::{reason}")
            else:
                print(f"{path}: {reason}")
        print("Language files are NOT valid!")
        sys.exit(1)

if __name__ == "__main__":
    main()
