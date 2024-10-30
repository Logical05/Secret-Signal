def secret_signal(signal) -> list:
    if not isinstance(signal, list):
        return "Error"
    
    result = []
    SYMBOLS = { '-': '0', '.': '1'}
    for i in signal:
        if not isinstance(i, str):
            continue
        
        binary = ""
        word = ""
        for j in i:
            if j not in SYMBOLS:
                continue

            binary += SYMBOLS[j]
            if len(binary) >= 8:
                word += chr(int(binary, 2))
                binary = ""

        tmp = word.strip()
        if tmp:
            result.append(tmp)
    return result

if __name__ == "__main__":
    print(secret_signal(["--.-f2543------.-h4------.-----", " ", "ADdsad"])) 