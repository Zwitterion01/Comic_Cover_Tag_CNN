from PIL import Image
import os
#This program is used to copy the data which label is identified as lacking data.
filename='C:\\Users\\johnson\\Desktop\\project\\data\\area_2\\europe\\'
count=15544
i=10

while i<12 :
    j=0
    while j<1025 :
        fn = filename + str(count+j) + '.jpg'
        f1 = open(fn, 'r')
        lena = Image.open(fn)
        lena.save('C:\\Users\\johnson\\Desktop\\project\\data\\area_2\\europe\\' + str(count+j+(i+1)*1024+1) + '.jpg')
        print(str(count+j) + ' done')
        f1.close()
        j=j+1
    i=i+1
