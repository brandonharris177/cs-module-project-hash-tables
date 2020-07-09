def word_count(s):
    tally = {}
    ignore_chars = {
        '"': None, 
        ':': None, 
        ';': None, 
        ',': None, 
        '.': None, 
        '-': None, 
        '+': None, 
        '=': None, 
        '/': None,
        '\\': None, 
        '|': None, 
        '[': None, 
        ']': None, 
        '{': None, 
        '}': None, 
        '(': None, 
        ')': None, 
        '*': None, 
        '^': None, 
        '&': None, 
        '': None 
    }

    for c in s:
        if c in ignore_chars:
            s = s.replace(c , "")

    final = s.lower().split()

    for c in final:   
        if c not in tally:
            tally[c] = 1
        else: 
            tally[c] += 1

    return tally 


    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))