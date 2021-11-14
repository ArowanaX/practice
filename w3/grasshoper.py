first_point=[0,0,10,10,177,10000000000,-433494437,1,-1]
jump=[1,2,10,99,13,987654321,87178291199,0,1]
main_list=list(zip(first_point,jump))
for i in main_list:
    pos=i[0]
    for j in range(1,i[1]+1):
            if pos%2==1:
                pos=pos+j
            elif pos%2==0:
                pos=pos-j
    print(pos)