#python fibonacci series print program

userinput = int(input("how much fibonacci series : "))
myl = [0, 1]
for x in range(userinput):
    df = myl[-1]+myl[-2]
    myl.append(df)
data = myl[0:-2]
for y in data:
    print(y)
