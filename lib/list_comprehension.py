#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
print(return_evens([1, 2, 3, 4, 5, 6]))
  

def make_exclamation(sentences_list):
        return [sentence + "!" for sentence in sentences_list]

print(make_exclamation(['Hello', 'I love python', 'Am so confused']))