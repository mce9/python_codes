import math, pyperclip

def main():
	myMessage = 'Cenoonommstmme oo snnio. s s c'
	myKey = 8

	plaintext = decryptMessage(myKey, myMessage)

	print(plaintext + '|')

	pyperclip.copy(plaintext)

def decryptMessage(key, message):

	# the number of columns in the transposition grid
	numOfColumns = int(math.ceil(len(message) / float(key)))
	# the number of rows in our grid
	numOfRows = key
	# the number of shaded boxes in the last column of the grid
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

	# each string in plaintext represents a column in the grid
	plaintext = [''] * numOfColumns

	# the column and roy variables point to where in the grid the next character goes
	column = 0
	row = 0

	for symbol in message:
		plaintext[column] += symbol
		column += 1

		if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1

	return ''.join(plaintext)

if __name__ == '__main__':
	main()