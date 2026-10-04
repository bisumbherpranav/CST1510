"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  IT
Date  :  01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0        # Create a count for OVER LIMIT

while True:        # Starts a while loop
    hostname=input(f"Enter hostname (or type 'quit' to exit): ")    # Enter hostname or type 'quit'

    if hostname == "quit":              # if user types 'quit' then program is terminated
        print("\nProgram terminated")
        break

    used = 0       

    for i in range(3):          # Loops 3 times
        value = int(input(f"Enter value {i+1}: "))   # asking for values (in this case, 3 values)
        used+=value                                # adds up all 3 values together --> a+b+c = used

    total=0         # Total GB 
    free=total-used     # Free GB left
    percent=(used/total)*100        # Percentage of Used GB value

    if percent>=100:            # if percentage is over 100%, status is 'OVER LIMIT'
        status=("OVER LIMIT")
        over_limit_count+=1         # Adds one to the 'OVER LIMIT' counter
    elif percent>=90:               # if percent between 90% and 99%, then prints 'WARNING'
        status=("WARNING")
    else:
        status=("OK")       # if anything below 90%, it prints 'OK'

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f" Used    : {used:>10.2f} GB")
    print(f" Total   : {total:>10.2f} GB")
    print(f" Free    : {free:>10.2f} GB")
    print(f" Percent : {percent:>10.2f} %")
    print(f" Status  : {status:>10}")
    print("="*34)
# if user types 'quit', the program is terminated along with this line printed with the 'OVER LIMIT' count
print(f"Session over. Total OVER LIMIT reached: {over_limit_count} ")

