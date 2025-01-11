# DNA Sequence Analysis Tool

## Overview
This program analyzes DNA sequences stored in a FASTA file format. It performs two key analyses:
1. **Finding the Longest Repeated Subsequence**: Identifies the longest subsequence that repeats itself within the input DNA sequence.
2. **Calculating GC Content**: Computes the percentage of guanine (G) and cytosine (C) nucleotides in the DNA sequence.

## Features
- **Input**: Accepts a DNA sequence in FASTA format.
- **Outputs**:
  - Length of the DNA sequence.
  - The longest repeated subsequence, if any.
  - GC content of the sequence as a percentage.

## Requirements
This program requires the following:
- Python 3.x
- [Biopython](https://biopython.org/) library for reading and parsing FASTA files.

### Installation
To install Biopython, run:
```bash
pip install biopython
