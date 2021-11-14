for i in range(int(input("test case: "))):
    len_list = int(input("len reshte ra vared konid: "))
    obj_list = list(map(int, input("list ra vared konid(bein har adad space bezanid): ").split()))
    color = list(input("rang ra vared konid(horoof bozorg): "))
    up = []
    down = []
    for i in range(len_list):
        if color[i] == "B":
            down.append(obj_list[i])
        else:
            up.append(obj_list[i])
    up.sort()
    down.sort()
    sw = False
    i = j = 0
    pos_iter = 1
    while i < len(up) and j < len(down):
        if down[j] >= pos_iter:
            j +=1
            pos_iter +=1
        elif up[i] <= pos_iter:
            i += 1
            pos_iter += 1
        else:
            sw = True
            break
    if sw==True:
        print("NO")
        continue
    while i < len(up):
        if up[i] <= pos_iter:
            i += 1
            pos_iter += 1
        else:
            sw = True
            break
    if sw==True:
        print("NO")
        continue
    while j < len(down):
        if down[j] >= pos_iter:
            j +=1
            pos_iter +=1
        else:
            sw = True
            break
    if sw==True:
        print("NO")
    else:
        print("YES")