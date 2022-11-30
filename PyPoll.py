# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete lost of candidates who recived votes.
# 3. The percentage of votes each candidate won.
# 4. The totalnumber of votes each candidate won.
# 5. The winner of the election base on the popular vote.
#import datetime
#now = datetime.datetime.now()
#print("The time right now is ", now)
#import datetime as dt
#now=dt.datetime.now()
#print("the time right now is", now)
#election_data = open(file_to_load, 'r')
#election_data.close()
#file_to_load = 'Resources/election_results.csv'
#with open(file_to_load) as election_data:
    #print(election_data)
# Assign a variable for the file to load and the path.
import csv
import os
# Open the election results and read the file
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # Print the file object
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#outfile=open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Write some data to the file. 
    #txt_file.write("Hello World")
# Write three Header to the file.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("------------------------\n")
# Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  # Print the header row.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file
    #for row in file_reader:
        #print(row)
   