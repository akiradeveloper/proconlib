from proconlib.cumsum2 import *

def test_cumsum2():
	sum = Cumsum2(3,3)
	sum.set(0,0,2)
	sum.set(0,1,0)
	sum.set(0,2,0)
	sum.set(1,0,1)
	sum.set(1,1,0)
	sum.set(1,2,3)
	sum.set(2,0,0)
	sum.set(2,1,8)
	sum.set(2,2,5)
	sum.build()
	print(sum.dp)

	assert sum.query((0,0), (3,3)) == 19
	assert sum.query((1,1), (3,3)) == 16
	assert sum.query((1,1), (2,3)) == 3
	assert sum.query((1,1), (2,2)) == 0
	assert sum.query((1,0), (3,2)) == 9