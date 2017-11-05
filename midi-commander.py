import os
import webbrowser
import rtmidi
import mido
from playsound import playsound

# SETTINGS
midicontroller = 'MPK mini'
midioutput = 'IAC Driver Bus 1'

#CONFIGURATION
mido.set_backend('mido.backends.rtmidi')
inport = mido.open_input(midicontroller)
outport = mido.open_output(midioutput)

#FUNCTIONS
## WEBSITE COMMANDS
def comsite(site):
    webbrowser.open('http://' + site + ".com")

def orgsite(site):
    webbrowser.open('http://' + site + ".org")
 
## MORE TO COME

#WHERE THE MAGIC HAPPENS    
with mido.open_output('MPK mini') as outport:
    for msg in inport:
        
        if msg.type == 'note_off':
            continue

        midi_note = msg.note

        if midi_note == 64:
            outport.reset()
            comsite('reddit')
        elif midi_note == 52:
            outport.reset()
            comsite('pitchfork')
        elif midi_note == 63:
            outport.reset()
            comsite('netflix')
         elif midi_note == 65:
            orgsite(wikipedia)
        else:
            print(midi_note)


# To Do Items:
# # create dictionary solution
