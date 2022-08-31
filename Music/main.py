import imp
from util import *
from frequencies import *
from pysine import sine
import frequencies
import util
import time

BPM = 130

def crazy_train():

    # #1st line
    for i in range(2):
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(3, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(3, BPM))
        sine(calc_octative(D_FREQUENCY, 5), calc_note_length(0.5, BPM))
        sine(calc_octative(D_FREQUENCY, 5), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        time.sleep(calc_note_length(1, BPM))


    #second line
    for i in range(3):
        #1st bar    
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(D_FREQUENCY, 5), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
        sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))

        sine(calc_octative(B_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))

        sine(calc_octative(B_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
        sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(D_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(C_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(B_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))

    sine(calc_octative(D_FREQUENCY, 5), calc_note_length(2, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))

    third_line()


def third_line():
    #3rd line
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))

    sine(calc_octative(A_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))

    sine(calc_octative(F_SHARP_BASE_FREQUENCY, 5), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.25, BPM))
    sine(calc_octative(E_BASE_FREQUENCY, 5), calc_note_length(1.5, BPM))

    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(G_SHARP_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))
    sine(calc_octative(A_BASE_FREQUENCY, 4), calc_note_length(0.5, BPM))


third_line()





