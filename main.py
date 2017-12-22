import dic

file_output = open('output.txt', 'w')

av_sym = ' '.join(dic.letters.keys())

print('You can use only this symbols: " {} ". Other symbols will not be displayed.'.format(av_sym))

word = input('Please input word: ')
print()
word = word.lower()

for string in range(dic.number_of_lines):
    for char in word:
        if char in dic.letters.keys():
            for char_for_print in dic.letters[char][string]:
                if char_for_print == '':
                    file_output.write(' ')
                else:
                    file_output.write(char.upper())
            file_output.write(' ')
        else:
            continue
    file_output.write('\n')