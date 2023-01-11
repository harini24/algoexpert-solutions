def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    minwaitingTime=0
    for ind, duration in enumerate(queries):
        queriesLeft = len(queries) - ind - 1
        minwaitingTime += duration*queriesLeft
    return minwaitingTime

def minimumWaitingTime1(queries):
    # Write your code here.
    queries.sort()
    minWaitingTime=0
    prevTimes=0
    for query in queries:
        minWaitingTime+=prevTimes
        prevTimes+=query
    return minWaitingTime