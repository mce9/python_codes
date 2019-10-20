import pyperclip

def main():
	myMessage = 'Common sense is not so common'
	myKey = 8

	ciphertext = encryptMessage(myKey, myMessage)

	# print the encrypted string in ciphertext to the screen, with a pipe character to represent space
	print(ciphertext + '|')

	# Copy the encrypted string in cipher text to the clipboard
	pyperclip.copy(ciphertext)

def encryptMessage(key, message):

	# Each string in the ciphertext represent a column in the grid
	ciphertext = [''] * key

	# Loop through each column in the ciphertext
	for column in range(key):
		currentIndex = column

		# Keep looping until currentIndex goes past the message length
		while currentIndex < len(message):
			ciphertext[column] += message[currentIndex]

			# move currentIndex over
			currentIndex += key

	# convert the ciphertext list into a single string and return it
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()