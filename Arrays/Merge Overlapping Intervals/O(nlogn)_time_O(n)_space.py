def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals,key = lambda x:x[0])
    mergedIntervals=[]
    currentInterval=sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currIntervalEnd>=nextIntervalStart:
            currentInterval[1]=max(nextIntervalEnd,currIntervalEnd)
        else:
            currentInterval=nextInterval
            mergedIntervals.append(currentInterval)
            
    return mergedIntervals
