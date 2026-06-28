str_='hossin Ali reza Saman rahman'

print("1_",str_)

str_=str_.lower()
print("2_",str_)



str_=str_.upper()
print("3_",str_)


str_=str_.title()
print("4_",str_)


str_=str_.capitalize()
print("5_",str_)



str_3='1234asc@@@'
str_4='abc1234'
str_5='1234'
str_6='abcd'
str_7='appp\nall23\t'
str_8='ab1234@'



print(str_3, " -> ",str_3.isalnum(),str_3.isdigit(),str_3.isalpha(),str_3.isprintable())
print(str_4, " -> ",str_4.isalnum(),str_4.isdigit(),str_4.isalpha(),str_4.isprintable())
print(str_5, " -> ",str_5.isalnum(),str_5.isdigit(),str_5.isalpha(),str_5.isprintable())
print(str_6, " -> ",str_6.isalnum(),str_6.isdigit(),str_6.isalpha(),str_6.isprintable())
print(str_7, " -> ",str_7.isalnum(),str_7.isdigit(),str_7.isalpha(),str_7.isprintable())


str_al="hossin@Torabi@09112223344@32323232323@Sari\nAli@Torabi@09112223346@32323232326@Sari\nsara@Torabi@09112229900@32323232326@Sari"

strline=str_al.splitlines()

listPtofile=[]
print(strline)


for x in strline:
    str_prof=x.split('@')
    listPtofile.append(str_prof)
    

print(listPtofile)




for x in listPtofile:
   print(x[2])
