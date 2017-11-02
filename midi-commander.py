import webbrowser
import rtmidi
import mido


mido.set_backend('mido.backends.rtmidi')
inport = mido.open_input('MPK mini')
outport = mido.open_output('IAC Driver Bus 1')
midiarray = []

with mido.open_output('MPK mini') as outport:
    for msg in inport:

        note = str(msg)
        sp = note.split('=', 5)
        noteindex = sp[2]
        midinote = noteindex[:2]

        if midinote == '64':
            outport.reset()
            webbrowser.open('http://www.reddit.com')

        elif midinote == '52':

            webbrowser.open('http://www.pitchfork.com')

        elif midinote == '63':

            webbrowser.open('http://www.netflix.com')

        else:

            print midinote

# To Do Items:
# # write in error handling for note on and note off
# # creation dictionary solution
