class InvertedDict():
    def __init__(self):
        original = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value1",
        "key":  "value1"

        }
        reverse={}
        for key,values in original.items():
            reverse.setdefault(values,[])
            reverse[values].append(key)
        print(reverse)
obj=InvertedDict()
