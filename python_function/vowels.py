def countVowel(username):
    count =  0
    for char in username.lower():
        if char in ['a','e','i','o','u']:
            count+=1
            
    return count

name = input("Enter Your Name : ")
print("your name cantians ",countVowel(name)," Vowels")