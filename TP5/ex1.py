class Pile:
    list = []
    def __init__(self,list):
        self.list  = list

    def delete(self):
        if(len(self.list)==0):
            print("list empty can't pop an element")
            return
        self.list.pop()
        print(stack)
    def add(self,x):
        if(len(self.list) == 3):
            print("list full maximum 3")
            return
        self.list.append(x)
        print(stack)
    def __str__(self):
        return(str(self.list))

stack = Pile([])
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)
stack.delete()
stack.delete()
stack.delete()
stack.delete()
stack.delete()