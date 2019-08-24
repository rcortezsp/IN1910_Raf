from string import ascii_lowercase as ac
def count_chars(string):
    alphabet = list(ac)
    stri = string.lower()    
    let_count = {}
    for l in alphabet:
        count = 0
        for letter in stri:
            if letter == l:
                count += 1
                let_count[l] = count
    return let_count

example = "Hello, world!"
for char, count in count_chars(example).items():
    print(f'{char:3}{count:10}')
