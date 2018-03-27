from PIL import Image
#Get a document of the dataset and split the dataset.
filename1= 'D:\\project\\data\\pictag_32X32.txt'
f1 = open(filename1, 'r')
allWords = []
line = f1.readline()
while line:
    list = line.split(' ')
    for word in list:
        if word[-1] == '\n':
            allWords.append(word[:-1])
        else:
            allWords.append(word)
    line = f1.readline()
f1.close()
i=0
a=len(allWords)/4
'''ip=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
typ=0
while i<a:
    typ=int(allWords[2 + 4 * i])
    ip[typ-16]=ip[typ-16]+1
    i=i+1
i=0
while i<len(ip):
    print(str(i+16)+' '+str(ip[i]))
    i=i+1
'''
filename2='D:\\project\\data\\pic_32X32\\'
while i<a:
    if allWords[2+4*i] == '16':
        filename3=filename2+str(i)+'.jpg'
        f1 = open(filename3, 'r')
        lena = Image.open(filename3)
        lena.save('D:\\project\\data\\theme_train\\hotblood\\' + str(i)+'.jpg')
        print(str(i)+'.jpg' + ' done')
        f1.close()
    if allWords[2+4*i] == '20'or allWords[2+4*i] == '19':
        filename3=filename2+str(i)+'.jpg'
        f1 = open(filename3, 'r')
        lena = Image.open(filename3)
        lena.save('D:\\project\\data\\theme_train\\schoollove\\' + str(i) + '.jpg')
        print(str(i) + '.jpg' + ' done')
        f1.close()
    if allWords[2+4*i] == '24':
        filename3 = filename2 + str(i) + '.jpg'
        f1 = open(filename3, 'r')
        lena = Image.open(filename3)
        lena.save('D:\\project\\data\\theme_train\\sports\\' + str(i) + '.jpg')
        print(str(i) + '.jpg' + ' done')
        f1.close()
    if allWords[2+4*i] == '25'or allWords[2+4*i] == '26':
        filename3=filename2+str(i)+'.jpg'
        f1 = open(filename3, 'r')
        lena = Image.open(filename3)
        lena.save('D:\\project\\data\\theme_train\\scifi\\' + str(i) + '.jpg')
        print(str(i) + '.jpg' + ' done')
        f1.close()
    if allWords[2+4*i] == '35':
        filename3=filename2+str(i)+'.jpg'
        f1 = open(filename3, 'r')
        lena = Image.open(filename3)
        lena.save('D:\\project\\data\\theme_train\\magic\\' + str(i)+'.jpg')
        print(str(i)+'.jpg' + ' done')
        f1.close()
    i=i+1