from sys import argv

filename = argv[1]
print "You have entered the file :",filename

nameOfWeek = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
numOfDays = [0,0,0,0,0,0,0]
numTrips = [0,0,0,0,0,0,0]
numMiles = [0,0,0,0,0,0,0]
numSignUp = [0,0,0,0,0,0,0]
numDayPass = [0,0,0,0,0,0,0]
numWeekPass = [0,0,0,0,0,0,0]
day=0

with open(filename) as targetFile:
	for x in xrange(7): 				##Skip first 7 lines b/c sparse data
		next(targetFile)
	for line in targetFile:
		columns = line.split(",")
		if(day==7):
			day=0
		numOfDays[day]=numOfDays[day]+1
		numTrips[day]+=float(columns[1])
		numMiles[day]+=float(columns[3])
		numSignUp[day]+=float(columns[6])
		numDayPass[day]+=float(columns[7])
		numWeekPass[day]+=float(columns[8])
		day=day+1
		
	
print("Day of Week -- Total Trips -- Avg Trips -- Avg Miles -- Avg. Sign Up -- Avg. 24hr Pass -- Avg. 7day Pass")
for i in range(7):
	avgTrips = float(numTrips[i]/numOfDays[i])
	avgMiles = float(numMiles[i]/numOfDays[i])
	avgSignUp = float(numSignUp[i]/numOfDays[i])
	avgDayPass = float(numDayPass[i]/numOfDays[i])
	avgWeekPass = float(numWeekPass[i]/numOfDays[i])
	print nameOfWeek[i],",",numTrips[i],",",avgTrips,",",avgMiles,",",avgSignUp,",",avgDayPass,",",avgWeekPass
