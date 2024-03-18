# Genome Analyzer

This project consists of a Python-based genome analysis tool that calculates and reports various statistics about a given genome sequence, such as sequence length in megabases, GC content, and relative codon usage. It uses a modular design with `genomeAnalyzer.py` as the main program and `sequenceAnalysis.py` as a supporting module that includes necessary classes and functions.

## Requirements

- Python 3.x

Ensure that Python 3 is installed on your system. This code has been tested with Python 3.8, but it should be compatible with other Python 3 versions.

## Files

- `genomeAnalyzer.py`: The main Python script that performs genome analysis.
- `sequenceAnalysis.py`: A Python module containing classes and methods for sequence analysis.
- `testGenome.fa`: A sample input file in FastA format containing genome sequences to be analyzed.

## Setup

1. Place `genomeAnalyzer.py`, `sequenceAnalysis.py`, and your FastA format input file (e.g., `testGenome.fa`) in the same directory.

2. Open a terminal or command prompt and navigate to the directory containing the files.

## Running the Program

To run the genome analysis, execute the following command in your terminal:

```bash
python genomeAnalyzer.py < testGenome.fa
