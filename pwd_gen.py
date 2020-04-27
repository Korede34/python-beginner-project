import random
import string

print('\t\t"""PASSWORD GENERATOR"""\n')
print()

print("The password length must be between 6-16 characters")
flag = True
while flag:
	try:
		pw_length = input("[+] Enter desired password length: ")
		if pw_length.isdigit() and int(pw_length) in range(6, 16 + 1):
			pw_lenght = int(pw_length)
			flag = False
		elif int(pw_length) < 6:
			print("Input less than minimum")
		elif int(pw_length) > 16:
			print("Input higher than maximum")
	except ValueError:
		print("Invalid input")
		
print()
print("[+] 1. Text only with upper and lower case")
print("[+] 2. Lowercase only")
print("[+] 3. Alphanumeric with lowercase")
print("[+] 4. Alphanumeric and punctuation")
print("[+] 5. Numbers only")
print()

upper_alpha = string.ascii_uppercase
lower_alpha = string.ascii_lowercase
nums = string.digits
punct = string.punctuation

while True:
	option = input("[+] Enter a number: ")
	if option.isdigit() and option in ["1", "2", "3", "4", "5"]:
		option = int(option)
		break
	else:
		print("Invalid input")
		
if option == 1:
	pw = "".join(random.choice(upper_alpha + lower_alpha) for i in range(1, pw_lenght + 1))
elif option == 2:
	pw = "".join(random.choice(lower_alpha) for i in range(1, pw_lenght + 1))
elif option == 3:
	pw = "".join(random.choice(nums + lower_alpha) for i in range(1, pw_lenght + 1))
elif option == 4:
	pw = "".join(random.choice(upper_alpha + lower_alpha + punct) for i in range(1, pw_lenght + 1))
else:
	pw = "".join(random.choice(nums) for i in range(1, pw_lenght + 1))

print(f"This is your generated password: {pw}")