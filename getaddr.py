from urllib import urlretrieve
#coding:utf-8
# -*- coding: cp936 -*-
#Process the dataset
#Date 12.06.2017  Author: Yuan Zhuoqun
myfile = open('C:\\Users\\johnson\\Desktop\\project\\data\\area.txt', 'r')
allWords = []
line = myfile.readline()
while line:
    list = line.split(' ')
    for word in list:
        if word[-1] == '\n':
            allWords.append(word[:-1])
        else:
            allWords.append(word)
    line = myfile.readline()
myfile.close()
i=6
count=0
counts = str(count)
while i<len(allWords):
      #print allWords[i]+' '+allWords[i-4]
      addr='http://image.vdm.cn/'+allWords[i]
      if addr[-3:]=='jpg':
         filename='C://Users//johnson//Desktop//project//data//pic//'+ counts +'.jpg'
         #urlretrieve(addr, filename)                 #Download the image
         myfile_1 = open('C:\\Users\\johnson\\Desktop\\project\\data\\pictag_32X32.txt', 'a ')
         myfile_1.write(counts + '.jpg' + ' ' + allWords[i - 3] + ' ' + allWords[i - 2] + ' ' + allWords[i-1] + '\n' )
         myfile_1.close()
         print filename + ' '+allWords[i]
      if addr[-3:]=='png':
         filename = 'C://Users//johnson//Desktop//project//data//pic//' + counts + '.png'
         #urlretrieve(addr, filename)                 #Download the image
         myfile_1 = open('C:\\Users\\johnson\\Desktop\\project\\data\\pictag_32X32.txt', 'a')
         myfile_1.write(counts + '.jpg' + ' ' + allWords[i - 3] + ' ' + allWords[i - 2] + ' ' + allWords[i - 1] + '\n')
         myfile_1.close()
         print filename + ' '+allWords[i]
      if addr[-3:]=='gif':
         filename = 'C://Users//johnson//Desktop//project//data//pic//' + counts + '.gif'
         #urlretrieve(addr, filename)                 #Download the image
         myfile_1 = open('C:\\Users\\johnson\\Desktop\\project\\data\\pictag_32X32.txt', 'a')
         myfile_1.write(counts + '.jpg' + ' ' + allWords[i - 3] + ' ' + allWords[i - 2] + ' ' + allWords[i - 1] + '\n')
         myfile_1.close()
         print filename + ' '+allWords[i]
      if addr[-4:]=='jpeg':
         filename = 'C://Users//johnson//Desktop//project//data//pic//' + counts + '.jpeg'
         #urlretrieve(addr, filename)                 #Download the image
         myfile_1 = open('C:\\Users\\johnson\\Desktop\\project\\data\\pictag_32X32.txt', 'a')
         myfile_1.write(counts + '.jpg' + ' ' + allWords[i - 3] + ' ' + allWords[i - 2] + ' ' + allWords[i - 1] + '\n')
         myfile_1.close()
         print filename + ' '+allWords[i]
      if( i<len(allWords)-6):
        if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
          i = i + 1;
          if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
              i = i + 1;
              if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
                  i = i + 1
                  if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
                      i = i + 1
                      if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
                          i = i + 1
                          if (allWords[i + 6][0] != "s" or allWords[i + 6][1] != "0"):
                              i = i + 1
      i = i + 6
      count=count+1
      counts = str(count)
print(count)
