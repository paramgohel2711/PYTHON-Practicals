import math
height = float(input("Enter the height to be reached: "))
angle = float(input("Enter the angle of the ladder with the ground (in degrees): "))
length = height / math.cos(math.radians(angle))
print("Length of the ladder required:", round(length, 2))
