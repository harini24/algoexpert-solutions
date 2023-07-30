# O(nlogn) time and O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    redOnTop = redShirtHeights[0] > blueShirtHeights[0]
    for ind,redStud in enumerate(redShirtHeights):
        blueStud = blueShirtHeights[ind]
        if (redOnTop and redStud<=blueStud): return False
        if (not redOnTop and redStud>=blueStud): return False
    return True
