# userdefined function ( with argument  with return )

def showMessage(username):
    return "Welcome ,  "+username

print(showMessage('Kunal'))


#user defined function (without argument and with return)
def showMessage():
    username = input("Enter your name : ")
    return "Welcome , "+username

print(showMessage())