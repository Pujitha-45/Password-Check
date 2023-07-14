a,b,c,d=0,0,0,0
l=m=p=q=[]
s=input("Enter your password:")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="!@#$%^&*()_[\]{};:<>?/"
digits="0123456789"
if (len(s)>=8):
 for i in s:
     if(i in smallalphabets):
         a+=1
     elif(i in capitalalphabets):
         b+=1
     elif(i in digits):
         c+=1
     elif(i in specialchar):
         d+=1
         
if(a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(s)):
 print("Valid Password")
 print("No. Small Alphabets are:",a)
 print("No. Capital Alphabets are:",b)
 print("No. Digits are:",c)
 print("No. Special Characters:",d)
 
else:
 print("Invalid Password")
