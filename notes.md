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
- 7L: D7
- 7R: E7
- 8L: D8
- 8R: A6

# Bar Measurements in mm
1. 53.72
2. 56.80
3. 60.65
4. 60.78
5. 63.78
6. 65.70
7. 67.48
8. 69.94
9. 73.22 
10. 78.02
11. 78.22
12. 82.52
13. 81.36
14. 85.38
15. 90.10
16. 97.72
