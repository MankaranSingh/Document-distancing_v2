############ THIS VERSION USES MULTIDIMENSIONAL ARRAYS AND HASH TABLES TO SIMULATE VECTORS ##########
############ NOTE -- MOST SIMILAR DOCUMENTS ARE THOSE, WHOSE SIMILARITY COEFFICIENT AND POSITIONING COEFFICIENTS ARE BOTH HIGH #############
############ RANGE OF COEFFICIENTS ARE [0,1] ##############
############ MADE BY MANKARAN SINGH ############

d1=str(input('Enter text of Document 1: '))
d2=str(input('Enter text of Document 2: '))
lst1=d1.split(' ')
set1=set(lst1)
lst2=d2.split(' ')
set2=set(lst2)
set3= set1 & set2
vec1={}
vec2={}
count=0
for i in set1:
    for x in lst1:
        if i==x:
            count+=1
    vec1.update({str(i):int(count)})
    count=0
for i in set2:
    for x in lst2:
        if i==x:
            count+=1
    vec2.update({str(i):int(count)})
    count=0

#MAIN

numerator=sum(vec1[x]*vec2[x] for x in set3)
sum1=sum(vec1[x]**2 for x in vec1)
sum2=sum(vec2[x]**2 for x in vec2)
denominator=((sum1)**(1/2))*((sum2)**(1/2))
cos=numerator/denominator
print('Similarity coefficient of two documents is: ', cos)

#POSITION CHECKER TO SEE IF WORDS ARE JUMBLED AND IF IT IS FOOLING DOCUMENT CHECKER V2.0

count=0
if (lst1[i]==lst2[x] for i in range(0,len(lst1)-1) for x in range(0,len(lst2)-1)):
    count+=1
same_pos = count/max(len(lst1), len(lst2))
print('Same postioning coefficient is: ', same_pos)


#VISUALIZATION

import matplotlib.pyplot as plt
plt.subplot(2,3,1)
histogram1=plt.hist(lst1)
plt.subplot(2,3,2)
histogram2=plt.hist(lst2)
plt.show()

