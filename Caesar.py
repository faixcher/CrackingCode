#Caesar Cipher
# 1) key , mode , SYMBOLS(for calculate position)


import pyperclip

# The string to be encrypted/decrypted
message = 'this is nothing'

# The encryption/decryption key:
key = 13 

#Whenther the program encrypts or decryts:
mode ='encrypt'
#mode ='decrypt'

#every posible symbol
SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?."

translated = ''

#code
for symbol in message:
	if symbol in SYMBOLS:
		symbolIndex = SYMBOLS.find(symbol) # find() is return index of charector
		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key 

		# condition for use this encrypt
		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex-len(SYMBOLS)
		elif translatedIndex < 0 :
			translatedIndex = translatedIndex+len(SYMBOLS)

		translated = translated + SYMBOLS[translatedIndex]
	else:
		translated = translated+symbol 

print(translated)
pyperclip.copy(translated)