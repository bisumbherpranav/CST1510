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
        return (self.value / self.limit) * 100
    
    def status(self):
        """Returns OVER LIMIT, WARNING, or OK based on the percent() method"""
        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"
        
    def is_over(self):
        """Checks if value > limit and returns bool"""
        return self.value > self.limit
        
def load_records(path):
    """Load my own records from my_own_data.txt file"""
    records = []
    with open(path) as f:
        for line in f:      # read line
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))  # append to list
    return records
over_limit = 0
records = load_records('my_own_data.txt')

for record in records:      # loop over records
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