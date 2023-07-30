import heapq
def optimalFreelancing(jobs):
    # Write your code here.
    jobs.sort(key=lambda x: x["deadline"])
    arr=[]
    print(jobs)
    for job in jobs:
        print(arr)
        if len(arr)<job["deadline"] and len(arr)<7:
            heapq.heappush(arr,job["payment"])
        else:
            if arr[0]<job["payment"]:
                heapq.heappushpop(arr,job["payment"])
    return sum(arr)