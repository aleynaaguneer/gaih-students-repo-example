list1=[2,4,6,8,10]
print("İlk listem:",list1)
list2=[1,3,5,7,9,11]
print("İkinci listem:",list2)
list1.extend(list2)
print("Birleştirilmiş Yeni Listem:",list1)
list1= [x*2 for x in (list1)]
print("Yeni listemin 2 ile çarpılmış hali:",list1)
for i in list1:
    print("{} adlı değerin veri tipi: {}".format(i, type(i)))
