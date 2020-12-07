import math

def TimeToDistance(t , u = 0):
    t = float(t)
    s = (9.8 * (t**2))/2 + u * t
    return s


def DistanceToTime(s , u = 0):
    s = float(s)
    t = math.sqrt(s/5)
    return t


while True:
	print("""Options:
	A) Time to Distance
	B) Distance to Time
	""")
	ab = input()
	
	if ab.lower() == "a":
		time = input("Time: ")
		initVel = input("Intial velocity(0 by Default): ")
		print(TimeToDistance(int(time) , int(initVel)))