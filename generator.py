#!/usr/bin/env python

import sys
import ascii_bin

method_pointers = {
    "ascii_bin": ascii_bin.generate
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
    try:
        generate_image(sys.argv[3], sys.argv[1], int(sys.argv[2]))
    except Exception as err:
        print("\033[91m./generator.py (method:str) (bytesize:int) (dimensions:str (WxH)) (input_file:str)\033[0m")
        raise err
