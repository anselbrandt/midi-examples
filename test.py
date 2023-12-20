import time
import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()
midiout_ports = midiout.get_ports()
midiin_ports = midiin.get_ports()

print(midiout_ports)
print(midiin_ports)

midiout.open_port(1)
midiin.open_port(1)

with midiout:
    note_on = [0x90, 60, 60]
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    midiout.send_message(note_off)
    time.sleep(0.1)

del midiout