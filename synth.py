import time
import fluidsynth

fs = fluidsynth.Synth(samplerate=44100.0)
fs.start()

soundfont = "/Users/ansel/Library/Audio/Sounds/Banks/wurlitzer.sf2"

sfid = fs.sfload(soundfont)
fs.program_select(0, sfid, 0, 0)

fs.noteon(0, 60, 90)
fs.noteon(0, 67, 90)
fs.noteon(0, 76, 90)

time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()