a = 10 

if a % 2 == 0 : 
    print("gerade")
else :
    print("ungerade")

f = [30,45,15,89,67,65,45,32,9879,36474,34532]

gerade = []
ungerade = []


for element in f:
    if element % 2 == 0 : 
        gerade.append(element)
    else :
        ungerade.append(element)

print (f"Das sind die geraden Zahlen{gerade}")
print (f"Das sind die ungeraden Zahlen{ungerade}")
