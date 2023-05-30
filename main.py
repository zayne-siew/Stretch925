import argparse
import os
import re
import subprocess


def config(filename: str) -> None:

    ROOT_DIR = os.path.abspath(os.curdir)
    YML_DIR = f'{ROOT_DIR}/cv/pipeline_config.yml'

    # Read the contents of the yml file
    with open(YML_DIR, 'r', encoding='utf-8') as file:
        contents = file.read()

    # Use regular expression to replace only the specific custom Node lines
    contents = re.sub(r"custom_nodes\.dabble\..*", f'custom_nodes.dabble.{filename}_stretch', contents)
    contents = re.sub(r"custom_nodes\.draw\..*", f'custom_nodes.draw.{filename}_stats', contents)

    # Write the modified contents back to the yml file
    with open(YML_DIR, 'w', encoding='utf-8') as file:
        file.write(contents)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Stretch925',
        description='Take a break. Have a stretch.'
    )
    parser.add_argument("exercise", choices=['arm', 'neck', 'side'])

    args = parser.parse_args()
    config({'arm': 'yw', 'neck': 'ms', 'side': 'lat'}[args.exercise])
    os.chdir('cv')
    subprocess.run(["peekingduck", "run"])
