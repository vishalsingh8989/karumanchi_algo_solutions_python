def get(a = 300 , r = 0.40, t=12, d = 0.03):
	sum = 0
	current = a
	for x in range(t):
		current = current + current*r
		sum  = sum +current
		print("{0} : {1}".format(current, sum))
		if r>0.01:
			r = r - d


get()
