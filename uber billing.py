x=int(input("Pickup Location:"))
y=int(input("Drop Location:"))
print("1: 'micro', 2: 'mini', 3: 'auto'")
z=int(input("mode:"))
rate=""
if(z==1):
    price=(y-x)*3
    print(price)
if(z==2):
    price=(y-x)*5
    print(price)
if(z==3):
    price=(y-x)*2
    print(price)
if(z>3):
    print(" choose from the given options")
