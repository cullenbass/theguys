import time
import gc
import micropython
from machine import Pin

led = Pin(25, Pin.OUT)

# in microseconds
SOLENOID_DELAY = 100000

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
			x&(2**7)!=0 ]:
			bits.append(y)
	return bits

actions = []

with open('songs.dat', 'rb', buffering=0) as f:
	while ts_byte:= f.read(4):
		timestamp = int.from_bytes(ts_byte, 'little')
		pin_map = decode(f.read(2))
		actions.append((timestamp, pin_map))
		actions.append((timestamp + SOLENOID_DELAY, [False]*16))

start = time.ticks_us()
print('start ticking: {}'.format(start))
curr = 0
micropython.mem_info()
print('-----------------------------')
print('Initial free: {} allocated: {}'.format(gc.mem_free(), gc.mem_alloc()))
while len(actions) > 0:
	dat = actions.pop(0)
	while curr < dat[0]:
		curr = time.ticks_us() - start
	print("Difference: {}".format(curr-dat[0]))
	led.toggle()
