import math

def TimeToDistance(t , u = 0):
    t = float(t)
    s = (9.8 * (t**2))/2 + u * t
    return s


def DistanceToTime(s , u = 0):
    s = float(s)
    t = math.sqrt(s/5)
    return t



print(TimeToDistance(10 , 5))
