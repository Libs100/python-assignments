import re
import argparse
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

def calculate_at_content(sequence):
    """
    Calculates the AT content of a DNA sequence.
    """
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    return (a_count + t_count) / len(sequence) * 100 if len(sequence) > 0 else 0

def print_divider():
    print("\n" + "🔬" + "—" * 50 + "🔬")

def analyze_file(file_path, find_repeats=False, calculate_gc=False, calculate_at=False):
    """
    Reads a DNA sequence from a file and performs analyses.
    """
    try:
        record = next(SeqIO.parse(file_path, "fasta"))  # Assumes FASTA format
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return
    
    sequence = str(record.seq).upper()
    print_divider()
    print(f"🌿 Analyzing sequence from file: {file_path}")
    print(f"📏 Sequence length: {len(sequence)}")
    
    if find_repeats:
        longest_repeat = find_longest_repeated_subsequence(sequence)
        print(f"🔁 Longest repeated subsequence: {longest_repeat if longest_repeat else 'None found'}")
    
    if calculate_gc:
        gc = calculate_gc_content(sequence)
        print(f"🧬 GC content: {gc:.2f}%")
    
    if calculate_at:
        at = calculate_at_content(sequence)
        print(f"🌟 AT content: {at:.2f}%")

    print_divider()

def main():
    parser = argparse.ArgumentParser(description="🌟 DNA Sequence Analysis Tool 🌟")
    parser.add_argument("file_path", type=str, help="Path to the FASTA file")
    parser.add_argument("--duplicate", action="store_true", help="Find longest repeated subsequence")
    parser.add_argument("--gc", action="store_true", help="Calculate GC content")
    parser.add_argument("--at", action="store_true", help="Calculate AT content")
    
    args = parser.parse_args()
    analyze_file(args.file_path, args.duplicate, args.gc, args.at)

if __name__ == "__main__":
    main()
