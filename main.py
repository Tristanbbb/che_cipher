import cipher
import decipher

if __name__ == '__main__':
	print("Type 1 to cipher, 2 to decipher.")
	
	choice = 0
	while(choice!="1" and choice !="2"):
		choice = raw_input("1 or 2?\n")

	text = ""

	if(choice=="1"):
		text = raw_input("Type the text to cipher:\n")
		key = raw_input("Type the 5 digit key:\n")
		print("Ciphered text:\n")
		print(cipher.cipher(text, key))
	else:
		text = raw_input("Type the text to decipher:\n")
		key = raw_input("Type the 5 digit key:\n")
		print("Deciphered text:\n")
		print(decipher.decipher(text, key))