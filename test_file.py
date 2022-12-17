import time
import winsound

# in microseconds
SOLENOID_DELAY = 10000

def decode(data):
	bits = []
	for x in data:
		for y in [
			x&2**0!=0,
			x&(2**1)!=0,
			x&(2**2)!=0,
			x&(2**3)!=0,
			x&(2**4)!=0,
			x&(2**5)!=0,
			x&(2**6)!=0,
			x&(2**7)!=0,
			x&(2**8)!=0,
			x&(2**9)!=0,
			x&(2**10)!=0,
			x&(2**11)!=0,
			x&(2**12)!=0,
			x&(2**13)!=0,
			x&(2**14)!=0,
			x&(2**15)!=0 ]:
			bits.append(y)
	return bits

actions = []

with open('songs.dat', 'rb', buffering=0) as f:
	while ts_byte:= f.read(4):
		timestamp = int.from_bytes(ts_byte, 'little')
		pin_map = decode(f.read(2))
		actions.append((timestamp, pin_map))
		# actions.append((timestamp + SOLENOID_DELAY, [False]*16))

time.sleep(2)

start = time.time_ns()/1000
print('start ticking: {}'.format(start))
curr = 0
while len(actions) > 0:
	dat = actions.pop(0)
	while curr < dat[0]:
		curr = time.time_ns()/1000 - start
	print("Difference: {}".format(curr-dat[0]))
	winsound.Beep(440,10)
