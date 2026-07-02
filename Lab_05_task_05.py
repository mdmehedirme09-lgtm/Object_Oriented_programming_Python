import json

class FilterEven():
    def __init__(self):
        my_dict=json.loads(input("Enter the dictionary: "))
        print()
        result={}
        for key,value in my_dict.items():
            even_number=[]
            for num in value:
                if num%2==0:
                    even_number.append(num)
            result[key]=even_number
        print(result)
output=FilterEven()