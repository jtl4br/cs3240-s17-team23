import requests

def login():
	username = input("Username: ")
	password = input("Password: ")

	r = requests.post('http://127.0.0.1:8000/login_FDA/', data = {'username':username, 'password':password})

	return r.json()

def viewReports():
	r = requests.post('http://127.0.0.1:8000/login_FDA/')

	return r.json()

viewReports()