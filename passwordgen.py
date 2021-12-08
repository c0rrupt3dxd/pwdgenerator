print('''
            .-""-.
           / .--. \\
          / /    \ \\
          | |    | |
          | |.-""-.|
         ///`.::::.`\\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\\\\ '::::' /
          `=':-..-'`''')
print(':-----|Password Generator|-----:')
print('================================')
print('>>This is a python script that generates random strong passwords.')
print('|===================================|')
print('|Created by: @xc3pt0w0 on instagram |')
print('|===================================|')

#main code

import random          
low = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sym = '[]{}#()*;._-'
all = low+up+num+sym
length = 10
pwd = "".join(random.sample(all,length))
print()
print('++++++++++++++++++++++++++++++++++++++')
print('|Your Randomly generated password is :',pwd)
print('++++++++++++++++++++++++++++++++++++++')