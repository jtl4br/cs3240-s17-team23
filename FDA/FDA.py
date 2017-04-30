import requests
import json

def viewReports():
	r = requests.post('http://127.0.0.1:8000/view_reports_FDA/')

	return r.json()


def login():

	username = input("Username: ")
	password = input("Password: ")

	r = requests.post('http://127.0.0.1:8000/login_FDA/', data = {'username':username, 'password':password})

	r = r.json()

	return r.get('passed')


if login() == 'y':
	print("successful login")
else:
	print("login failed")