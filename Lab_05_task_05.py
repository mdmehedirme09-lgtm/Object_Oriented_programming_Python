class FilterEven:
    def __init__(self):
        self.Dict={"v":[1,4,6,10],"VI":[1,4,12],"VII":[1,3,8]}
        self.lists=[]
        self.new_list=[]
        for key in self.Dict:
            self.lists.append(self.Dict[key])
            
        for i in range(len(self.lists)):
            self.new_list.append([])
            for j in range(len(self.lists[i])):
                if self.lists[i][j]%2==0:
                    self.new_list[i].append(self.lists[i][j])

        # print(self.new_list)
        k=0
        for key in self.Dict:
            self.Dict[key]=self.new_list[k]
            k+=1
        print(self.Dict)
a=FilterEven()
