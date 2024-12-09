#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import csv
import os
from datetime import datetime
from Bio import Entrez

# Set up email for NCBI
Entrez.email = "libisaad100@gmail.com"  

def download_ncbi_data(database, term, number):
    try:
        try:
            print(f"🔍 Searching NCBI database '{database}' for term '{term}'...")
            handle = Entrez.esearch(db=database, term=term, retmax=number)
            search_results = Entrez.read(handle)
            handle.close()
        except Exception as e:
            print(f"❌ Error in Entrez.esearch for term '{term}' in database '{database}': {e}")
            return [], 0
        
        ids = search_results["IdList"]
        total_found = search_results["Count"]

        filenames = []
        for ncbi_id in ids:
            try:
                handle = Entrez.efetch(db=database, id=ncbi_id, rettype="fasta", retmode="text")
                data = handle.read()
                handle.close()
                
                filename = f"{database}_{ncbi_id}.fasta"
                with open(filename, "w") as f:
                    f.write(data)
                filenames.append(filename)
            except Exception as e:
                print(f"❌ Error downloading ID {ncbi_id}: {e}")

        return filenames, total_found
    except Exception as e:
        print(f"❌ Error occurred while downloading data from NCBI: {e}")
        return [], 0

def log_search_details(csv_filename, date, database, term, max_number, total_found, status="success"):
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total", "status"])
        writer.writerow([date, database, term, max_number, total_found, status])

def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI databases.")
    parser.add_argument("--database", default="nucleotide", help="NCBI database to search (default: nucleotide)")
    parser.add_argument("--term", required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Number of items to download (default: 10)")

    args = parser.parse_args()
    
    # Clean and validate the term
    args.term = args.term.strip()
    if not args.term.isalnum():
        print(f"⚠️ Warning: The search term '{args.term}' contains non-alphanumeric characters.")

    print(f"Searching {args.database} for '{args.term}'...")
    filenames, total_found = download_ncbi_data(args.database, args.term, args.number)

    if filenames:
        print("Downloaded files:")
        for filename in filenames:
            print(f"  {filename}")
    else:
        print("No files downloaded.")

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_search_details("search_log.csv", current_date, args.database, args.term, args.number, total_found, status="failed" if total_found == 0 else "success")
    print("Search details logged to search_log.csv")

if __name__ == "__main__":
    main()


# In[ ]:




