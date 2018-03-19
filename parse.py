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
volume = 0.0
#open, close, high, low


weekArray = []
finalData = []
finalData.append( ["weeklyChange", "day1Rate", "day2Rate", "day3Rate", "day4Rate", "day5Rate", "day1Range", "day2Range", "day3Range", "day4Range", "day5Range", "weeklyVolume"] )

with open('AAPL.csv') as csvfile:
    myReader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for row in myReader:
    	if row[0] != 'ticker':
	    	if rowNum == 5:
	    		rowNum = 0
	    		#print("day5: ", volume)
	    		weeklyChange = float(weekArray[4][1]) - float(weekArray[0][0])
	    		rowWrite = []
	    		rowWrite.append(weeklyChange)
	    		for dayArray in weekArray: 
	    			#write theRange x5, write changeRate x5 to csv
	    			rowWrite.append(dayArray[5])
	    		for dayArray in weekArray:
	    			rowWrite.append(dayArray[6])
	    		#write volume
	    		rowWrite.append(volume)

	    		finalData.append(rowWrite)
	    		volume = 0.0
	    		weekArray = []
	    		#calculate and write to file


	    	#open, close, high, low, volume
	    	dayArray = []
	    	dayArray.append(row[9]) #open
	    	dayArray.append(row[12]) #close
	    	dayArray.append(row[10]) #high
	    	dayArray.append(row[11]) #low
	    	dayArray.append(row[13]) #volume

	    	changeRate = ( float(row[12]) - float(row[9]) ) / float(row[9])
	    	dayArray.append(changeRate)

	    	theRange = ( float(row[10]) - float(row[11]) ) / float(row[9])
	    	dayArray.append(theRange)

	    	weekArray.append(dayArray)

	    	volume += float(row[13])

	        print(dayArray)

	        rowNum += 1

myFile = open('output.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(finalData)
     
print("Writing complete")

print(weekArray)