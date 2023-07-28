def validIPAddresses(string):
    # Write your code here.
    ans = []
    n=len(string)
    for i in range(4):
        val=string[:i+1]
        if int(val)>255 or (str(int(val)) != val):
            continue
        ip=val+'.'
        for j in range(i+1,n-2):
            val=string[i+1:j+1]
            if int(val)>255 or (str(int(val)) != val):
                continue
            ip1=ip+val+'.'
            for k in range(j+1,n-1):
                val=string[j+1:k+1]
                if int(val)>255 or (str(int(val)) != val):
                    continue
                ip2=ip1+val+'.'
                for l in range(k+1,n):
                    val=string[k+1:l+1]
                    if int(val)>255 or (n-l-1)>0 or (str(int(val)) != val):
                        continue
                    print(n-l-1)
                    ip3=ip2+val
                    ans.append(ip3)
            
        
    return ans
