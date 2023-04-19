import os
import sys
from pathlib import Path

# Get the directory to execute in from the command-line argument
if len(sys.argv) > 1:
    mydir = Path(sys.argv[1])
else:
    mydir = Path("")

# Create a new file called "output.txt" and open it in write mode
# The "with" statement ensures the file is automatically closed when the block is exited
with open("output.txt", "w") as output_file:
    
    # Iterate over all PDF files in the current working directory
    for file in mydir.glob('*.pdf'):
        
        # Define two command-line tools to run on each file
        command1 = "sha256sum"
        command2 = "pdfx"
        
        # Write the name of the current file and a horizontal line to the output file
        output_file.write(f"\n\n{file.name}:\n")
        output_file.write("-" * 50 + "\n")
        
        # Run the first command and write its output to the output file
        output_file.write(f"{command1}:\n")
        output = os.popen(f"{command1} '{file.name}'").read()
        output_file.write(output)
        
        # Run the second command and write its output to the output file
        output_file.write(f"{command2}:\n")
        output = os.popen(f"{command2} '{file.name}'").read()
        output_file.write(output)
