def old_phone():
    words = input('type in your word')
    keypad = {2:['a','b','c'],\
    3:['d','e','f'],\
    4:['g','h','i'],\
    5:['j','k','l'],\
    6:['m','n','o'],\
    7:['p','q','r','s'],\
    8:['t','u','v'],\
    9:['w','x','y','z']}
    for word in list(words.lower()):
        print(word)
        value_list = list(keypad.keys())[list(keypad.values()).index(word)]
        place_value = [i for i,x in enumerate(keypad) if x == word]
        print(place_value)
        print(value_list)
old_phone()
