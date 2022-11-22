import os
from pathlib import Path

mydir = Path("")
for file in mydir.glob('*.pdf'):
    command = "sha256sum"
    command2 = "pdfx"
    print(" ")
    print(" ")
    os.system(command + " " + "'" + file.name + "'")
    print(" ")
    os.system(command2 + " " + "'" + file.name + "'")

    