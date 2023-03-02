#l=10 # global
#def function1(n):
#    l=5
 #   m=8
 #   l=l+45
 #   print(l,m)
 #   print(n,"is printed")
#function1(2)

x= 89
def harry():
    x=20
    def rohan():
      global x
      x=88
      print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
harry()
print(x)