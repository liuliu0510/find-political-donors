from check_data_validity import *
from get_median import *
import datetime
import sys
import os.path

"""
processData():read the input file, extract the data fields we need. 
Using 2 dictionaries: zipDict and dateDict to preserve the information. 
zipDict utilizes (cmteID,zipCode) as the key
dateDict utilizes (cmteID,transDate) as the key

call functions medianByZip() and medianByDate() separately to process each qualified 
line, then write results to the two output files `medianvals_by_zip.txt` and 
`medianvals_by_date.txt` by calling writeFile() function
"""
def processData(inputPath,zipOutPath,dateOutPath):
    zipDict = {}
    dateDict = {}
    for line in open(inputPath,'r'):
        readData = line.split('|')
        #if the input line is not the standard FEC format, neglect it
        if len(readData)!=21:
            continue
        cmteID = readData[0]
        zipCode = readData[10]
        transDate = readData[13]
        transAMT = readData[14]
        otherID = readData[15]
            
        if(check_otherID(otherID)==False or check_cmteID_and_transactionAMT(cmteID, transAMT)==False):
            continue
        
        if(check_zipCode(zipCode)==True):
            newLine = medianByZip(cmteID,zipCode,transAMT,zipDict)
            writeFile(newLine, zipOutPath)
        
        if(check_transactionDate(transDate)==True):
            medianByDate(cmteID,transDate,transAMT,dateDict)
    
    #write lines to dateFile by keys order, instead of every input line
    for key in sorted(dateDict.iterkeys()):
            cmteID = key[0]
            date = datetime.datetime.strftime(key[1], '%m%d%Y')
            newMedian = dateDict[key].getMedian()
            totalTrans = dateDict[key].getTotalTrans()
            totalAMT = dateDict[key].getTotalAMT()
            newLine = "%s|%s|%s|%s|%s\n" % (cmteID,date,newMedian,totalTrans,totalAMT)
            writeFile(newLine, dateOutPath)


""" process data by zipcode """
def medianByZip(cmteID,zipCode,transAMT,zipDict):
    zipCode = zipCode[:5]
    transAMT = int(transAMT)
    #if keys not exist in the dictionary, define a new one by the class
    if (cmteID,zipCode) not in zipDict:
        newTrans = GetMedianByHeap()
    else:
        newTrans = zipDict[(cmteID, zipCode)]
    newTrans.add(transAMT)
    zipDict[(cmteID,zipCode)] = newTrans
    newMedian = newTrans.getMedian()
    totalTrans = newTrans.getTotalTrans()
    totalAMT = newTrans.getTotalAMT()
    #print "%s|%s|%s|%s|%s" % (cmteID,zipCode,newMedian,totalTrans,totalAMT)
    newLine = "%s|%s|%s|%s|%s\n" % (cmteID,zipCode,newMedian,totalTrans,totalAMT)
    return newLine


""" process data by transaction date """
def medianByDate(cmteID,transDate,transAMT,dateDict):
    transAMT = int(transAMT)
    date = datetime.datetime.strptime(transDate, '%m%d%Y')
    if (cmteID,date) not in dateDict:
        newTrans = GetMedianByHeap()
    else:
        newTrans = dateDict[(cmteID,date)]
    newTrans.add(transAMT)
    #print newTrans.getMedian()
    #print newTrans.getTotalTrans()
    #print newTrans.getTotalAMT()
    dateDict[(cmteID,date)] = newTrans


""" write to files """
def writeFile(newLine,writePath):
    with open(writePath,'a') as wf:
        wf.write(newLine)
    wf.close()


def main():
    try:
        script,inputPath,zipOutPath,dateOutPath = sys.argv 
    except IndexError:
        print "Number of parameters is not right. It should contains 4: python find_political_donors.py input output1 output2"
    
    if not os.path.isfile(inputPath):
        print "Input file does not exist"
        sys.exit()
    
    #make sure the input file exists
    try:
        wf = open(zipOutPath,'w')
        wf.close()
    except IOError:
        print "The given Zip Output file doesn't exist/cannot be created"
        sys.exit()
    
    try:
        wf = open(dateOutPath,'w')
        wf.close()
    except IOError:
        print "The given Date Output file doesn't exist/cannot be created"
        sys.exit()
        
    processData(inputPath,zipOutPath,dateOutPath)
    

if __name__ == "__main__":
	main()
