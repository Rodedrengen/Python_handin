import os
from pathlib import Path
import argparse

parser= argparse.ArgumentParser(description='Utility module to work with files')

parser.add_argument('--choice', help='Choose what function to execute')
parser.add_argument('-f','--folderpath', help='What folder to work on')
parser.add_argument('-o','--output', help='The name of the output file')

args = parser.parse_args();

if __name__ == '__main__':
    print("status")

def get_file_names(folderpath,out="./data/output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    filesInFolder = os.listdir(folderpath)

    with open(out, 'a') as file_object:
        for line in filesInFolder:
            file_object.write(line)
            file_object.write("\n")

def get_all_file_names(folderpath,out="./data/output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    
    with open(out, 'w') as file_object:
        for path in Path(folderpath).rglob('*'):
            file_object.write(str(path))
            file_object.write("\n")

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open(file, 'r') as file_object:
            first_line = file_object.readline()
        print(first_line.strip())

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in file_names:
        with open(file, 'r') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if "@" in line:
                    print(line.strip())

def write_headlines(md_files, out="./data/output.txt"):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    output = ""

    for file in md_files:
        with open(file, 'r') as file_object:
            lines = file_object.readlines()
            output += str([line for line in lines if line[0] == "#"]) + "\n"

    with open(out, 'w') as file_object:
            file_object.write(output)