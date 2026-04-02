inp=input("Type a list of numbers between 0 and 9.")

pangram=True

num={"1":0,
     "2":0,
     "3":0,
     "4":0,
     "5":0,
     "6":0,
     "7":0,
     "8":0,
     "9":0,
     }

for i in inp:
    if i in num:
        num[i]+=1

print()

for i in num.values():
    if i==0:
        pangram=False
        break
if pangram:
    print("The input is a pangram.")
else:
    print("The input is not a pangram.")