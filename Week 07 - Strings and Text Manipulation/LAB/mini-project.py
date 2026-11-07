"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  IT
Date  :  04/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.


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


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

total_records = 0
flagged_records = 0
with open("my_messy_lines.txt") as f:  # opens "my_messy_lines.txt" file
    for line in f:  # loop line by line
        record = parse_line(
            line
        )  # parse each line with parse_line function and store in record var
        print(
            {
                "hostname": record["hostname"],
                "used": record["used"],
                "total": record["total"],
            }  # print hostname, used and total and put everything in a dict
        )  # print hostname with its status - calls status_of with used and total from record
        print(f"{record["hostname"], status_of(record["used"], record["total"])}\n")
        total_records += 1
        if status_of(record["used"], record["total"]) == "FLAGGED":
            flagged_records += 1

    print(f"{total_records} records processed; {flagged_records} were FLAGGED")
# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
