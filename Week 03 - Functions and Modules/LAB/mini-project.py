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

def status_of(percent):
    """Determine status of percentage and returns OVER LIMIT, WARNING or OK"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    """Calculate and return difference and percentage"""
    percent = (value/limit)*100     # calculates percentage
    difference = value - limit      # calculates difference
    return difference, percent      # returns both difference and percentage

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
    status = status_of(percent) # calls the status_of function
    if status == "OVER LIMIT":  
        over_limit+=1       # adds 1 to the counter if status is over limit
    print_report(label, value, limit, difference, percent, status)  
    # calls the print_report with label, value, limit, difference, percent and status passed into the parameter

# if user types 'quit', the program is terminated along with this line printed with the 'OVER LIMIT' count
print(f"Session over. Total OVER LIMIT reached: {over_limit} ")