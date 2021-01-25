#!/usr/bin/env python

import sys
from ascii_bin import main as ascii_bin

method_pointers = {
    "ascii_bin": ascii_bin
}


def get_input(file:str, bytesize:int = 8) -> list:
    f = open(file, "r")

    f_str = f.read()
    f_str = f_str.strip()
    f_str = f_str.replace(" ", "")

    return [ f_str[i:i+bytesize] for i in range(0, len(f_str), bytesize) ]

def generate_image(file:str, method:str = "ascii_bin", bytesize:int = 8) -> None:
    inp = get_input(file, bytesize)

    method_pointers[method](inp)


if __name__ == "__main__":
    generate_image(sys.argv[3], sys.argv[1], int(sys.argv[2]))
