import os
from pathlib import Path

mydir = Path("")
with open("output.txt", "w") as output_file:
    for file in mydir.glob('*.pdf'):
        command1 = "sha256sum"
        command2 = "pdfx"
        output_file.write(f"\n\n{file.name}:\n")
        output_file.write("-" * 50 + "\n")
        output_file.write(f"{command1}:\n")
        output = os.popen(f"{command1} '{file.name}'").read()
        output_file.write(output)
        output_file.write(f"{command2}:\n")
        output = os.popen(f"{command2} '{file.name}'").read()
        output_file.write(output)
