"""
# Day 24 - CSV File IO
"""

#####################################################################
# NOTE: Always save data files to the same folder as your script files

# Introducing CSV (comma-separated value) files
##  A text file used for storing tabular data
##  Each line represents a data record.
##  Fields within the record are separated by commas.
##########################
# Review:
#  with open(filename, mode) as file_object:
#       import csv
#       statements

# All reads below start at current cursor position in the file
#    The data type in a text file is a string.
#  csv.reader(file_object) -- reads rows from a CSV_file into a list of strings
#  csv.writer(file_object) -- allows writing of rows (iterable data type) into a CSV_file
#       csvFile.writerows(data) -- writes multiple rows (each being a list) to the CSV_file
##########################
'''
###############################
# How do you work with the text in a .csv file?
#   Assume file_object is a file that has been opened.

# 1. To look at every character,
#   bigstring = file_object.read() # a string
# 2. To look at every record of data,
#   dataRecords = csv.reader(file_object)
#   # a list of strings (representing each field in the record)

# Then loop through the string or list, as appropriate
#  and solve your problem.
################
'''
####################
# READ a csv file - fallactivity.csv

''' standard file IO all lines  '''
def readcsvOLD(filename):
    with open(filename, "r") as inCSV:
        # read all lines (i.e. rows) into a list object
        theLines = inCSV.readlines()

        #   create a empty list for the data
        csvdata = []
        # loop through the list object
        for line in theLines:       
            # create a list of item lists (a list of records)
            # add the list of data items to the list of data
            csvdata.append(line.strip().split(","))
        # display the data
        print(f"The file has {len(csvdata)} rows.\n{csvdata}")
        
##readcsvOLD('fallactivity.csv')

''' csv file IO all lines '''
def readcsvNEW(filename):
    with open(filename, "r") as inCSV:
        import csv
        # read all lines (i.e. rows) into a csv list object (a listing of item lists)
        # create a list of item lists (a list of records)
        csvdata = list(csv.reader(inCSV))
        # display the data list
        print(f"The file has {len(csvdata)} rows.\n{csvdata}")

##readcsvNEW('fallactivity.csv')

''' csv file IO separate header from data '''
def readcsvALL(filename):
    with open(filename, "r") as inCSV:
        import csv
        # read all lines (i.e. rows) into a csv list object (a listing of item lists)
        # create a list of item lists (a list of records)
        csvFile = csv.reader(incsv)
        # Read the header and all rows
        header = next(csvFile)
        data = list(csvFile)
        # display the data list
        print(f"The file has {len(data)+1} rows.\n{header}\nrows 1-{len(data)}:\n{data}")
        
##readcsvALL('fallactivity.csv')

####################
# WRITE a csv file - fallactivity.csv
def writeCSV(filename):
    import csv
    header = ["item", "quantity", "price"]
    data = [["apples", 4, .79], ["oranges", 3, .89], ["bananas", 6, .39]]
    
    # Write the data to the CSV file
    with open(filename, "w", newline='') as outCSV:
        # prepare output file for writing
        outFile = csv.writer(outCSV)
        
        # Write the header row to the file
        outFile.writerow(header)
        # Write the data rows to the file
        outFile.writerows(data)
    

##writeCSV('inventory.csv')
        
####################
# EXAMPLE - put it all together
## write a function that will read 'grocery_sales.csv' and write a csv file
## 'grocery_salesProfit.csv', with an addtional column 'profit' which is a result 
## of the calculation (quantitySold * pricePerItem).
##def salesprofit(input_file, output_file):
##    import csv
##
##    """ check if the input file exists """
##
##    """ Display, the input CSV file does not exists """
##    if found == False:
##        print(reason)
##    else:
##        """ Read data, the input CSV file exists """
##        with open(input_file, "r") as inCSV:
##            csvFile = csv.reader(inCSV)
##            
##            # Read the header and data rows
##
##            
##            # add 'Profit' to header to create new_header 
##            
##            # create an empty new_data List to store the new rows with the 'profit' column
##            
##            # Calculate 'profit' for each row data, and append it to the new_data list
##
##                # unpack the row values on to data item variables
##
##                # Calculate profit = (quantitySold) * (pricePerItem)
##
##                # Append all row data item variables including profit, as a list on to the new_data list
##    
##    """ Write the updated data to the output CSV file """
##    with open(output_file, "w", newline='') as outCSV:
##        # prepare output file for writing
##
##        
##        # Write the new header row to the file
##
##        
##        # Write the new data rows to the file
##
##
##salesprofit('grocery_sales.csv', 'grocery_salesprofit.csv')


