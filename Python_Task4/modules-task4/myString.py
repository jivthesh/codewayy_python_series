
#to return middle character of a string
def middle_char(test_string):
   return test_string[(len(test_string)-1)//2:(len(test_string)+2)//2]


#to return vowel in string
def vowels(test_string):
   count=0
   vowel={'a','e','i','o','u','A','E','I','O','U'}
   for i in test_string:
      if i in vowel:
         count+=1
   print("The numbers of vowels in test_string:",count)

    
#to return length of a string
def length_str(test_string):
    return len(test_string)



#to return number of words in a string
def words_str(test_string):
    res = len(test_string.split())
    return res
    

