class Jumper:
    def __init__(self):
        self.list=[]
    def add_num(self):
        while True:
            num=input("Enter your number: ")
            if num=="STOP":
                break
            self.list.append(num)
    def display(self):
        diff_list=[]
        verify_list=[]
        for i in range(len(self.list)):
            if i==len(self.list)-1:
                break
            verify_list.append(i+1)
            diff_list.append(abs(int(self.list[i])-int(self.list[i+1])))
        diff_list.sort()
        if diff_list == verify_list:
            print("UB Jumper")
        else:
            print("Not UB Jumper")        


obj=Jumper()
obj.add_num()
obj.display()