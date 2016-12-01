#Zeno's paradox
#Where i in range 1 to infinity, the summation of (1/2^i)=1

import time
exp=-1.0000000000000
base=2**exp
print 2**exp
while 1:
	if exp==-1:
		pass
	else:
		curr=2**exp
		new=base+curr
		#Adjust this decimal for precision
		print '%.15f' % new
		base=new
	exp-=1
	time.sleep(.25)
