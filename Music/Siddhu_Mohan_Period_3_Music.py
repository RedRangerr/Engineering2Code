from pysine import sine
import time

#Siddhu Mohan A-3, Crazy Train by Ozzy Osbourne

C_BASE_FREQUENCY = 16.35
C_SHARP_BASE_FREQUENCY = 17.32
D_FREQUENCY = 18.35
D_SHARP_BASE_FREQUENCY = 19.45
E_BASE_FREQUENCY = 20.6
F_BASE_FREQUENCY = 21.83
F_SHARP_BASE_FREQUENCY = 23.12
G_BASE_FREQUENCY = 24.5
G_SHARP_BASE_FREQUENCY = 25.96
A_BASE_FREQUENCY = 27.5
A_SHARP_BASE_FREQUENCY = 29.14
B_BASE_FREQUENCY = 30.87

# 2^(octave) * base_frequency
def calc_octative(base_frequency, octave):
    return 2 ** (octave) * base_frequency

def calc_note_length(num_beats, bpm):
    seconds_per_beat = 1/(bpm/60)
    return seconds_per_beat * num_beats
    #120 bpm = 2 beat per second --> 0.5 seconds per beat    
    #2 beat = 1 second


BPM = 140

OCTAVE_OFFSET = 1

def crazy_train():
    first_line()
    second_line()
    third_line()
    fourth_line()
    fifth_line()
    sixth_line()
    seventh_line()
    eigth_line()
    line_9_to_13()
    line_end()
    first_line()
    second_line()
    sine(calc_octative(D_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    time.sleep(calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

def first_line():
    for i in range(2):
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(3, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(3, BPM))
        sine(calc_octative(D_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(D_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))

def second_line():
    for i in range(3):
        #1st bar    
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(C_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(D_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(C_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

        sine(calc_octative(B_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(G_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

        sine(calc_octative(B_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(G_SHARP_BASE_FREQUENCY, 3 + + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

    sine(calc_octative(D_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(2, BPM))

def third_line():
    #3rd line
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))

    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))

    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))

    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

def fourth_line():
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))

    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3+ OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))

    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(0.25, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))

    sine(calc_octative(A_BASE_FREQUENCY, 3 + OCTAVE_OFFSET), calc_note_length(1, BPM))    

def fifth_line():
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    time.sleep(calc_note_length(2, BPM))
    time.sleep(calc_note_length(1.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    time.sleep(calc_note_length(4, BPM))
    
def sixth_line():
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    time.sleep(calc_note_length(1.5, BPM))
    #2nd part
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    time.sleep(calc_note_length(4, BPM))
    
def seventh_line():
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    time.sleep(calc_note_length(2, BPM))
    time.sleep(calc_note_length(1.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    time.sleep(calc_note_length(5.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))

def eigth_line():
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    time.sleep(calc_note_length(1.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    time.sleep(calc_note_length(4, BPM))
    
def line_9_to_13():
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    time.sleep(calc_note_length(1, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2.5, BPM))
    time.sleep(calc_note_length(1.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    time.sleep(calc_note_length(5.5, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    time.sleep(calc_note_length(6, BPM))
    
    
def line_end():
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(D_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    time.sleep(calc_note_length(6, BPM))
    
    for i in range(3):
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(1.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), calc_note_length(2, BPM))
    
crazy_train()