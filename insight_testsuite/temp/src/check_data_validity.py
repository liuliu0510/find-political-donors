import datetime

def check_otherID(Other_ID):
  #only consider individual contributions, where Other_Id is empty 
    if Other_ID:
        print "Other_ID not empty"
        return False
    else:
        return True
        
def check_transactionDate(Transaction_DT):
  #make sure the transaction date is valid(MMDDYYYY) 
    if len(Transaction_DT)!=8:
        return False
    try:
        date=datetime.datetime.strptime(Transaction_DT, '%m%d%Y')
     #   if not date:
      #      raise ValueError('invalid date')
    #if date is not the format of MMDDYYYY or value is not correct, like MM>12, return false
    except ValueError:
        print "date invalid"
        return False 
    else:
        #transaction date shouldn't beyond today's date
        if date>datetime.datetime.today():
            return False
        else:
            return True

def check_zipCode(Zip_Code):
    if Zip_Code=="" or len(Zip_Code)<5 or len(Zip_Code)>9 or Zip_Code.isdigit()==False:
        print "zipcode invalid"
        return False
    else:
        return True

def check_cmteID_and_transactionAMT(CMTE_ID,Transaction_AMT):
    #CMTE_ID and Transaction_AMT fields shouldn't be empty 
    if CMTE_ID and Transaction_AMT:
        return True
    else:
        print "CMTE_ID or Transaction_AMT empty"
        return False
        
