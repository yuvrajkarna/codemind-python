a=input()
hour=(ord(a[0])-48)*10+ord(a[1])-48
min=(ord(a[3])-48)*10+ord(a[4])-48
if min%2==0:
    angle=30*hour*1.0-11*min/2
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))
else:
    angle=30*hour*1.0-5.5*min
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))  