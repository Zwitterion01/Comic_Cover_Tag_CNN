import os
count=0
#Detect data lose.
while count<=16568:
 counts=str(count)
 filename1='C:\\Users\\johnson\\Desktop\\project\\data\\pic_32X32\\'+counts+'.jpg'
 filename2='C:\\Users\\johnson\\Desktop\\project\\data\\pic\\'+counts+'.png'
 filename3='C:\\Users\\johnson\\Desktop\\project\\data\\pic\\'+counts+'.jpeg'
 filename4 = 'C:\\Users\\johnson\\Desktop\\project\\data\\pic\\' + counts + '.gif'
 if os.path.exists(filename1): #or os.path.exists(filename2)or os.path.exists(filename3)or os.path.exists(filename4):
     print(counts + ' exist')

 else:
     print(counts+' doesnt exist')
     break

 count=count+1
