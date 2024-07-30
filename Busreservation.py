Name=["Madhurima","Baban","Dhriti","Mayank","Vivek"]
# def Login(name):
#     # print(Name)
#     for i in range(len(Name)):
#         if Name[i]==name:
#             return 1
#         else:
#             pass
        

# print(Login("Sayan"))        
    
# def Registration(name):
#     if Login(name)==None:
#         Name.append("Sayan")
#         print(Name)

# Registration("Sayan")  
# print(Login("Sayan"))      

def Check_seat():
    no_of_seat = 30
    if len(Name)<= no_of_seat:
        available_Seat=(no_of_seat-len(Name))
        print("No of seat :"+ str(available_Seat))
# Check_seat()    


def Book_seat(name,seat_no):
    data={
        23:"Madhurima",
        24:"Baban",
        15:"Dhriti",
        3:"Mayank",
        21:"Vivek",
        11:"Sayan"
    }
    Check_seat()
    if data.get(seat_no):
        print("Already booked!!")
    else:
        data[seat_no] = name
        print("Seat booked for "+name+" at seat number "+str(seat_no))
        print(data)

Book_seat("poppy",25)
