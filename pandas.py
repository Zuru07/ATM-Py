#Modules
import csv
import pandas as pd
#File_Open_CSV1
datalst=[]
with open("D:\Saathvik\CSC IP CLASS XII\Data.csv", "a+", newline="\r\n") as
fh1:
 fh1.seek(0)
 eread=csv.reader(fh1)
 for i in eread:
 datalst.extend(i)
#Interface_1
print(" ")
print("****Welcome to SASU Bank****")
print(" ")
a=(input("Enter Account Number: "))
d=len(datalst)
e=False
for i in range(10,d,6):
 if a==datalst[i]:
 b=datalst.index(a)
 c=input("Enter your PIN Number: ")
 if c==datalst[b-1]:
 print(" ")
 print("Welcome ", datalst[b-3], "!", sep="")
 e=True
 break
 else:
 print(" ")
 print("Invalid PIN Number!")
 break
else:
 print(" ")
 print("Invalid Account Number!")
#Interface_2
if e==True:
 print(" ")
 print('''Choose your Service:
1. Withdrawal
2. Fast Cash
3. Balance Inquiry
4. PIN Change
5. Cash Deposit''')
 print(" ")
 f=int(input("Enter your Choice: "))
#Withdrawal
 if f==1:
 print(" ")
 print("Current Balance: ", float(datalst[b + 1]))
 m = float(input("Enter Amount to be Withdrawn (In Rupees): "))
 if float(datalst[b+1])>m:
 n = float(datalst[b+1]) - m
 o = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 o.loc[int(datalst[b - 4]) - 1, "Amount"] = n
 o.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",index=False)
 print("Balance after Withdrawal: ", n)
 else:
 print("Insufficient Funds!")
#Fast_Cash
 if f==2:
 print(" ")
 print("Current Balance: ", float(datalst[b + 1]))
 p=int(input('''1. 100
2. 500
3. 1000
4. 2000
5. 3000
6. 5000
7. 7500
8. 10000
Choose Option: '''))
 if p == 1:
 if float(datalst[b + 1]) > 100.0:
 q = float(datalst[b + 1]) - 100.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 2:
 if float(datalst[b + 1]) > 500.0:
 q = float(datalst[b + 1]) - 500.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 3:
 if float(datalst[b + 1]) > 1000.0:
 q = float(datalst[b + 1]) - 1000.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 4:
 if float(datalst[b + 1]) > 2000.0:
 q = float(datalst[b + 1]) - 2000.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 5:
 if float(datalst[b + 1]) > 3000.0:
 q = float(datalst[b + 1]) - 3000.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 6:
 if float(datalst[b + 1]) > 5000.0:
 q = float(datalst[b + 1]) - 5000.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 7:
 if float(datalst[b + 1]) > 7500.0:
 q = float(datalst[b + 1]) - 7500.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 if p == 8:
 if float(datalst[b + 1]) > 10000.0:
 q = float(datalst[b + 1]) - 10000.0
 r = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 r.loc[int(datalst[b - 4]) - 1, "Amount"] = q
 r.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv",
index=False)
 print("Balance after Withdrawal: ", q)
 else:
 print("Insufficient Funds!")
 elif p not in [1,2,3,4,5,6,7,8]:
 print("Invalid Input!")
#Balance_Inquiry
 if f==3:
 print(" ")
 bal=float(datalst[b+1])
 print("Current Balance:",bal)
#PIN_Change
 if f==4:
 print(" ")
 pin1=input("Enter OLD PIN Number: ")
 if pin1==datalst[b-1]:
 pin2=input("Enter NEW 4 Digit PIN Number: ")
 if len(pin2)==4:
 pin3=input("Re-enter NEW PIN: ")
 if pin3==pin2:
 g=datalst.index(pin1)
datalst[g]=pin3
 h=pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 h.loc[int(datalst[b-4])-1,"PIN"]=pin3
 h.to_csv("D:\Saathvik\CSC IP CLASS
XII\Data.csv",index=False)
 print("PIN Succesfully Updated!")
 else:
 print("PIN doesn't match!")
 else:
 print("Enter a Valid PIN!")
 else:
 print(" ")
 print("Invalid PIN Number!")
#Cash_Deposit
 if f==5:
 print(" ")
 12
 print("Current Balance: ", float(datalst[b+1]))
 j=float(input("Enter Amount to be Added (In Rupees): "))
 k1=j+float(datalst[b+1])
 l = pd.read_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv")
 l.loc[int(datalst[b - 4]) - 1, "Amount"] = k1
 l.to_csv("D:\Saathvik\CSC IP CLASS XII\Data.csv", index=False)
 print("Balance after Deposition: ", k1)
#Invalid_(e=False)
 elif f not in [1,2,3,4,5]:
 print("Invalid Input!")
else:
 pass
