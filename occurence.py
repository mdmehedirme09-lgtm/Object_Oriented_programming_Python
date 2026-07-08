class Occurence:
    def __init__(self):
        self.lists=[]
        self.occ=[]
    def add_num(self):
        while True:
            num=input("Enter the number: ")
            if num =="sesh":
                break
            self.lists.append(num)
            


    def display(self):
        unique_list=list(set(self.lists))
        unique_list.sort()
        
        for item in unique_list:
            counts=self.lists.count(item)
            print(f"{item}-{counts} times")


obj=Occurence()
obj.add_num()
obj.display()