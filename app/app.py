users_list = [{"username": "Harun", "password": "sensei", "role": "admin"}, {"username": "Ken", "password": "mwangi", "role": "moderator"}, {"username": "Mambo", "password": "bryan", "role": "normal"}]

class UserLogin():
	def login_func(self):
		log = input("Enter username: " )
		password= input("Enter password: " )

		for user in users_list:
			if user["username"] == log:
				if user["password"] == password:
					username = log
					print("You have logged in Succesfully")
					return True
			else:
				print ("Log in Unsuccessful")

