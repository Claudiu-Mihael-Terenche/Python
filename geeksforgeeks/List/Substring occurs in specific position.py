# Python3 code to test if substring occurs in specific position using string slicing
str1 = 'Gfg is best'
i, j = 7, 11
substr = 'best'

res = str1[i:j] == substr

print('Does string contain substring at required position?', res)
