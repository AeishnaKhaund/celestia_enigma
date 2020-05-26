import sys
import random

class PlugBoard(object):
    def __init__(self, num_pairs=10):
        self.num_pairs = num_pairs
        #A dictionary in which each letter is each letter is paired with its corresponding pair
        self.pairs_dict = {}

    #computer sets the pairs randomly
    def set_pairs_random(self):
        letter_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #letters are addressed by numbers so A is 0, B is 1 and Z is 25 etc
        sequence = [i for i in range(26)]
        random.shuffle(sequence)
        #letters corresponding to the first 20 numbers are assumed to be pairs
        #letters corresponding to the last 6 numbers are not paired
        #consecutive elements upto the 20th elements are considered as pairs. So elements 1,2 form a pair, elements 3,4 form another and so on
        i=0
        while i<(2*self.num_pairs -1):
            self.pairs_dict[letter_string[sequence[i]]] = letter_string[sequence[i+1]]
            self.pairs_dict[letter_string[sequence[i+1]]] = letter_string[sequence[i]]
            i = i + 2
        while i<26:
            self.pairs_dict[letter_string[sequence[i]]] = letter_string[sequence[i]]
            i = i + 1

    #function that lets you set the pairs manually
    def set_pairs_man(self):
        letter_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(self.num_pairs):
            pair = input()
            self.pairs_dict[pair[0]] = pair[1]
            self.pairs_dict[pair[1]] = pair[0]
        for i in letter_string:
            flag = 0
            for j in self.pairs_dict:
                if i==j:
                    flag = 1
            if flag==0:
                self.pairs_dict[i] = i

    def change_letter(self, letter_in):
        letter_out = self.pairs_dict[letter_in]
        return letter_out

#testing
p = PlugBoard()
p.set_pairs_random()
print(p.pairs_dict)
print('')
letter_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_letter_string = ''
for i in letter_string:
    new_letter_string = new_letter_string + p.change_letter(i)
print('plaintext: %s'%letter_string)
print('ciphertext: %s'%new_letter_string)
print(sys.version)
