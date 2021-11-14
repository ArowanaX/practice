def balance():
    word=input("write a or b: ")
    if word[0]==word[-1]:
        print(word)
    else:
        if word[0]=="a":
            print("b"+word[1:])
        else:
            print("a"+word[1:])
for i in range(int(input("test case: "))):
    balance()