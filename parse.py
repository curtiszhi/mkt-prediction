import csv 
import sys
 
# f = open('AAPL.csv', newline='') 
# reader = csv.reader(f)
# rowNum = 1
# volume = 0 
# #open, close, high, low
# day1 = []
# day2 = []
# day3 = []
# day4 = []
# day5 = []
# for row in reader
# 	print(row)
 
# f.close()

rowNum = 0
volume = 0
#open, close, high, low
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []

weekArray = []


with open('AAPL.csv') as csvfile:
    myReader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in myReader:
    	if row[0] != 'ticker':
	    	if rowNum == 5:
	    		rowNum = 0
	    		print("day5: ", volume)
	    		volume = 0
	    		#calculate and write to file
	    	#open, close, high, low, volume
	    	dayArray = []
	    	dayArray.append(row[9]) #open
	    	dayArray.append(row[12]) #close
	    	dayArray.append(row[10]) #high
	    	dayArray.append(row[11]) #low
	    	dayArray.append(row[13]) #volume
	    	weekArray.append(dayArray)
	    	volume += int(row[13])
	        print(row[12])
	        rowNum += 1

