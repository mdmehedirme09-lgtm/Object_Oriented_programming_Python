class occurence():
    def __init__(self):
        num_list=[]
        while True:
            num=input("Enter a number: ")
            if num=="SESH":
                break
            num=int(num)
            num_list.append(num)

        for i in num_list:
            count=num_list.count(i)
            #print(f"{i} - {count} times")
        uniq_list=list(set(num_list))
        for i in uniq_list:
            count=num_list.count(i)
            print(f"{i} - {count} times")

occ=occurence()