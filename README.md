CitiBike
========

##CitiBike Statistics##

###Intro###

This is a project designated to analyzing the existing CitiBike data in New York on a daily basis using unix commands. 

I have included my AWK commands in files and the current CitiBike Data via (http://citibikenyc.com/system-data). 

####How to get Data####

The link to the data in .csv format is located on the [Citi Bike System Data](http://citibikenyc.com/system-data) website and the link on the bottom right that says "Get Data" is the link for the data in .csv format. 

    

---
###Code - Python Script###
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

####Usage####

In the terminal:

    python CitiBikeParse.py data-CSXes.csv

###Code - awk Command###

    awk '
    BEGIN {
    FS=",";
    day=0;
    nameOfWeek[0]="Monday		";
    nameOfWeek[1]="Tuesday	";
    nameOfWeek[2]="Wednesday	";
    nameOfWeek[3]="Thursday	";
    nameOfWeek[4]="Friday		";
    nameOfWeek[5]="Saturday	";
    nameOfWeek[6]="Sunday		";
    }; 
  
    
    {if(NR>7){  # skip beginning days with limited data
    if(day=="7"){
    day=0;
    numOfDay[day]++;
    numTrips[day]+=$2;
    numMiles[day]+=$4;
    numSignUp[day]+=$7;
    numDayPass[day]+=$8;
    numWeekPass[day]+=$9;
    day++;
    }else{
    numOfDay[day]++;
    numTrips[day]+=$2;
    numMiles[day]+=$4;
    numSignUp[day]+=$7;
    numDayPass[day]+=$8;
    numWeekPass[day]+=$9;
    day++;
    }
    }};
    
    
    END{
    printf("Day of Week -- Total Trips -- Avg Trips -- Avg Miles -- Avg. Sign Up -- Avg. 24hr Pass -- Avg. 7day Pass\n");
    for(i=0;i<7;i++){
    avgTrips=numTrips[i]/numOfDay[i];
    avgMiles=numMiles[i]/numOfDay[i];
    avgSignUp=numSignUp[i]/numOfDay[i];
    avgDayPass=numDayPass[i]/numOfDay[i];
    avgWeekPass=numWeekPass[i]/numOfDay[i];
    printf(nameOfWeek[i]" -- "numTrips[i]" Trips -- "avgTrips" Trips per Day -- "avgMiles" Miles per Day-- "avgSignUp" Annual Signups --"avgDayPass" Day Passes --"avgWeekPass" Week Passes\n");
    }
    };'  data-CSXes.csv

###Results###

As of (09/26/2013) here are my findings broken down by day: 

      Monday -- 509879 Trips -- 29992.9 Trips per Day -- 69348.4 Miles per Day-- 481.824 Annual Signups --2870.53 Day Passes --187 Week Passes  
      Tuesday -- 445093 Trips -- 26181.9 Trips per Day -- 50588.4 Miles per Day-- 588.647 Annual Signups --1321.59 Day Passes --190.824 Week Passes  
      Wednesday -- 513837 Trips -- 30225.7 Trips per Day -- 55799.7 Miles per Day-- 565.176 Annual Signups --1130.94 Day Passes --227.235 Week Passes  
      Thursday -- 522459 Trips -- 32653.7 Trips per Day -- 61113.4 Miles per Day-- 566.188 Annual Signups --1302.12 Day Passes --211.688 Week Passes  
      Friday -- 506088 Trips -- 31630.5 Trips per Day -- 58891.1 Miles per Day-- 484.562 Annual Signups --1337.12 Day Passes --196.5 Week Passes  
      Saturday -- 503489 Trips -- 31468.1 Trips per Day -- 58056.6 Miles per Day-- 423.625 Annual Signups --1406.88 Day Passes --169.125 Week Passes  
      Sunday -- 513825 Trips -- 32114.1 Trips per Day -- 69745.6 Miles per Day-- 373.812 Annual Signups --2863.81 Day Passes --199.312 Week Passes  


---

![alt tag](https://raw.github.com/KFoxder/CitiBike/master/PassesChart.png)

![alt tag](https://raw.github.com/KFoxder/CitiBike/master/MilesTripChart.png)
