class month():
    def __init__(self):
        dict={"January":31,"February":29,"March":31
        ,"April":30,"May":31,"June":30,"July":31,
        "August":31,"September":30,"October":31,
        "November":30,"December":31}
        #print(dict)
        name=input("Enter the month name :")
        print(dict[name])
        print("The month in sorted order are :")
        print()
        for key in sorted(dict):
            print(key)
        print("The month with 31 days are :")
        print()
        for key in dict:
            if dict[key]==31:
                print(key)
        print("the key_value pairs in sorted(in order to values) order are :")
        for key in sorted(dict,key=dict.get):
            print(key,dict[key])
        print("Sorted in descending order of values are :")
        for key in sorted(dict,key=dict.get,reverse=True):
            print(key,dict[key])
out=month()


        