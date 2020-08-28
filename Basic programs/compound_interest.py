def ci (p, r, t):
	a=p*(pow((1+r/100),t))
	#a=p*(1+r/100)**t #alternate formula
	print('simple interest is', a)
	return a
x=input('principle amount ')
y=input('rate ')
z=input('time ')

x=int(x)
y=float(y)
z=int(z)

ci(x,y,z)

