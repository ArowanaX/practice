for _ in range(int(input("test case: "))):
    len_num = int(input("len adad ra vared konid: "))
    test_list = [int(elm) for elm in input("list adad ro vared konid: ").split()]
    ans = 0
    for i in range(len_num):
        ans = max(ans,test_list[i]-i-1)
    print(ans)