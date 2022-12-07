from mido import MidiFile, tick2second
from collections import OrderedDict
import os

mid = MidiFile('demo2.mid')

ticks_per_beat = mid.ticks_per_beat

tempo = -1

# 16 entry list with 0-15 being note value for each thing
PIN_MAPPING = [60,62,64,65,
	0,0,0,0,
	0,0,0,0,
	0,0,0,0,
]

# grab numbers for timestamp determination
for i, track in enumerate(mid.tracks):
	for msg in track:
		if msg.type == 'set_tempo':
			tempo = msg.tempo
		break
	if tempo != -1:
		break

#initial unprocessed work
notes = OrderedDict()

# tempo is microseconds per beat
print('ticks_per_beat: {} tempo: {}'.format(ticks_per_beat, tempo))
msg_delta = 0
for msg in mid.tracks[1]:
	msg_delta = msg_delta + msg.time
	timing_us = int((msg_delta)/ticks_per_beat)*tempo
	if msg.type == 'note_on':
		if timing_us in notes:
			notes[timing_us] = notes[timing_us].append(msg.note)
		else:
			notes[timing_us] = [msg.note]

print(notes)

final_bytes = bytes()

for ts in notes:
	timestamp = ts.to_bytes(4, 'little')
	raw_map = 0
	for i in range(len(PIN_MAPPING)):
		if PIN_MAPPING[i] in notes[ts]:
			raw_map = raw_map + 2**i
	int_map = raw_map.to_bytes(2, 'little')
	final_bytes = final_bytes + timestamp + int_map 
	
with open('songs.dat', 'wb') as f:
	f.write(final_bytes)