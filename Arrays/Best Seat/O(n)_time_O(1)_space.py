def bestSeat(seats):
    # Write your code here.
    maxCount = 0
    curr=0
    i=0
    seat = -1
    n=len(seats)
    while i<n:
        if seats[i] == 0:
            j=i+1
            while j<n and seats[j]==0:
                j+=1
            if j-i > curr:
                curr=j-i
                seat = (j+i-1)//2
            print(i,j)
            i=j
        else:
            i+=1
                
            
    return seat