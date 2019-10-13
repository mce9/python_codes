import pyperclip

# Whether the program encrypts or decrypts
mode = input('Enter "encrypt" or "decrypt": ')

# string to be encrypted/decrypted
message = input('Enter the message: ')

# The encryption/decryption key
key = int(input('Enter the key to use: '))

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message
translated = ''

for symbol in message:
	# Only symbols in the SYMBOLS string can be encrypted/decrypted
	if symbol in SYMBOLS:
		symbolIndex = SYMBOLS.find(symbol)

		# Perform encryption/decryption
		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key

		# Handle wraparound, if needed
		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex - len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex = translatedIndex + len(SYMBOLS)

		translated = translated + SYMBOLS[translatedIndex]
	else:
		# Append the symbol without encrypting/decrypting
		translated = translated + symbol

print(translated)
pyperclip.copy(translated)