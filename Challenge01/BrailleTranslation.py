def solution(s):
    enc = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    str = "The quick brown fox jumps over the lazy dog"
    ENC_LENGTH = 6
    enc_pos = 0
    encoding = ""
    map_dict = {" " : "000000", "cap" : "000001"}
    CAP = "cap"
    for c in str:
        if c.isupper():
            enc_pos +=ENC_LENGTH
            end = enc_pos + ENC_LENGTH
            map_dict[c.lower()] = enc[enc_pos : end]
            enc_pos+=ENC_LENGTH
        elif c.lower():
            end = enc_pos + ENC_LENGTH
            map_dict[c.lower()] = enc[enc_pos : end]
            enc_pos+=ENC_LENGTH
        else:
            enc_pos+=ENC_LENGTH
            continue
    
    for c in s:
        enc_format = "{}{}"
        prefix = "" if not c.isupper() else map_dict[CAP]
        char_code = map_dict[c.lower()] if c.isalpha() else map_dict[c]
        addition = enc_format.format(prefix, char_code) 
        print(c)
        print(f"Encoding Before:\n{encoding}")
        print(f"Addition for {c}:\n{addition}")
        encoding += addition
        print(f"Encoding after:\n{encoding}")
        print("*"*50)
    
    return encoding
        
print("code" + "\n" + solution("code"))
print("*"*50)
print("Braille" + "\n" + solution("Braille"))
print("*"*50)
print("The quick brown fox jumps over the lazy dog" + "\n" + solution("The quick brown fox jumps over the lazy dog"))
print("*"*50)