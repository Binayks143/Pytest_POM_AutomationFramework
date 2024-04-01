import csv
'''
This Python function, getCSVData(fileName), reads data from a CSV (Comma Separated Values) 
file and returns the data as a list of rows
'''

def getCSVData(fileName):
    #Create a EMpty list to store rows
    rows=[]
    #open the csv file in read mode
    dataFile=open(fileName,'r')
    #create a CSV reader from CSV file
    reader=csv.reader(dataFile)
    #skip the header
    next(reader)
    #add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows