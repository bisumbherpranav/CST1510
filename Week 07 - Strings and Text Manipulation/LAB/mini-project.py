"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  IT
Date  :  07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """Cleans and parses one raw, messy line into a dict"""
    line = raw_line.strip()
    # removes spaces from the beginning and the end, not the spaces inside string
    hostname, rest = line.split(",", 1)  # split at the first comma
    hostname = hostname.strip().lower() 
    # removes spaces from the end and convert to lowercase
    values = {}  # creates an empty dict
    for item in rest.split(","):  # rest.split(",") creates a list for items in rest
        # items -> " used=87 " and " total=100"
        key, value = item.split("=")  # split at "=" -> used = key and 87 = value
        values[key.strip().lower()] = float(value.strip())
        # ValueError: could not convert string to float: 'no'
    return {"hostname": hostname, "used": values["used"], "total": values["total"]}


def status_of(used, total):  # define status_of takes used and total value
    """Return OVER LIMIT, WARNING or OK for a used/total pair"""
    percent = (used / total) * 100  # calculates percentage
    if percent >= 100:
        return "OVER LIMIT"  # returns OVER LIMIT if percent 100 or more
    elif percent >= 90:
        return "WARNING"  # returns WARNING if percent 90 or more
    else:
        return "FLAGGED"  # returns FLAGGED if none applied


total_records = 0
flagged_records = 0
with open("my_messy_lines.txt") as f:  # opens "my_messy_lines.txt" file
    for line in f:  # loop line by line
        record = parse_line(
            line
        )  # parse each line with parse_line function and store in record var.
        print(
            {
                "hostname": record["hostname"],
                "used": record["used"],
                "total": record["total"],
            }  # print hostname, used and total and put everything in a dict
        )
        print(f"{record["hostname"], status_of(record["used"], record["total"])}\n")
        # print hostname with its status - calls status_of with used and total for each record

        total_records += 1  # adds one to the counter for every records processed
        if status_of(record["used"], record["total"]) == "FLAGGED":
            # calls status_of for each record with 'used' and 'total' - check if status returns "FLAGGED"
            flagged_records += 1  # adds 1 to the counter for every flagged records

    print(f"{total_records} records processed; {flagged_records} were FLAGGED")
    # print one line summary - how many records, how many flagged
