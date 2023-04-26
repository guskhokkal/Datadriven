
import pandas as pd
import re


ds = pd.read_csv("C:\\Users\\alexa\\Downloads\\jobtech_dataset2022.csv")

#check how many rows in the database
print(len(ds))

# Create a new dataset for rows containing "nurs"
jobtech_nurses = []

# Loop through each row in the dataframe
for index, row in ds.iterrows():
    # Loop through each column in the row and check for the term 'nurse'
    for column in ds.columns:
        if 'vgr' in str(row[column]).lower() and 'sjuksköterska' in str(row[column]).lower():
            jobtech_nurses.append(row)
            break

# Print the matching rows
for row in jobtech_nurses:
    #print(row)
    print(ds['description'])

#check how many instances are in the dataframe
print(len(jobtech_nurses))

#change the list back into a dataset
nurses = pd.DataFrame(jobtech_nurses)

#now export to both a new csv file and a excel file
nurses.to_csv('~/Desktop/sjuksköterskor.csv', index=False)
nurses.to_excel('~/Desktop/sjuksköterskor.xlsx', index=False)
