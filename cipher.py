import math

equivDict = {
	"A": "6",
	"B": "38",
	"C": "32",
	"D": "4",
	"E": "8",
	"F": "30",
	"G": "36",
	"H": "34",
	"I": "39",
	"J": "31",
	"K": "78",
	"L": "72",
	"M": "70",
	"N": "76",
	"O": "9",
	"P": "79",
	"Q": "71",
	"R": "58",
	"S": "2",
	"T": "0",
	"U": "52",
	"V": "50",
	"W": "56",
	"X": "54",
	"Y": "1",
	"Z": "59",
}

def cipher(plainText, key):

	encodedText = encryptedText = ""

	# Encoding from letter to number equivalent
	for letter in plainText:
		encodedText += equivDict[letter.upper()]

	
	# Now we need to apply the addition modulo 10 of the 5 digit key on blocks of 5 digits from our encoded text
	for index, digit  in enumerate(encodedText):
		encryptedText += str(int(int(digit)+int(key[index%5]))%10)
	
	return encryptedText


