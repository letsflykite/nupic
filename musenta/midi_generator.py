#!/usr/bin/env python

def list_to_strln(input_list):
    output_str = str(input_list)
    output_str = output_str[1:(len(output_str) - 1)] + '\n'
    output_str = output_str.replace("'", "")
    return output_str

#   Assume the shortest note is an eighth note
atom_note = 8

#   Read in melody as a sequence of atom notes
sequence = [int(float(line)) for line in open('multistep_output_10.txt')]

clocks_per_QN = 120
track = 4
channel = 2
velocity = 100

write_filename = 'multistep_generated_10.csv'
f = open(write_filename, 'w')

top_lines = """0, 0, Header, 1, 10, 120
1, 0, Start_track
1, 0, Time_signature, 2, 2, 24, 8
1, 0, Key_signature, 1, "major"
1, 0, Tempo, 500000
1, 7200, End_track
4, 0, Start_track
4, 0, MIDI_port, 0
"""

f.write(top_lines)

current_pitch = sequence[0]
duration = 0
start_time = 0
end_track_time = 0
for (index, pitch) in enumerate(sequence):
    if pitch == current_pitch:
        duration = duration + clocks_per_QN*4/atom_note
    if (pitch != current_pitch) or index == (len(sequence) - 1):
        line1 = [track, start_time, 'Note_on_c', channel, current_pitch, velocity]
        f.write(list_to_strln(line1))

        line2 = [track, start_time + duration, 'Note_on_c', channel, current_pitch, 0]
        f.write(list_to_strln(line2))

        start_time = start_time + duration
        end_track_time = start_time
        duration = clocks_per_QN*4/atom_note
        current_pitch = pitch

end_track_line = [track, end_track_time, 'End_track']
f.write(list_to_strln(end_track_line))

f.write('0, 0, End_of_file\n')
f.close()

