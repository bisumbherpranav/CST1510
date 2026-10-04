"""
RECORD CHECK  -  my version
===========================

Name  : Pranav Bisumbher
Lane  :  AI/Data Science     
Date  : 9/25/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

dataset_name = input("Enter the dataset name: ")                # Ask user for the data set name (e.g. covid-19 survery)

rows_loaded = int(input("Enter number of rows loaded: "))       # Ask user for rows of data that was loaded

rows_expected = int(input("Enter number of rows expected: "))   # Ask user for rows of data that was to be expected

difference = rows_loaded - rows_expected                        # calculates difference between rows loaded and rows expected 
percent = (rows_loaded/rows_expected)*100                       # calculates percentage difference for rows loaded over rows expected

# report here
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {dataset_name}")
print("=" * 34)
print(f" Rows Loaded        :{rows_loaded:>8}")
print(f" Rows Expected      :{rows_expected:>8}")
print(f" Difference         :{difference:>+11.2f}")
print(f" Percent            :{percent:>11.2f}%")

# shows the exact margin of less data than expected or more data than expected
print(f" Percent Difference :{(difference/rows_expected)*100:>+11.2f}%") 
print("=" * 34)
