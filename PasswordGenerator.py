from random import choice

char_sets = [ 							   # char_sets is a set that holds different char sets
			'abcdefghijklmnopqrstuvwxyz',  # char set for lowercase
			'0123456789',				   # char set for nums
			'ABCDEFGHIJKLMNOPQRSTUVWXYZ',  # char set for uppercase
			'^!\\$%&/()=?{[]}+~#-_.:,;<>|' # char set for special chars
			]


def main():

	length = get_input() 				 # get desired password length from user
	new_pass = generate_password(length) # generate password
	print("Password is: ", new_pass)					 # print password


def get_input(): # function to get input from user
	while(1):
		pass_len = input("please enter desired password length >= 8: ")
		pass_len = int(pass_len) # typecast input from str to int

		if pass_len >= 8:		 # check for length requirement
			return pass_len		 # if input is valid, return
		else:					 # input is invalid
			print("invalid input, a strong password must be at least 8 characters long.")


def generate_password(length): # function to generate password
	password = []												# initialize password
	charset = choice(char_sets) 								# select one set from char_sets i.e. lowercase, uppercase, nums, or special

	for x in range(length):										# loop until password is equl to desired length
		password.append(choice(charset)) 						# append a random char from the chosen charset
		charset = choice(list(set(char_sets) - set([charset]))) # take char out of set
	return "".join(password) 									# return newly generated password


main() # call to main()
