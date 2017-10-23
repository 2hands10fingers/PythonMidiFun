# Convert any block of text or string and convert it into midi information
# Created by 2hands10fingers

import math
import random
import rtmidi_python as rtmidi
import time

midi_out = rtmidi.MidiOut()
midi_out.open_port(1)

note_map = {
	'A': 4,
	'B': 5,
	'C': 7,
	'D': 9,
	'E': 11,
	'F': 12,
	'G': 14,
	'H': 16,
	'I': 17,
	'J': 19,
	'K': 21,
	'L': 23,
	'M': 24,
	'N': 26,
	'O': 28,
	'P': 29,
	'Q': 31,
	'R': 33,
	'S': 35,
	'T': 36,
	'U': 38,
	'V': 40,
	'W': 41,
	'X': 43,
	'Y': 45,
	'Z': 47,
	'a': 48,
	'b': 50,
	'c': 52,
	'd': 53,
	'e': 55,
	'f': 57,
	'g': 59,
	'h': 60,
	'i': 62,
	'j': 64,
	'k': 65,
	'l': 67,
	'm': 69,
	'n': 71,
	'o': 72,
	'p': 74,
	'q': 76,
	'r': 77,
	's': 79,
	't': 81,
	'u': 83,
	'v': 84,
	'w': 86,
	'x': 88,
	'y': 89,
	'z': 91,
	',': 93,
	'.': 95,
	'!': 96,
	'@': 36,
	'#': 40,
	'$': 101,
	'%': 103,
	'^': 105,
	'&': 107,
	'*': 108,
	'(': 110,
	')': 112,
	'-': 113,
	'_': 115,
	'+': 117,
	'/': 119,
	'{': 120,
	'}': 122,
	'[': 124,
	']': 125,
	'?': 127,
}


def replace_chars(character):
	return note_map.get(character, 0)

def translate_to_midi(string):
	output = []
	for character in string:
		output.append(replace_chars(character))
	return output

def on_data():
    
    thisString = "CONVERTS THIS STRING"
    print "MIDI CONVERSION COMMENCE!"
    for i in translate_to_midi(thisString):
    	
      midinote=[0x90]
      midioff=[0x80]
      
      #Adjusted parameters using time.sleep() and add NoteOff function with var midioff variable
    	midinote.insert(1, i)
    	midinote.insert(2, random.uniform(50, 100))
    	
      midi_out.send_message(midinote)

    	midioff.insert(1, i)
    	midioff.insert(2, random.uniform(50, 100))
    	midi_out.send_message(midioff)

    	time.sleep(0.12)

        print midinote

on_data()

