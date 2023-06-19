def longest(a1, a2):
    list1=[]
    for i in a1:
        if i not in list1:
            list1.append(i)
    for i in a2:
        if i not in list1:
            list1.append(i)
    list1.sort()
    string=''
    for i in list1:
        string+=i
    return string

