name = input("what \'s your name ?")
email = input("Enter your email address :")
email_index = email.index("@")
user_name = email[:email_index]
print(f"Hello {name.capitalize()} your email is {user_name}")
 