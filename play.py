import mido

ports = mido.get_output_names()
print(ports)

outport = mido.open_output(ports[0])
inport = mido.open_input(ports[0])

satinDoll = 'midi/dougmckenzie/SatinDoll.mid'
mid = mido.MidiFile(satinDoll)

midTracks = mid.tracks

pianoMid = mid
pianoTracks = []

pianoMidTracks = pianoMid.tracks

for track in pianoMidTracks:
    if "piano" in track[0].name.lower():
        pianoTracks.append(track)

pianoMid.tracks = pianoTracks

for msg in pianoMid.play():
   outport.send(msg)