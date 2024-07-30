database=[["Madhurima Saha",20000],["Rohit Sinha",300000],["Manali Kapur",875689]]

def check_bal(name):
   for i in range(3):
      if database[i][0] == name:
         print(database[i][1])

check_bal("Bantu Sinha")  

def Withd(name,amt_of_withd):
   for i in range(3): 
    if database[i][0]==name:
        if amt_of_withd>=0:
          if amt_of_withd<=database[i][1]:
            print("allowed")
            database[i][1]=database[i][1]-amt_of_withd
            print(database[i][1])
        else:
           print("not allowed")     
Withd("Bantu Sinha",2000)

def Deposite(name,amt_of_deposite):
   for i in range(3):
      if database[i][0]==name:
         if amt_of_deposite>=0:
          database[i][1]=database[i][1]+amt_of_deposite
         print(database[i][1])
Deposite("Madhurima Saha",5000)           