class Usb_Jumper():
    def __init__(self):
        while True:
            num_input=[]
            num_input=input()
            if num_input=="STOP":
                break
            num_list=[int(x) for x in num_input.split()]
            diff_list=[]
            for i in range(len(num_list)-1):
                diff_list.append(num_list[i+1]-num_list[i])

            for i in range(len(diff_list)):
                if diff_list[i]>=len(num_list):
                    print("Not UB Jumper")
                    return
            print("UB Jumper")

output=Usb_Jumper()