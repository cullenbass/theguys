import time
import os
import threading

# test file only
mapping = [
	1760, 2349.32, 2637.02, 2959.96,
	3135.96, 3322.44, 3520.00, 3951.07,
	4434.92, 4698.63, 4978.03, 5274.04,
	5919.91, 6271.93, 6644.88, 7040.00
]

mapping = [int(x) for x in mapping]

try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('play -n synth %s sin %s' % (duration/1000, frequency))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

def play(dat):
	for i, note in enumerate(dat):
		if note:
			return playsound(mapping[i], 100)


def decode(data):
	bits = []
	for x in data:
		print(x)
		for y in [
			x&2**0!=0,
			x&(2**1)!=0,
			x&(2**2)!=0,
			x&(2**3)!=0,
			x&(2**4)!=0,
			x&(2**5)!=0,
			x&(2**6)!=0,
			x&(2**7)!=0,]:
			bits.append(y)
	return bits

actions = []

for filename in sorted(filter(lambda x: '.dat' in x, os.listdir())):
	with open(filename, 'rb', buffering=0) as f:
		while ts_byte:= f.read(4):
			timestamp = int.from_bytes(ts_byte, 'little')
			pin_map = decode(f.read(2))
			actions.append((timestamp, pin_map))

	start = time.time_ns()/1000
	print('start ticking: {}'.format(start))
	curr = 0
	while len(actions) > 0:
		dat = actions.pop(0)
		while curr < dat[0]:
			curr = time.time_ns()/1000 - start
		print("Difference: {}".format(curr-dat[0]))
		play(dat[1])
	time.sleep(2)