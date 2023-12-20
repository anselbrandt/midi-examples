# a hardware midi device must be connected
# or fluidsynth must be installed and running
import mido

ports = mido.get_output_names()
print(ports[1])

outport = mido.open_output(ports[1])

autumnLeaves = 'midi/dougmackenzie/AutumnLeaves.mid'
mid = mido.MidiFile(autumnLeaves)

pianoMid = mid
pianoTracks = []

pianoMidTracks = pianoMid.tracks

for track in pianoMidTracks:
    if "piano" in track[0].name.lower():
        pianoTracks.append(track)

for track in pianoTracks:
    print(track[0].name)

pianoMid.tracks = pianoTracks

for msg in pianoMid.play():
   outport.send(msg)