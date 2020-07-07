import string
l = list(string.ascii_letters + string.digits)
print(l[0])
print(l[-1])
print(l[2])
print(l[-3])
print(l[:10])
int_l = []
for i in l :
    try:
        int_l.append(int(i))
    except:
        pass
print(int_l)
print(int_l[::2])
print('-'.join(l))
