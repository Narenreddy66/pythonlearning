# if elseif condions

a=int(input("Enter the Number"))
if (a>18):
    print("You Can vote")
elif (a==0 )    :
    print("You cnnot vote")
else:
    print('soory')    


    # MatchCase

    x=int(input("Enter the alue ofx:"))
    
    match x:

      case 2 :
             print("x is two ")
      case 4:
            print("x is 4")
      case _:
              print("plesejejkefjk")          

#    forloops        

name="Narendhar"
for i  in name:
  print(i , end=( ','))    


  for k in range(5):
    print(k)  

    # while loops

    x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

    # Nested loops

for i in range(1, 4):
    print(i,"iiiiiiiiiiiiiiiii")
    k = 1
    while (k <= 3):
        print(i, "*", k, "=", (i * k))
        k = k + 1
    print()
#  control statemensts
# pass
i = 1
while (i < 5):
    pass
 
for j in range(5):
    pass
 
if (i == 2):
    pass
# break
for i in range(1, 10):
    print(i)
    if (i == 5):
        break
# continue
i = 1
while (i <= 10):
    i = i + 1
    if (i % 2 != 0):
        continue
    print(i)