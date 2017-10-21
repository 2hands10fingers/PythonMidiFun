import random
import time
import rtmidi_python as rtmidi

midi_out = rtmidi.MidiOut()
midi_out.open_port(1)

x = range(1, 127)

for i in x:
    midinote = [0x90]
    midinote.insert(1, i)
    midinote.insert(2, random.uniform(50, 100))
    midi_out.send_message(midinote)
    time.sleep(0.01)
    print midinote
