def arrayOfProducts(array):
    # Write your code here.
    pre=1
    post=1
    arr=[1]*len(array)
    for i in range(len(array)):
        arr[i] *= pre
        pre *= array[i]
        arr[len(array)-1-i] *= post
        post *= array[len(array)-1-i]
    return arr
