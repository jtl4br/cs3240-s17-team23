import requests
import json


def login():
    username = input("Username: ")
    password = input("Password: ")

    r = requests.post('http://127.0.0.1:8000/login_FDA/', data={'username': username, 'password': password})
    # r = requests.post('https://frozen-mesa-42823.herokuapp.com/', data = {'username':username, 'password':password})
    r = r.json()

    return r.get('passed')


def viewReports():
    r = requests.post('http://127.0.0.1:8000/viewReports_FDA/')

    data = r.json()  # (r.json()).get('reportDictionary')

    for key in data:
        print("report id: ", key)
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


# return data

def viewReport():
    reportID = input("Enter the id of the report you would like to view: ")
    r = requests.post('http://127.0.0.1:8000/viewReport_FDA/', data={'reportID': reportID})
    return r.json()


# return r.get('passed')


# BEGINNING OF THE USER INTERFACE FOR FDA
if login() == 'y':
    print("successful login")
    print()
    print("Welcome to Lohaki!")
    print()

    value = ""

    while value != "quit":
        print("Enter '1' to view reports")
        print("Enter '2' to view a specific report")
        print("Enter 'quit' to exit FDA")
        value = input("Enter command: ")
        print()

        if value == '1':
            viewReports()
        elif value == '2':
            viewReport()
        elif value != 'quit':
            print("Invalid input")
else:
    print("login failed")