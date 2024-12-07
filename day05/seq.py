import sys
import os

def main():
    # Get the list of file paths from the command line arguments
    args = sys.argv
    if len(args) < 2:
        print('No files received')
        return
    
    file_names = args[1:]  # Exclude the script name
    combined_results = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 0}
    
    for file_name in file_names:
        try:
            result = parse_file(file_name)
            print(f"\n{file_name}")
            print_result(result)
            
            # Update combined results
            for key in combined_results:
                combined_results[key] += result[key]
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing '{file_name}': {e}")
    
    print("\nAll")
    print_result(combined_results)

def parse_file(file_name):
    """Parses a file and counts occurrences of A, C, G, T, and unknown characters."""
    with open(file_name, 'r') as f:
        data = f.read().strip().upper()
    
    if len(data) == 0:
        print(f"Warning: The file '{file_name}' is empty.")
        return {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 0}

    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in nucleotide_counts:
        count = data.count(nucleotide)
        nucleotide_counts[nucleotide] = count

    total_characters = len(data)
    unknown_count = total_characters - sum(nucleotide_counts.values())
    nucleotide_counts['Unknown'] = unknown_count
    nucleotide_counts['Total'] = total_characters

    return nucleotide_counts

def print_result(result):
    """Prints the statistics of the nucleotide counts in the format you requested."""
    for key in ['A', 'C', 'G', 'T', 'Unknown']:
        count = result[key]
        total = result['Total']
        percentage = (count / total * 100) if total > 0 else 0
        print(f"{key}: {count:>9} {percentage:5.1f}%")
    print(f"Total:  {result['Total']:>5}\n")

if __name__ == '__main__':
    main()
