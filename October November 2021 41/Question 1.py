def Unknown(X, Y):
	if X < Y:
		print(str(X + Y))
		return Unknown(X + 1, Y) * 2
	elif X == Y:
		return 1
	else:
		print(str(X + Y))
		return int(Unknown(X - 1, Y) / 2)

print("10 and 15")
print(str(Unknown(10, 15)))
print("10 and 10")
print(str(Unknown(10, 10)))
print("15 and 10")
print(str(Unknown(15, 10)))

'''
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
'''

def IterativeUnknown(X,Y):
	Total = 1
	while X != Y:
		print(str(X + Y))
		if X < Y:
			X = X + 1
			Total = Total * 2
		else:
				X = X - 1
				Total = int(Total / 2)
	return Total

print("10 and 15")
print(str(IterativeUnknown(10, 15)))
print("10 and 10")
print(str(IterativeUnknown(10, 10)))
print("15 and 10")
print(str(IterativeUnknown(15, 10)))

'''
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
10 and 15
25
26
27
28
29
32
10 and 10
1
15 and 10
25
24
23
22
21
0
'''