"""
RECORD CHECK  -  my version
===========================

Name  :  Pranav Bisumbher
Lane  :  AI
Date  :  27/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd  # import panda module to work with dataframe
import matplotlib.pyplot as plt  # import pyplot from the matplotlib module for the graph

df = pd.read_csv(
    "my_own_data.csv"
)  # import and read my own data file from "my_own_data.csv" file

df["percent"] = ((df["value"] / df["limit"]) * 100).round(1)
# add a percent column by calculating each values as a percentage over limit from each rows, and rounded to 1 decimal place

print(f"Print Dataframe as it is with its percent column:\n{df}")   # print the df as it is with its percent column
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)   # add a status column by applying a lambda function to the percent column
    # compare each percent value (p) and return whether its OVER LIMIT, WARNING or OK

not_ok = df[df["status"] != "OK"]
# filter out only the rows that have status as "WARNING" or "OVER LIMIT"
print(f"\nTake out rows that have 'OK' in status:\n{not_ok}")   # and print them

grouped_by_status = (                    
    df.groupby("status")["status"]          # group df by status 
    .value_counts()                         # add count for each group
    .plot(kind="bar", title="Sever counts per status")      # specify its a bar chart and gave it a title
)
print(f"\nValue counts of each status group\n{df["status"].value_counts()}")   
# print how many values in each status group
plt.tight_layout()      # prevent labels from overlapping
plt.savefig("my_status_counts_bar.png")     
# save the bar chart to a png file "my_status_counts_bar.png"
df.to_csv("my_results.csv", index=False)
# save df to a new file call my_results.csv with its columns names