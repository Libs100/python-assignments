import sys
from collections import Counter

def calculate_statistics(sequence):
    """Calculate statistics for a given sequence."""
    total = len(sequence)
    counts = Counter(sequence)
    stats = {
        "A": counts.get("A", 0),
        "C": counts.get("C", 0),
        "G": counts.get("G", 0),
        "T": counts.get("T", 0),
        "Unknown": total - sum(counts.get(base, 0) for base in "ACGT"),
        "Total": total,
    }
    for key in stats:
        if key != "Total":
            stats[key] = (stats[key], stats[key] / total * 100 if total > 0 else 0)
    return stats

def print_statistics(stats, label="File"):
    """Print statistics in a formatted way."""
    print(f"{label}:")
    for base, (count, percentage) in stats.items():
        if base == "Total":
            print(f"Total:   {count}")
        else:
            print(f"{base}: {count:>8} {percentage:5.1f}%")
    print()

def analyze_files(file_paths):
    """Analyze one or more files and display statistics."""
    all_sequences = []
    if not file_paths:
        print("No files received")
        return
    for file_path in file_paths:
        with open(file_path, "r") as file:
            sequence = file.read().replace("\n", "").upper()
            stats = calculate_statistics(sequence)
            print_statistics(stats, label=file_path)
            all_sequences.extend(sequence)
    
    # Overall statistics
    overall_stats = calculate_statistics(all_sequences)
    print_statistics(overall_stats, label="All")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seq.py <file1> <file2> ...")
        sys.exit(1)
    
    file_paths = sys.argv[1:]
    analyze_files(file_paths)

