"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  AI 
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Determine status of percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def check_record(value,limit):
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

def load_records(path):
    """Reads label, value, limit lines from the file and returns a list of dicts"""
    records=[]
    try:
        with open(path) as f:  # open file with file name passed in the parameter
            for line in f:  # read line by line
                label,value,limit=line.strip().split(',')   # remove whitespaces and split each items
                records.append({'label': label, 'value': float(value), 'limit': float(limit)})
                # add dict to list and convert value and limit to float
    except FileNotFoundError:
        print(f"FILE DOES NOT EXIST: {path}")
        return []  # if file not found, prints a clear message and returns a empty list 
    return records  # returns list of dicts
records = load_records('my_own_data.txt')
# records = load_records('not_existing_file.txt')  --> Prints the FileNotFoundError message
over_limit = 0    # start a count for over-limit

with open('my_own_output.txt','w') as f:
    """Loop over records -> call check_record() and print_report()"""
    for row in records:    
        # store label,value & limit in their respective variable names so easily accessible
        label,value,limit=row['label'],row['value'],row['limit']  
        difference, percent = check_record(value,limit)  # calls check_record function 
        status = status_of(percent) # calls status_of function
        if status == "OVER LIMIT":
            over_limit+=1       # add 1 to the over limit counter if status is OVER LIMIT
        print_report(label, value, limit, difference, percent, status)  # calls print_report 
        f.write(f"{label},{status}\n")      # writes 'label,status'

"""Writes the label,status in a new file call 'my_own_output.txt'"""
with open('my_own_output.txt') as f:
    print(f.read())      # read my_own_output.txt and print each line

# After reviewing every line, the program is terminated along with this line printed with the 
# 'OVER LIMIT' count"""
print(f"Session over. Total OVER LIMIT reached: {over_limit} ")