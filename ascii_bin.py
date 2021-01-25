import numpy as np
import scipy.misc as smp
from PIL import Image


bit_on  = [255, 255, 255] # RGB value if bit is 1
bit_off = [0, 0, 0] # RGB value if bit is 0

def translate_bit_color(bit:str):
    if( bit == "1" ):
        return bit_on
    else:
        return bit_off

def data_to_matrix(data:list) -> np.array:
    newdat = [ [translate_bit_color(bit) for bit in byte] for byte in data ]
    col_array = np.array(newdat, dtype=np.uint8)

    return col_array

def generate(inp:list) -> None:
    col_array = data_to_matrix(inp)

    img = Image.fromarray(col_array, "RGB")
    img.save("ascii_bin-image.jpg")
