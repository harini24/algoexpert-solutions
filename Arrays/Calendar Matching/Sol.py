# (c1+c2) time and space
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    updatedCalender1 = updatedCalender(calendar1,dailyBounds1)
    updatedCalender2 = updatedCalender(calendar2,dailyBounds2)

    mergedcalendar = mergeCalendars(updatedCalender1,updatedCalender2)

    nonOverlappingCalendar = nonOverlappingIntervals(mergedcalendar)

    return matchingCalendarAvailabilities(nonOverlappingCalendar,meetingDuration)

def updatedCalender(calender,bound):
    updatedCal = calender[:]
    updatedCal.insert(0,["0:00",bound[0]])
    updatedCal.append([bound[1],"23:59"])
    return list(map(lambda x: [convertTimeToMinutes(x[0]),convertTimeToMinutes(x[1])] , updatedCal))

def convertTimeToMinutes(time):
    hours,mins = list(map(int,time.split(":")))
    return hours * 60 + mins

def convertMinutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    minsString = "0"+str(mins) if mins <10 else str(mins)
    return str(hours)+":"+minsString
    

def mergeCalendars(calendar1,calendar2):
    mergedCalendar = []
    n = len(calendar1)
    m = len(calendar2)
    i=0
    j=0
    while i<n and j<m:
        if calendar1[i] < calendar2[j]:
            mergedCalendar.append(calendar1[i])
            i+=1
        else:
            mergedCalendar.append(calendar2[j])
            j+=1
    while i<n:
        mergedCalendar.append(calendar1[i])
        i+=1
    while j<m:
        mergedCalendar.append(calendar2[j])
        j+=1
    return mergedCalendar

def nonOverlappingIntervals(intervals):
    nonOverlappingValues=[intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] < nonOverlappingValues[-1][1]:
            nonOverlappingValues[-1][1] = max(nonOverlappingValues[-1][1], intervals[i][1])
        else:
            nonOverlappingValues.append(intervals[i])
    return nonOverlappingValues

def matchingCalendarAvailabilities(calendar,duration):
    matchingAvailablities = []
    for i in range(1,len(calendar)):
        if calendar[i][0]  - calendar[i-1][1] >= duration:
            matchingAvailablities.append([convertMinutesToTime(calendar[i-1][1]),convertMinutesToTime(calendar[i][0])])
    return matchingAvailablities
    