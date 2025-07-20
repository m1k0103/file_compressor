
# Encodes text into utf-8, converts into hex, then into binary representation, then uses run-length encoding
def compress(raw_text: str):
    # Converts text to binary
    hex = raw_text.encode("utf-8").hex()
    binary_str = "".join(format(ord(char), "b") for char in hex)

    # Run length encoding
    #for i in range(len(binary)):
    #    first =
    start_ptr = 0
    end_ptr = 0
    compressed_str = 0
    while end_ptr != (len(binary_str) - 1):
        if binary_str[end_ptr] == binary_str[start_ptr]: # if the values at the pointers are the same, increment end pointer
            end_ptr += 1
        elif binary_str[end_ptr] != binary_str[start_ptr]: # if the values are different, find length between pointers and what is between them.
            len_between_ptr = len(binary_str[]) #carry on from here

        pass



def decompress():
    pass

compress("HELLO WORLD")