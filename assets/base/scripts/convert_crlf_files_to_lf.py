import os
import click

def convert_crlf_to_lf(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    content = content.replace(b'\r\n', b'\n')

    with open(file_path, 'wb') as f:
        f.write(content)

def convert_crlf_to_lf_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                convert_crlf_to_lf(file_path)

@click.command()
@click.argument('directory_path', default='.')
def main(directory_path):
    convert_crlf_to_lf_in_directory(directory_path)

if __name__ == "__main__":
    main()