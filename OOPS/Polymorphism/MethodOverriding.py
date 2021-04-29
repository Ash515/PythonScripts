class Father:
    
    def show(self):
        print("my fathers phone is Nokia")

class Son(Father):
  
    def show(self):
        print("my phone is Readmi")  #overrides here


myphone=Son()
myphone.show()