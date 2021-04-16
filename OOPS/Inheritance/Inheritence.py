class A:
    def f1(self):
        print("F1 is working")
    def f2(self):
        print("F2 is working")

class B(A):  #inheriting A to B
    def f3(self):
        print("F3 is working")
    def f4(self):
        print("F4 is working")

a1=A()
a1.f1()
a1.f2()


b1=B()
b1.f1()
b1.f4()  #calling inherit method from A f4

    