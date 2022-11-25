def slice(a):
    s=a.index("@")
    u=a[0:s]
    d=a[s+1:]
    print("user name:",u)
    print("domain:",d.upper())
n=int(input("enter the number of emails:"))
l=[]
for i in range(n):
    a=input("enter the mail:")
    l.append(a)
for j in l:
    slice(j)


