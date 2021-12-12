Ax=1
Ay=1
Bx=2
By=5
Cx=5
Cy=4
Px=2
Py=3

bx = Bx-Ax
by = By-Ay
cx = Cx-Ax
cy = Cy-Ay
x = Px-Ax
y = Py-Ay

d = bx*cy - cx*by

WA = (x*(by-cy) + y*(cx-bx) + bx*cy-cx*by)/d
WB = (x*cy - y*cx)/d
WC = (y*bx - x*by)/d

if 0 < WA and WB and WC < 1:
    print("P noktasi ucgen alaninin icinde.")
else:
    print("P noktasi ucgen alaninin icinde degil!")
    
print(WA,WB,WC)