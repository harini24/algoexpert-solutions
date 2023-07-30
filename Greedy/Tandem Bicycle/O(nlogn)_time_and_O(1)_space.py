def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse= fastest)
    print(redShirtSpeeds,blueShirtSpeeds)
    sum = 0
    for ind in range(len(blueShirtSpeeds)):
        sum += max(blueShirtSpeeds[ind],redShirtSpeeds[ind] )
      
    return sum
