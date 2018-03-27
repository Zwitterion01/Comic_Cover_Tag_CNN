from PIL import Image
import os
#Change the RGB to grey-level.
count = 0;
while count < 16569:
 counts=str(count)
 filename1 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\' + counts + '.jpg'
 if os.path.exists(filename1):
     f1 = open(filename1, 'r')
     lena = Image.open(filename1)
     lena = lena.convert('L')
     lena.save('C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32_gray\\' + counts + '.pgm')
     print(counts+' done')
     f1.close()
 count = count + 1
