def Flames(name1,name2):
    namestr = name1 + name2

for c in namestr:
if namestr.count(c) != 1:
# counting common letters
namestr = namestr.replace(c,"")

# The common letters are repalced by blankspace therefore namestr has only remaining letters

print("FLAMES....")
print("F = Friend \nL = Love \nA = Affection \nM = Marriage \nE = Enemy \nS = Siblings \n\n")

numbre = len(namestr) % 6
# number to move through FLAMES
rel = ""

if nnumber == 1:
rel += "Friends"
elif number == 2:
rel += "love"
elif number == 3:
rel += "Affection"
elif number == 4:
rel += "Marriage"
elif number == 5:
rel += "Enemy"
elif number == 0:
rel += "Siblings"
else:

return rel

n1 = input("Enter your name : ").upper()
n2 = input("Enter your crush name : ").upper()
print(f"Your Relationship is : {flames(n1,n2)}")