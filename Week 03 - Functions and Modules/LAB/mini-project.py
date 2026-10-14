"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  AI  
Date  :  11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""User type in data (dataset name, rows loaded, rows expected), calculates the
    difference and percent and prints it in a formatted report. 
    While loop runs True until user types quit, then kill the program"""

def status_of(percent, over_limit):
    """Determine status and the over limit counter"""
    if percent >= 100:
        over_limit+=1
        return "OVER LIMIT", over_limit
    elif percent >=90:
        return "WARNING", over_limit
    else:
        return "OK", over_limit

def check(value,limit):
    """Calculate and return difference and percentage"""
    percent = (value/limit)*100
    difference = value - limit
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the final formatted  data report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows Loaded   : {value:>10.2f}")
    print(f"  Rows Expected : {limit:>10.2f}")
    print(f"  Difference    : {difference:>10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>9}")
    print("="*34)

over_limit = 0  # start a count for over-limit
while True:
    label = input("Enter dataset name: ")
    if label == "quit":              # if user types 'quit' then program is terminated
        print("\nProgram terminated")
        break
    value = float(input("Enter rows loaded: "))         # ask user for rows loaded
    limit = float(input("Enter rows expected: "))       # ask user for rows expected
    difference, percent = check(value, limit)           # calls the check function 
    status, over_limit = status_of(percent, over_limit) # calls the status_of function

    print_report(label, value, limit, difference, percent, status)  # calls the print_report 

# if user types 'quit', the program is terminated along with this line printed with the 'OVER LIMIT' count
print(f"Session over. Total OVER LIMIT reached: {over_limit} ")

