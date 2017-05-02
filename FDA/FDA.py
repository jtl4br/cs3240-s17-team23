import requests
import json

<<<<<<< HEAD

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
        print("files: ", data[key][8])
        print()

    return r.json()


# return data

def viewReport():
    reportID = input("Enter the id of the report you would like to view: ")
    r = requests.post('http://127.0.0.1:8000/viewReport_FDA/', data={'reportID': reportID})

    data = r.json()

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
        filename = data[key][8]
        print("files: ", data[key][8])
        print()

    dl = input("Would you like to download the files associated with this report? [y/n]: ")
    if dl == 'y':
        download_file(filename)
=======

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
>>>>>>> 8120f60f5c03e56d0dcbce929cb65a9092ee17b6

def viewReport():
    reportID = input("Enter the id of the report you would like to view: ")
    r = requests.post('http://127.0.0.1:8000/viewReport_FDA/', data={'reportID': reportID})

<<<<<<< HEAD
    return r.json()


# return r.get('passed')

def decrypt():
    filename = input("Enter the name of the file you would like to encrypt: ")
    # r = requests.post('http://127.0.0.1:8000/encrypt_FDA/', data={'filename': filename})
    #
    # data = r.json()
    #
    # for key in data:
    #     print("report id: ", key)
    #     print("company name: ", data[key][0])
    #     print("company phone: ", data[key][1])
    #     print("ceo: ", data[key][2])
    #     print("email: ", data[key][3])
    #     print("location: ", data[key][4])
    #     print("sector: ", data[key][5])
    #     print("industry: ", data[key][6])
    #     print("projects: ", data[key][7])
    #     print()
    #
    # return r.json()
=======
    data = r.json()

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
>>>>>>> 8120f60f5c03e56d0dcbce929cb65a9092ee17b6


# return r.get('passed')

def decrypt():
    filename = input("Enter the name of the file you would like to encrypt: ")
    # r = requests.post('http://127.0.0.1:8000/encrypt_FDA/', data={'filename': filename})
    #
    # data = r.json()
    #
    # for key in data:
    #     print("report id: ", key)
    #     print("company name: ", data[key][0])
    #     print("company phone: ", data[key][1])
    #     print("ceo: ", data[key][2])
    #     print("email: ", data[key][3])
    #     print("location: ", data[key][4])
    #     print("sector: ", data[key][5])
    #     print("industry: ", data[key][6])
    #     print("projects: ", data[key][7])
    #     print()
    #
    # return r.json()

<<<<<<< HEAD
=======



>>>>>>> 8120f60f5c03e56d0dcbce929cb65a9092ee17b6
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
        print("Enter '3' to encrypt a file")
        print("Enter 'quit' to exit FDA")
        value = input("Enter command: ")
        print()

        if value == '1':
            viewReports()
        elif value == '2':
            viewReport()
        elif value == '3':
            print("temp")
            #decrypt()
        elif value != 'quit':
            print("Invalid input")
else:
<<<<<<< HEAD
    print("login failed")

=======
    print("login failed")
>>>>>>> 8120f60f5c03e56d0dcbce929cb65a9092ee17b6
