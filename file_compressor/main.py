
# Encodes text into utf-8, converts into hex, then into binary representation, then uses run-length encoding
def compress(raw_text: str):
    # Converts text to binary
    hexa_str = raw_text.encode("ascii").hex()
    binary_str = "".join(format(ord(char), "b") for char in hexa_str)
    print(binary_str, "\n", hexa_str)
    

    # Run length encoding
    #for i in range(len(binary)):
    #    first =
    start_ptr = 0
    end_ptr = 0
    compressed_str = ""
    while end_ptr != (len(binary_str) - 1):
        if binary_str[end_ptr] == binary_str[start_ptr]: # if the values at the pointers are the same, increment end pointer
            end_ptr += 1
        elif binary_str[end_ptr] != binary_str[start_ptr]: # if the values are different, find length between pointers and what is between them.
            len_between_ptr = len(binary_str[start_ptr:end_ptr]) #carry on from here
            compressed_str += f"{'0'*(2-len(str(len_between_ptr)))}{str(len_between_ptr)}{binary_str[start_ptr]}" # amount(2) | char(1) = total 3
            start_ptr = end_ptr
    return compressed_str


# Reconstructs the runlength encoded
def decompress(compressed_string):
    split = [compressed_string[i:i+3] for i in range(0, len(compressed_string), 3)]
    
    binary = ""
    for i in split:
        binary += f"{str(i[2]) * int(i[:2])}"
    
    #hex_str = hex(int(binary, 2))
    hex_str = "".join([hex(binary[i:i+2]) for i in range(0,len(binary), 5)])

    pass

# There is an issue somewhere in this code. The compress function has an issue where when doing ord() on a char(str), that is then converted to hex,
# which then causes issues because in decompress function the hex is somehow different??? Not sure whats going on here.

a = compress("HELLO WORLD")
decompress(a)