# 📘 Assignment: File I/O and Data Processing

## 🎯 Objective

Master reading, writing, and processing files in Python. You'll work with text files, CSV data, and JSON formats to build practical skills for handling real-world data. By completing this assignment, you'll understand file operations, error handling, and how to transform data between different formats.

## 📝 Tasks

### 🛠️ Read and Write Text Files

#### Description
Create a program that reads data from a text file, processes it, and writes the results to a new file. Implement error handling for missing or corrupted files.

#### Requirements
Completed program should:

- Open and read a text file line by line
- Process each line (filter, transform, or analyze content)
- Write processed data to an output file
- Handle file not found errors gracefully
- Handle file permission errors gracefully
- Close files properly (or use context managers)

### 🛠️ Parse and Transform CSV Data

#### Description
Load a CSV file, parse the data, filter or aggregate it based on criteria, and write the results to a new CSV file or JSON file.

#### Requirements
Completed program should:

- Read data from a CSV file
- Parse rows and columns correctly
- Filter data based on specific conditions
- Calculate aggregates (sum, average, count, etc.)
- Write results to a new CSV or JSON file
- Handle malformed CSV data without crashing

### 🛠️ Convert Between File Formats

#### Description
Build a utility that converts data between different file formats (text to CSV, CSV to JSON, JSON to text). Support at least two conversion pairs.

#### Requirements
Completed program should:

- Convert data from one format to another accurately
- Preserve data integrity during conversion
- Handle edge cases (empty files, special characters, nested JSON)
- Provide clear feedback about conversion success or failure
- Support at least two different conversion types
