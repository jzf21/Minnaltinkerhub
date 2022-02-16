import csv

def loginLibrarian():
    username=input("enter username")
    password=input("enter password")
    f=open("librarian.csv",'r')
    reader=csv.reader(f)
    for i in reader:
        if i[0]==username and i[1]==password:
            print("logged in")
        else:
            print("Username or password incorrect")
loginLibrarian()