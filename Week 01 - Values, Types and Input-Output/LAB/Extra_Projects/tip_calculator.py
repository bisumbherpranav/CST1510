
bill = float(input("What was the total bill:    $ "))                # Ask for the total bill.
people = int(input("How many people are splitting it:   "))          # Ask for how many people are splitting it.
tip_percentage = int(input("What is the tip percentage:     "))      # Ask for the tip percentage.
should_pay = (bill/people) * (1 + (tip_percentage/100))              # Calculate what each person owes and 
print(f"Each person should pay: $ {should_pay:.2f}")                 # Print it formatted to exactly 2 decimal places.

