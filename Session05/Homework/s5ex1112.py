def is_inside(l,m):
    if m[0] <= l[0] <= (m[0]+m[2]) and m[1] <= l[1] <= (m[1] + m[3]):
        return True
    else:
        return False

print(is_inside([200, 120], [140, 60, 100, 200]))
print(is_inside([100, 120], [140, 60, 	]))


if is_inside([500,260],[200,140,350,300]) == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")