# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:07:13 2020

@author: Benny
"""
x=True

while x==True:
    VOWELS= 'aeiou'
    consonants= 'bcdfghjklmnpqrstvwxyz'
        
    word= input('enter a word: ')
    word = word.lower()
    firstletter= word[0]
    if word in 'quit':
        x=False
        print('restart')
    elif firstletter in VOWELS:
        piglatin = word + 'way'
        print('This word in pig latin is:' , piglatin)
    elif firstletter in consonants:
        delete_fl= word[1:]
        print('this word in pig latin is:' , delete_fl + firstletter + 'ay')
        