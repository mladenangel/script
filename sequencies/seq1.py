#!/usr/bin/env python3

seq = input('Sentence:')

screen_width = 80
text_width = len(seq)
box_width = text_width + 6
left_margin = (screen_width-box_width)//2

print()
print('' * left_margin + '+' + '-' *(box_width-2) + '+')
print(""*left_margin+"| "+ ""  *text_width+" |")


