from mido import MidiFile, tick2second
from collections import OrderedDict
import os

# 16 entry list with 0-15 being note value for each thing
PIN_MAPPING = [
	81,86,88,90,
	91,92,93,95,
	97,98,99,100,
	102,103,104,105,
]


files = list(filter(lambda x: '.mid' in x,  sorted(os.listdir('songs'))))


for fi, file in enumerate(files):
	mid = MidiFile('songs/{}'.format(file))
	ticks_per_beat = mid.ticks_per_beat
	tempo = -1
	
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
	print('file: {} ticks_per_beat: {} tempo: {}'.format(file, ticks_per_beat, tempo))
	msg_delta = 0
	for msg in mid.tracks[1]:
		msg_delta = msg_delta + msg.time
		if msg.type == 'note_on':
			timing_us = int((msg_delta*tempo)/ticks_per_beat)
			if timing_us in notes:
				notes[timing_us].append(msg.note)
			else:
				notes[timing_us] = [msg.note]

	final_bytes = bytes()

	for ts in notes:
		timestamp = ts.to_bytes(4, 'little')
		raw_map = 0
		for i in range(len(PIN_MAPPING)):
			if PIN_MAPPING[i] in notes[ts]:
				raw_map = raw_map + 2**i
		int_map = raw_map.to_bytes(2, 'little')
		final_bytes = final_bytes + timestamp + int_map 

	with open(f'{fi:02d}.dat', 'wb') as f:
		f.write(final_bytes)