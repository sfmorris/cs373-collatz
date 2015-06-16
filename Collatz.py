#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    max_cycle_length = 0
    cycle_length = 0
    if j < i :
        range_min = j
        range_max = i
    else :
        range_min = i
        range_max = j
    for k in range(range_min, range_max+1) :
        #print("\nevaluating k: {}".format(k))
        cycle_length = collatz_cycle_length(k)
        #print("cycle_length is {} of type {}".format(cycle_length, type(cycle_length)))
        #print("max_cycle_length is {} of type {}".format(max_cycle_length, type(max_cycle_length)))
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
    return max_cycle_length

# --------------------
# collatz_cycle_length
# --------------------

def collatz_cycle_length (n) :
    """
    n the individual natural number to find cycle length for
    return the cycle length for n, found iteratively
    """
    count = 1
    while (n > 1) :
        if n % 2 == 0 :
            n /= 2
            count += 1
        else :
            n = 3 * n + 1
            count += 1
    return count

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
