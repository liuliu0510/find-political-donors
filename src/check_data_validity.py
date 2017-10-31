import datetime

"""
functions to check data validity, according to the predefined limitions.

"""


#only consider individual contributions, where Other_Id is empty
def check_otherID(Other_ID):
    if Other_ID:
        #print "Other_ID not empty"
        return False
    else:
        return True

 
#only consider individual contributions, where Other_Id is empty       
def check_transactionDate(Transaction_DT):
    if len(Transaction_DT)!=8:
        return False
    try:
        date=datetime.datetime.strptime(Transaction_DT, '%m%d%Y')
    #if date is not the format of MMDDYYYY or value is not correct, like MM>12, return false
    except ValueError:
        #print "date invalid"
        return False 
    else:
        #transaction date shouldn't beyond today's date
        if date>datetime.datetime.today():
            return False
        else:
            return True


#make sure zipcode has at least 5 digits and no more than 9 digits
def check_zipCode(Zip_Code):
    if Zip_Code=="" or len(Zip_Code)<5 or len(Zip_Code)>9 or Zip_Code.isdigit()==False:
        #print "zipcode invalid"
        return False
    else:
        return True


#CMTE_ID and Transaction_AMT fields shouldn't be empty 
def check_cmteID_and_transactionAMT(CMTE_ID,Transaction_AMT):
    if CMTE_ID and Transaction_AMT:
        return True
    else:
        #print "CMTE_ID or Transaction_AMT empty"
        return False
        
