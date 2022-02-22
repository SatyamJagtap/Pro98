
def swapword():
    a = input("Enter First File Name")
    b = input("Enter Second File Name")
    
    with open(a,'r') as afile:
        data_a = afile.read()
    with open(b,'r') as bfile:
        data_b = bfile.read()
    with open(a,"w") as afile:
        afile.write(data_b)
    with open(b,"w") as bfile:
        bfile.write(data_a)

            

swapword()