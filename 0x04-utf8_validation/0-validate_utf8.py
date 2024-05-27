#!/usr/bin/python3
"""
Main file for utf8_validation
"""


def xtract(num):
    byte_a = bin(num)[2:]
    bits = ''
    for i in byte_a:
        if i == '0':
            bits += i
            break
        bits += i
    return(bits)

def is_byte(num):
    return (num < 128)


def many_bytes(num):
    a_byte = bin(num)[2:]
    n_bytes = 0
    for i in a_byte:
        if i == '0':
            break
        n_bytes = +1
    return (n_bytes)


def right_shift(num):
    return ((num >> 1) - 1)


def validUTF8(data):
    i = 0
    t = True
    while (i < len(data)):
        if is_byte(data[i]):
            t = True
            i += 1
            continue
        else:
            n_bytes = many_bytes(data[i])
            try:
                con_num = data[i: (i + n_bytes + 1)]
            except IndexError as e:
                return (False)
            j = 0
            while (j < len(con_num) - 1):
                j_cur = int(xtract(con_num[j]), 2)
                j_next = int(xtract(con_num[j + 1]), 2)
                if right_shift(j_cur) != j_next:
                    return (False)
            i = i + n_bytes + 1
    return (t)