import string, random, time, getpass


print("(It will not be shown)")
password = getpass.getpass("Type your password: ")



start = time.time()


while True :
	def id_generator(size = len(password), chars=string.printable):
		return ''.join(random.choice(chars) for _ in range(size))
	if id_generator() == password:
		end = time.time()
		print("found your code")
		print("your code is: " + password)
		print("time it took: " + str(end - start))
		stop = input("")
		break
	else :
		print(id_generator())

