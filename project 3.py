def slice(a):
    s=a.index("@")
    u=a[0:s]
    d=a[s+1:]
    print("user name:",u)
    print("domain:",d.upper())
n=int(input("enter the number of emails:"))
l=[]
for i in range(n):
    b=input("enter the mail:")
    l.append(b)
for j in l:
    slice(j)


