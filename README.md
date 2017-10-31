# Find Political Donors 
1. [Introduction](README.md#introduction)
2. [Details of challenge](README.md#details-of-challenge)
3. [Input file](README.md#input-file)
4. [Output files](README.md#output-files)
5. [Approaches](README.md#approaches)
6. [Packages required](README.md#packages-required)
10. [Methods to run](README.md#methods-to-run)
11. [Tips](README.md#tips)

# Introduction
My solution to the Coding challenge of Insight Data Engineering, which is written in Python.


# Details of challenge

We’re given one input file, `itcont.txt`. Each line of the input file contains information about a campaign contribution that was made on a particular date from a donor to a political campaign, committee or other similar entity. Out of the many fields listed on the pipe-delimited line, we’re primarily interested in the zip code associated with the donor, amount contributed, date of the transaction and ID of the recipient.

After providing the data, we need to write results to 2 different files: `medianvals_by_zip.txt` and `medianvals_by_date.txt`, according to some requirements.


## Input file

The Federal Election Commission provides data files stretching back years and is [regularly updated](http://classic.fec.gov/finance/disclosure/ftpdet.shtml)

For the purposes of this challenge, we’re interested in individual contributions with the following fields:  

* `CMTE_ID`: identifies the flier, which for our purposes is the recipient of this contribution
* `ZIP_CODE`:  zip code of the contributor (we only want the first five digits/characters)
* `TRANSACTION_DT`: date of the transaction
* `TRANSACTION_AMT`: amount of the transaction
* `OTHER_ID`: a field that denotes whether contribution came from a person or an entity 


## Output files

**`medianvals_by_zip.txt`**

The first output file `medianvals_by_zip.txt` should contain the same number of lines or records as the input data file minus any records that were ignored as a result of the 'Input file considerations.'

Each line of this file contains these fields:
* recipient of the contribution  
* 5-digit zip code of the contributor  
* running median of contributions received by recipient from the contributor's zip code streamed in so far.  
* total amount of contributions received by recipient from the contributor's zip code streamed in so far

 
**`medianvals_by_date.txt`**

Each line of this file contains these fields:
* recipeint of the contribution 
* date of the contribution  
* median of contributions received by recipient on that date.  to the next dollar) 
* total number of transactions received by recipient on that date
* total amount of contributions received by recipient on that date

This second output file does not depend on the order of the input file, and in fact should be sorted alphabetical by recipient and then chronologically by date.


# Approaches
This program mainly consists 3 files: `find_political_donors.py`, `check_data_validity.py`, and `get_median.py`

`check_data_validity.py` is used for checking input data's validity. Make sure they conform to those requirements, like: the `OTHER_ID` should be empty, the `CMTE_ID` and `Transaction_AMT` shouldn't be empty.

`get_median.py` defines a class `getMedianByHeap` which is used to find medians of the data. Of course, We can use the numpy package of Python, `numpy.median()` to find the median of input list. However, here I choose another strategy(using 2 heaps) to realize that, which I think is better. 

Since for the `medianvals_by_zip.txt` output file, we need to update medians with the input lines, which means we need to compute the median for every line. Instead of sorting the whole list again every time, we can utilize the previous results to save the sorting time, which means every time when we process a new line, adding a new number, we can just insert this number into a appropriate place of the previously sorted list. 

So here I used 2 heaps to achieve that, largeHeap and smallHeap. largeHeap is used for the larger half part of the input number, and the smallHeap contains the smaller half part. In this way, we can directly get the median number from roots of the two heaps. If largeHeap contains one more number than the smallHeap, its root value would be the median one. If the two heaps have the same amount of numbers, then we can get the median value by computing the average of those two roots.

`find_political_donors.py` contains the main function of this solution.  
It mainly consists functions as following: 

*processData(), which reads the input file, extracts the data information we need, and calls functions for different situation.
*medianByZip(), medianByDate(), processing data according to the specific requirements of zipcode and transaction date.
*writeFile(), writing results to the relevant output file path.


# Packages required
Utilized python libraries: datetime, heapq, sys, os.path

# Methods to run
to run this program, simply execute the `./run.sh` in the root directory.

## Tips
I encountered the premission denied problem, when I first used ./run.sh to run the program in cloud9. If you also meet the same problem, 
just input `chmod +x run.sh` in the beginning, before inputing `./run.sh`

