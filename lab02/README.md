
# Lab 2: Manipulating Data Types in Computational Biology

This repository contains Python scripts developed for Lab 2, focusing on manipulating data types to solve various computational biology problems. The scripts include functionalities for cleaning DNA sequences, parsing sequence name information from FASTQ files, converting sequence information between different amino acid representations, and calculating bond lengths and angles from atomic coordinates.

## Requirements

- Python 3.x
- No external libraries are required for these scripts.

## Files Description

- `seqCleaner.py`: Cleans up DNA sequences by removing ambiguous bases denoted by "N" and replaces them with a count in curly brackets.
  - Sample Input: `AaNNNNNNGTC`
  - Expected Output: `AA{6}GTC`
- `fastqParse.py`: Parses sequence name information from a FASTQ file's seqname line and displays each field on a new line.
  - Sample Input: `@EAS139:136:FC706VJ:2:2104:15343:197393`
  - Expected Output:
    ```
    Instrument = EAS139
    Run ID = 136
    Flow Cell ID = FC706VJ
    Flow Cell Lane = 2
    Tile Number = 2104
    X-coord = 15343
    Y-coord = 197393
    ```
- `converter.py`: Converts sequence information between different amino acid representations using mappings (e.g., from 3-letter codon codes to one-letter amino acid codes).
  - Sample Input: `ATG`
  - Expected Output: `ATG = MET`
- `coordinateMathSoln.py`: Takes three sets of atomic coordinates, calculates the bond lengths and angles, and outputs them with the correct number of significant digits.
  - Sample Input: `C = (39.447, 94.657, 11.824) N = (39.292, 95.716, 11.027) Ca = (39.462, 97.101, 11.465)`
  - Expected Output:
    ```
    N-C bond length = 1.33
    N-Ca bond length = 1.46
    C-N-Ca bond angle = 124.0
    ```

## Running the Scripts

To run the scripts, open a terminal or command prompt in the directory containing the scripts and execute the following commands:

- **seqCleaner.py**
  ```bash
  python seqCleaner.py
  ```
  Follow the prompt to input a DNA sequence.

- **fastqParse.py**
  ```bash
  python fastqParse.py
  ```
  Input a FASTQ seqname line when prompted.

- **converter.py**
  ```bash
  python converter.py
  ```
  Provide a codon or amino acid representation as input when prompted.

- **coordinateMathSoln.py**
  ```bash
  python coordinateMathSoln.py
  ```
  Enter three sets of atomic coordinates on a single line as prompted.

## Additional Notes

- Ensure Python 3.x is installed and properly set up in your environment.
- The input format for `coordinateMathSoln.py` should follow the specific structure outlined in the lab instructions for accurate results.
