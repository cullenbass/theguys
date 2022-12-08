# MIDI format
## Header
- `<Header Chunk> = <chunk type><length><format><ntrks><division>`
	+ chunk type MUST be `4d54 6864` (MThd in ASCII) 
	+ length is 32 bit number 6 (`0000 0006`)
	+ format is 16 bit, should check for 0
	
## screw it library time
- mido
- 1000 micro -> milli 

# Hardware
## Data format
- `<time code> <pin mapping>`
	+ time code is 32 bit unsigned int number of microseconds since start of file
	+ pin mapping is 32 bit unsigned int mapping
		* upper 16 bit unused, lower 16 for bells
## Pseudocode
- throw entire structure into RAM; should fit easily
	1. checking if current timer > next event
	2. if so, change outputs to lower 16 bits
	3. go to 1


## Musical notes:
Starts at Santa, then back along string, then front of other string and back
- 1L: E8
- 1R: D#8
- 2L: G8
- 2R: C#8
- 3L: A8
- 3R: B7
- 4L: G#8
- 4R: A7
- 5L: F#8
- 5R: G7
- 6L: G#7
- 6R: F#7
- 7L: E7
- 7R: D7
- 8L: A6
- 8R: D8