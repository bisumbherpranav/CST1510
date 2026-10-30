"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  AI    
Date  :  25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    def __init__(self, label, value, limit):
        """Initialise Record class with its attributes label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Returns value as a percentage over limit"""
        return (self.value / self.limit) * 100      # returns percentage
    
    def status(self):
        """Returns OVER LIMIT, WARNING, or OK based on the method percent(), 
            greater than 100, 90 or less"""
        percent = self.percent()       # store percentage from .percent() in a variable
        if percent >= 100:
            return "OVER LIMIT"     # returns OVER LIMIT if percent is 100 or more
        elif percent >= 90:
            return "WARNING"        # returns WARNING if percent is between 90 and 99
        else:
            return "OK"         # if none applied, returns OK
        
    def is_over(self):
        """Checks if value > limit and returns bool"""
        return self.value > self.limit      # compare if value is more than limit then returns bool
        
def load_records(path):
    """Load my own records from my_own_data.txt file"""
    records = []    # an empty list
    with open(path) as f:       # open a file with file name passed into path
        for line in f:      # read line by line
            label, value, limit = line.strip().split(",")   
            # remove whitespaces and split it like CSV fields
            records.append(Record(label, float(value), float(limit)))   
            # append each object into the list and convert value and limit to float
    return records      # returns a list of Record objects
over_limit = 0      # start a count for over limit
records = load_records('my_own_data.txt')
# load up my_own_data.txt file and calls load_records and stores it

for record in records:      # loop over each records in the list
    # formatted print report:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Rows Loaded   : {record.value:>9}")
    print(f"  Rows Expected : {record.limit:>9}")
    print(f"  Percent       : {record.percent():>10.2f} %")
    print(f"  Status        : {record.status():>10}")
    print("="*34)
    if record.is_over():        # calls is_over function, check if value > limit
        over_limit+=1           # if so, adds 1 to the over_limit counter
# print one line summary of how many records are over limit
print(f"\n{over_limit} of {len(records)} records are OVER LIMIT")