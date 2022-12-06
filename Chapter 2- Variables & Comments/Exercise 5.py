cash = int(input("please input the amount of cash you have: "))
USB = int(input("how much is each USB?: "))
print("you could get", cash//USB)

amount = int(input("how many USB's did you get?: "))

print("you're going to spend: ", amount*USB)
print("which makes your change: ", cash-amount*USB)