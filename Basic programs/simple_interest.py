def si (p, t, r):
	a=(p*t*r)/100
	print('simple interest is', a)
	return a
x=int(input('principle amount '))
y=input('time ')
z=input('rate ')

y=int(y)
z=int(z)

si(x,y,z)

