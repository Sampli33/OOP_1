from solution_8 import MorseMsg

a = '..-. ..- -. -. -.-- . -..- . .-. ... -.-. .. ... . ...'
a_decode = MorseMsg(a)
print(a_decode)
print(a_decode.eng_decode())
print(a_decode.get_vowels('eng'))
print(a_decode.get_consonants('eng'))
b = '--- ... --- -... . -. -. --- .--. --- ... .-.. . -.. -. .. . - .-. ..'
b_decode = MorseMsg(b)
print(b_decode)
print(b_decode.ru_decode())
print(b_decode.get_vowels('ru'))
print(b_decode.get_consonants('ru'))
