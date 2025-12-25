import json
import os
import click

def validate_json_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True, "Success"
    except json.JSONDecodeError as e:
        return False, str(e)
    except FileNotFoundError:
        return False, "File not found"

def validate_json_in_directory(directory):
    results = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                success, reason = validate_json_from_file(file_path)
                if not success:
                    results[file_path] = reason
    return results

@click.command()
@click.argument('directory_path', default='.')
def main(directory_path):
    try:
        results = validate_json_in_directory(directory_path)
        if len(results) == 0:
            print("Language files are valid!")
        else:
            for path, reason in results.items():
                print(path + ": " + reason)
            raise ValueError("Found syntax errors.")
    except ValueError as ex:
        print("Language files are NOT valid!", ex)
        exit(1)

if __name__ == "__main__":
    main()
