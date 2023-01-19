compose = lambda f, g: lambda x: f( g(x) )

def inc(arg):
	arg+=1
	return arg

def pow(arg):
	return arg**2

h = compose(pow, inc)
print(h(6))