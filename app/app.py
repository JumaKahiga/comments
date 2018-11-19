import datetime
now = datetime.datetime.now()

users_list = [{"username": "Harun", "password": "sensei", "role": "admin"}, {"username": "Ken", "password": "mwangi", "role": "moderator"}, {"username": "Mambo", "password": "bryan", "role": "normal"}]
comments = []
initial_message = "Are you happy?"

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


class Comments(UserLogin):
	def __init__(self):
		self.start = UserLogin.login_func(self)
		#self.username = login_func

	def start_message(self):
		if self.start:
			print(initial_message)
			return True

	def new_comment(self):
		app_starting = Comments.start_message(self)
		if app_starting:
			author = input("Enter username: ")
			comment_id = input("Enter password: ")
			message = input("Enter message: ")    

			comment = {"author": author,
					"comment_id": len(comments)+1,
					"comment": message,
					"timestamp": now.strftime("%Y-%m-%d %H:%M")}    

			print(comment)
			comments.append(comment)
			return True
