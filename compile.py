"""
Simple Compilation Script

{name.html} is replaced with the contents of the file name.html
"""

import shutil
import os
import re

source = "src"
target = "dist"

include_re = re.compile(r"\{([^{}]+)\}")

def include(match):

    filename = match.group(1)
    include_path = os.path.join(source, filename)

    return compile_file(include_path)

def compile_file(path):

    file = open(path, "r", encoding="utf-8")
    text = file.read()
    file.close()

    return include_re.sub(include, text)

if os.path.exists(target):
    
    shutil.rmtree(target)

os.makedirs(target)

for root, directories, files in os.walk(source):

    if "blocks" in directories:

        directories.remove("blocks")

    relative_root = os.path.relpath(root, source)

    output_root = os.path.join(target, relative_root)

    os.makedirs(output_root, exist_ok=True)

    for filename in files:

        source_file = os.path.join(root, filename)
        output_file = os.path.join(output_root, filename)

        if filename.endswith(".html"):

            file = open(output_file, "w", encoding="utf-8")
            file.write(compile_file(source_file))
            file.close()
        
        else:

            shutil.copy2(source_file, output_file)
