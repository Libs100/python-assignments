import re
from Bio import SeqIO

def find_longest_repeated_subsequence(sequence):
    """
    Finds the longest subsequence that repeats itself in the given sequence.
    """
    n = len(sequence)
    longest = ""
    for length in range(1, n // 2 + 1):
        for i in range(n - length + 1):
            subseq = sequence[i:i + length]
            pattern = re.compile(subseq)
            if len(pattern.findall(sequence)) > 1 and len(subseq) > len(longest):
                longest = subseq
    return longest

def calculate_gc_content(sequence):
    """
    Calculates the GC content of a DNA sequence.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return (g_count + c_count) / len(sequence) * 100 if len(sequence) > 0 else 0

def analyze_file(file_path):
    """
    Reads a DNA sequence from a Fasta file and performs analyses.
    """
    try:
        record = next(SeqIO.parse(file_path, "fasta"))  # Assumes FASTA format
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    sequence = str(record.seq).upper()
    print(f"\nSequence from file: {file_path}")
    print(f"Length of sequence: {len(sequence)}")
    
    # Perform analyses
    longest_subsequence = find_longest_repeated_subsequence(sequence)
    gc_content = calculate_gc_content(sequence)
    
    print(f"\nLongest repeated subsequence: {longest_subsequence}")
    print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    # Change the file path if needed
    file_path = "example.fa"
    analyze_file(file_path)
