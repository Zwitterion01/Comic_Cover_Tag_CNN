from PIL import Image
import os
#This program is used to generate a unified dataset.
count=0;
while count<16569:
 counts=str(count)
 filename1 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic\\' + counts + '.jpg'
 filename2 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic\\' + counts + '.png'
 filename3 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic\\' + counts + '.jpeg'
 filename4 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic\\' + counts + '.gif'
 if os.path.exists(filename1):
     f1=open(filename1,'r')
     lena = Image.open(filename1)
     lena = lena.convert('RGB')
     out = lena.resize((32, 32))
     out.save('C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\' + counts + '.jpg')
     print(counts+' done')
     f1.close()

 if os.path.exists(filename2):
     f1=open(filename2,'r')
     lena = Image.open(filename2)
     lena = lena.convert('RGB')
     out = lena.resize((32, 32))
     out.save('C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\' + counts + '.jpg')
     print(counts + ' done')
     f1.close()

 if os.path.exists(filename3):
     f1=open(filename3,'r')
     lena = Image.open(filename3)
     lena = lena.convert('RGB')
     out = lena.resize((32, 32))
     out.save('C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\' + counts + '.jpg')
     print(counts + ' done')
     f1.close()

 if os.path.exists(filename4):
     f1=open(filename4,'r')
     lena = Image.open(filename4)
     lena = lena.convert('RGB')
     out = lena.resize((32, 32))
     out.save('C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\' + counts + '.jpg')
     print(counts + ' done')
     f1.close()

 count=count+1