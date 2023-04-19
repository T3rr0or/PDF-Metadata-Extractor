# PDF Analysis Tool
This is a Python script that analyzes PDF files using two command-line tools: sha256sum and pdfx. The script can be used to extract metadata and other information from multiple PDF files at once and store the results in a single text file.

Requirements:

- Python 3.x

- Command-line tools sha256sum and pdfx (typically installed on Linux or macOS systems)


Usage
Open a terminal window.
Navigate to the directory containing the pdf_analysis_tool.py script.
To execute the script in the current working directory, enter the following command:

```
python pdf_analysis_tool.py
```

To execute the script in a specific directory, provide the directory path as a command-line argument:
bash

```
python pdf_analysis_tool.py /path/to/directory
```

The script will analyze all PDF files in the specified directory and write the results to a text file called 'output.txt'. The output for each file will include the name of the file, the SHA-256 hash calculated by 'sha256sum', and the metadata and other information extracted by 'pdfx'.

## Output
The output is written to a text file called output.txt in the same directory as the script. Each file's output is separated by a horizontal line and includes the following information:

- File name
- SHA-256 hash calculated by sha256sum
- Metadata and other information extracted by pdfx


That's it! With these instructions, you should be able to use the PDF Analysis Tool to quickly analyze multiple PDF files and extract useful information.
