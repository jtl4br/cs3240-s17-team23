import requests
import json


def login():

	username = input("Username: ")
	password = input("Password: ")

	r = requests.post('http://127.0.0.1:8000/login_FDA/', data = {'username':username, 'password':password})

	r = r.json()

	return r.get('passed')

def viewReports():
	r = requests.post('http://127.0.0.1:8000/viewReports_FDA/')

	data = r.json()

	for key in data:
		print("company name: ", data[key][0])
		print("company phone: ", data[key][1])
		print("ceo: ", data[key][2])
		print("email: ", data[key][3])
		print("location: ", data[key][4])
		print("sector: ", data[key][5])
		print("industry: ", data[key][6])
		print("projects: ", data[key][7])
		print()
	
	return r.json()


# BEGINNING OF THE USER INTERFACE FOR FDA
if login() == 'y':
	print("successful login")
	print()
	print("Welcome to Lohaki!")
	print()

	value = input("Enter '1' to view reports: ")

	print(value)

	if value == '1':
		viewReports()
	else:
		print("Invalid input")
else:
	print("login failed")
