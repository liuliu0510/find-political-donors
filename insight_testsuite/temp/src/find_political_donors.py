from check_data_validity import *
from get_median import *
import datetime

def processData():
    zipDict={}
    dateDict={}
    for line in open('input/itcont.txt','r'):
        readData = line.split('|')
        cmteID = readData[0]
        zipCode = readData[10]
        transDate = readData[13]
        transAMT = readData[14]
        otherID = readData[15]
            
        if(check_otherID(otherID)==False or check_cmteID_and_transactionAMT(cmteID, transAMT)==False):
            continue
        
        if(check_zipCode(zipCode)==True):
            newLine=medianByZip(cmteID,zipCode,transAMT,zipDict)
           # writePath="../output/medianvals_by_zip.txt"
            writeZipFile(newLine,"output/medianvals_by_zip.txt")
        
        if(check_transactionDate(transDate)==True):
            medianByDate(cmteID,transDate,transAMT,dateDict)
    writeDateFile(dateDict,"output/medianvals_by_date.txt")



def medianByZip(cmteID,zipCode,transAMT,zipDict):
    zipCode=zipCode[:5]
    transAMT=int(transAMT)
    if (cmteID,zipCode) not in zipDict:
        newTrans=GetMedianByHeap()
    else:
        newTrans=zipDict[(cmteID,zipCode)]
    newTrans.add(transAMT)
    zipDict[(cmteID,zipCode)]=newTrans
    newMedian=newTrans.getMedian()
    totalTrans=newTrans.getTotalTrans()
    totalAMT=newTrans.getTotalAMT()
    #print "%s|%s|%s|%s|%s" % (cmteID,zipCode,newMedian,totalTrans,totalAMT)
    newLine = "%s|%s|%s|%s|%s\n" % (cmteID,zipCode,newMedian,totalTrans,totalAMT)
    return newLine

def medianByDate(cmteID,transDate,transAMT,dateDict):
    transAMT=int(transAMT)
    date=datetime.datetime.strptime(transDate, '%m%d%Y')
    if (cmteID,date) not in dateDict:
        newTrans=GetMedianByHeap()
    else:
        newTrans=dateDict[(cmteID,date)]
    newTrans.add(transAMT)
    #print newTrans.getMedian()
    #print newTrans.getTotalTrans()
    #print newTrans.getTotalAMT()
    dateDict[(cmteID,date)]=newTrans



def writeZipFile(newLine,writePath):
    with open(writePath,'a') as wf:
        wf.write(newLine)
    wf.close()


def writeDateFile(dateDict,writePath):
    with open(writePath,'a') as wf:
        for key in sorted(dateDict.iterkeys()):
            cmteID=key[0]
            date=datetime.datetime.strftime(key[1], '%m%d%Y')
            newMedian=dateDict[key].getMedian()
            totalTrans=dateDict[key].getTotalTrans()
            totalAMT=dateDict[key].getTotalAMT()
            newLine= "%s|%s|%s|%s|%s\n" % (cmteID,date,newMedian,totalTrans,totalAMT)
            wf.write(newLine)
    wf.close()


def main():
    processData()
    

if __name__ == "__main__":
	main()
