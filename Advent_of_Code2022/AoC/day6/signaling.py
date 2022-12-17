with open("input.txt", "rb") as f:
    for line in f:
        line = line.decode().strip()
        chars = [x for x in line]
        previous_chars = chars[:3]
        del chars[:3]
        for count, char in enumerate(line):
            previous_chars.append(char)
            char_set = {x for x in previous_chars}
            print(previous_chars)
            print(count)
            if len(char_set) == len(previous_chars):
                print(count+4)
                break
            del previous_chars[0]
