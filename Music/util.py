import math

# 2^(octave) * base_frequency
def calc_octative(base_frequency, octave):
    return 2 ** (octave) * base_frequency

def calc_note_length(num_beats, bpm):
    seconds_per_beat = 1/(bpm/60)
    return seconds_per_beat * num_beats
    #120 bpm = 2 beat per second --> 0.5 seconds per beat    
    #2 beat = 1 second



