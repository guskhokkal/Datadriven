
import pandas as pd
import re

#importing the dataset from the downloads folder with help from pandas
ds = pd.read_csv("C:\\Users\\alexa\\Downloads\\jobtech_dataset2022.csv")

#check how many rows in the database to compair with the result of the new dataset
print(len(ds))

# Create a new dataset as a list for now. 
jobtech_nurses = []

# Loop through each row in the dataset and if they contain 'VGR' or 'sjuksköterska' they get added to the empty list created above
for index, row in ds.iterrows():
    # Loop through each columns in the dataset
    for column in ds.columns:
        #.lower makes the found text in the database lower case so we can compare with out termonology
        if 'vgr' in str(row[column]).lower() and 'sjuksköterska' in str(row[column]).lower():
            jobtech_nurses.append(row)
            break

# Print the matching rows description, more to check that it worked
for row in jobtech_nurses:
    print(ds['description'])

#check how many instances are in the dataframe to comapire with the original to evaluate if the result is possible
print(len(jobtech_nurses))

#change the list back into a dataset again using pandas
nurses = pd.DataFrame(jobtech_nurses)

#now export to both a new csv file and a excel file, the csv to do futher work with while the excel file is to open and analyse ourselves
#Also choosing to export to desktop so they are easier to find
nurses.to_csv('~/Desktop/sjuksköterskor.csv', index=False)
nurses.to_excel('~/Desktop/sjuksköterskor.xlsx', index=False)
