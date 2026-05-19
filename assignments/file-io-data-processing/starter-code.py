import csv
import json
from pathlib import Path

# Task 1: Read and Write Text Files
def process_text_file(input_file, output_file):
    """
    Read a text file, process each line, and write to output file.
    
    TODO: Implement this function
    - Open input_file and read line by line
    - Process each line (e.g., convert to uppercase, filter empty lines, etc.)
    - Write processed lines to output_file
    - Handle FileNotFoundError and PermissionError
    - Use try/except blocks and context managers (with statement)
    """
    pass


# Task 2: Parse and Transform CSV Data
def analyze_csv(input_csv, output_csv):
    """
    Read CSV file, perform analysis or filtering, and write results.
    
    TODO: Implement this function
    - Use csv.DictReader or csv.reader to parse CSV
    - Apply filtering or aggregation logic
    - Calculate statistics if needed
    - Write results using csv.DictWriter or csv.writer
    - Handle malformed CSV gracefully
    """
    pass


# Task 3: Convert Between Formats
def text_to_csv(text_file, csv_file):
    """
    TODO: Convert text file to CSV format
    - Parse structured text data
    - Write to CSV with appropriate headers
    """
    pass


def csv_to_json(csv_file, json_file):
    """
    TODO: Convert CSV file to JSON format
    - Read CSV with headers
    - Create list of dictionaries
    - Write to JSON file with proper formatting
    """
    pass


def json_to_text(json_file, text_file):
    """
    TODO: Convert JSON file to readable text format
    - Read JSON data
    - Format as human-readable text
    - Write to text file
    """
    pass


if __name__ == "__main__":
    # Test your functions here
    # Example:
    # process_text_file("input.txt", "output.txt")
    pass
