import mido

ports = mido.get_output_names()
print(ports[1])
print()

outport = mido.open_output(ports[1])
inport = mido.open_input(ports[1])

autumnLeaves = 'midi/dougmackenzie/AutumnLeaves.mid'
giantSteps = 'midi/book_1/GIANTS~1.MID'
mid = mido.MidiFile(giantSteps)

midTracks = mid.tracks

for track in midTracks:
    print(track[0].name)

print()

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