import random
import string

lower_len=int(input("Enter No.of Lowercase Characters"))
upper_len=int(input("Enter No. of Uppercase Characters"))
digit_len=int(input("Enter No. of digits"))
symbol_len=int(input("Enter No. of Symbols"))

pwd_len=lower_len+upper_len+digit_len+symbol_len

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
  
str=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=digit_len)+random.choices(symbol,k=symbol_len)

random.shuffle(str)
password="".join(str)
print("Password is :",password)
