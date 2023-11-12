import secrets
import string

print("\nWelcome to a simple password generator App\n".upper())

#defining the variables
letters_string = string.ascii_letters
number_string = string.digits
special_char_string = string.punctuation

#concatenation of all strings
all_string = letters_string + number_string + special_char_string

#creating code to iterate to generate password

password_length = int(input("Specify the length (digits) of password you desire:__ "))

password = " "

for i in range(password_length):
  password += " ".join(secrets.choice(all_string))

print(password)




