def underscorifySubstring(string, substring):
    # Write your code here.
    open=-1
    close=-1
    curr=0
    ans=""
    m=len(string)
    n=len(substring)
    while curr<m:
        sub = string[curr:curr+n]
        if sub == substring:
            if open<0:
                ans+='_'
                open=curr
            close=curr+n
        elif curr==close:
            ans+="_"
            open=-1
            close=-1

        ans += string[curr]
        curr+=1

    if close>0:
        ans+='_'
    return ans