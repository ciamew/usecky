from PIL import Image
pic = Image.new("RGB",(250, 250),"white")
pixels = pic.load()

a1 = int(input("Zadaj x-ovu suradnicu bodu A: "))
a2 = int(input("Zadaj y-ovu suradnicu bodu A: "))
b1 = int(input("Zadaj x-ovu suradnicu bodu B: "))
b2 = int(input("Zadaj y-ovu suradnicu bodu B: "))

v1 = abs(b1 - a1) #vektor 1
v2 = abs(b2 - a2) #vektor 2

if a1 > b1:
    bx = -1
else:
    bx = 1
if a2 > b2:
    by = -1
else:
    by = 1


sz = v1 - v2 #size

while a1 != b1 or a2 != b2:
    pixels[a1, a2] = (0, 0, 0) #nastavy farbu ciary
    e2 = 2 * sz
    if e2 > -v2:
        sz -= v2
        a1 += bx
    if e2 < v1:
        sz += v2
        a2 += by

pic.show()
