import math

equivDict = {
	"6": "A",
	"38": "B", 
	"32": "C", 
	"4": "D", 
	"8": "E", 
	"30": "F", 
	"36": "G", 
	"34": "H", 
	"39": "I", 
	"31": "J", 
	"78": "K", 
	"72": "L", 
	"70": "M", 
	"76": "N", 
	"9": "O", 
	"79": "P", 
	"71": "Q", 
	"58": "R", 
	"2": "S", 
	"0": "T", 
	"52": "U", 
	"50": "V", 
	"56": "W", 
	"54": "X", 
	"1": "Y", 
	"59": "Z", 
}


def decipher(encryptedText, key):

	plainText = encodedText = ""

	for index, digit  in enumerate(encryptedText):
		encodedText += str(int(int(digit)-int(key[index%5]))%10)

	# Encoding from letter to number equivalent
	index = 0
	while index < len(encodedText):
		# The toDecode variable is either one or two digits
		toDecode = encodedText[index]
		if(toDecode=='3' or toDecode=='7' or toDecode=='5'):
			toDecode += encodedText[index+1]
			index +=1

		print("To decode: {}".format(toDecode))
		plainText += equivDict[toDecode]

		index += 1
	
	return plainText





