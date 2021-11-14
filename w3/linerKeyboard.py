
def word_distance():
    key_board=str(input("write the keyboard: "))
    key_board.lower()
    word_s=str(input("write the s word: "))
    word_s.lower()
    flag=False
    ans=0
    for i in word_s:    
        if flag==False:
            dic1=key_board.find(i)+1
            flag=True
        else:
            dic2=key_board.find(i)+1
            ans+=abs(dic2-dic1)
            dic1=dic2
    return ans
    
for i in range(int(input("test case: "))):
    print(word_distance())
