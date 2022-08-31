import imp
from util import *
from frequencies import *
from pysine import sine
import frequencies
import util
import time
#https://www.virtualsheetmusic.com/score/HL-42568.html
BPM = 140

OCTAVE_OFFSET = 1

def crazy_train():
    first_line()
    second_line()
    third_line()
    fourth_line()

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
    sine(calc_octative(E_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), 0.5)
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5 + OCTAVE_OFFSET), 1.5)
    time.sleep(calc_note_length(2, BPM))
    time.sleep(calc_note_length(1.25, BPM))
    

first_line()
second_line()
third_line()
fourth_line()
fifth_line()