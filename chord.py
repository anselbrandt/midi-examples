import time
import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()
midiout.open_port(0)
midiin.open_port(0)


with midiout:
    chord = [60,64,67,71,76]

    for note in chord:
        midiout.send_message([0x90, note, 80])

    time.sleep(1)

    for note in chord:
        midiout.send_message([0x80, note, 0])

    time.sleep(0.1)
 
del midiout