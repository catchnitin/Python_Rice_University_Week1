#%%
def problem1_7():
    base1 = input("Enter the length of one of the bases:")
    base2 = input("Enter the length of the other base:")
    height = input("Enter the height:") 
    basea = float(base1)
    baseb = float(base2)
    baset =  basea + baseb
    heigt = float(height)
    area = heigt * baset 
    areaf = area / 2
    print("The area of a trapezoid with bases",basea,"and",baseb,end='')
    print(" and height",heigt,"is",areaf)


