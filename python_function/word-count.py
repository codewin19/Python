def wordCount(sentence=""):
    count = 0
    for char in sentence:
        if char==' ':
            count+=1
    return count+1

sen = input("Enter Sentence : ")
print("No. of Words in sentence : ",wordCount(sen))