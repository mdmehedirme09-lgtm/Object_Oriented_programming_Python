class InvertedDict():
    def __init__(self):
        original = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value1"
        }
        reverse={}
        for key,value in original.items():
            if value not in reverse:
                reverse[value]=[]
            reverse[value].append(key)
        print(reverse)
obj=InvertedDict()