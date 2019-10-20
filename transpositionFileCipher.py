# transposition cipher encrypt/decrypt file

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'

    # if the input file does not exist, the program terminates early
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # if the output file already exists, give the user a chance to exit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # measure how long the encryption/decryption takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # write out the translated message to the output file
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
    main()