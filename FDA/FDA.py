import requests

def login():
	username = input("Username: ")
	password = input("Password: ")

	r = requests.post('http://127.0.0.1:8000/login_api/', data = {'username':username, 'password':password})

	return r.json()


login()