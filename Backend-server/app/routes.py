from flask import request,make_response,jsonify
from app import app
from validation.Login import Login
from Database.connecting import db_validation
import datetime
from datetime import date
from datetime import datetime
import re





@app.route ('/Register',methods=["POST"])
def Register_data():
    data=request.get_json()
    First=data["First_name"]
    Last=data["Last_name"]
    Email=data["Email"]
    DOB=data["Dob"]
    Password=data["Password"]
    Confirm_password=data["Confirm_password"]
    Response=Register(First,Last,Email,DOB,Password,Confirm_password)
    if Response == True:
          db_insert=DB_query(First,Last,Email,DOB,Password)
    return make_response(Response)
def DB_query(first,last,email,dob,password):
    user_query="""INSERT INTO Register (FirstName, LastName, Email,DOB,credentials) VALUES (%s, %s, %s, %s, %s)"""
    user_params=[]
    user_params.extend([first,last,email,dob,password])
    db_res=db_validation(user_query,user_params)
    if "error" in db_res:
        return"some error happens"
    else:
        return "Registration success"

def Register(First,Last,Email,DOB,Password,Confirm_password):

     if not validate_name(First):
         return "enter the proper name"
     if not validate_lastname(Last):
         return "enter the proper last name"
     if not validate_Email(Email):
         return "enter the proper email id"
     if not validate_birth(DOB):
         return "Please enter the proper date of birth"
     if not validate_password(Password):
         return "please enter the proper password"
     if Password!=Confirm_password:
         return "password mismatch"
     return True




def validate_name(first):
    if first.isnumeric():
        return False
    if " " in first:
        return False
    if first.isalnum():
        return True
def validate_lastname(Last):
    if Last.isnumeric():
        return False
    if " " in Last:
        return False
    if Last.isalnum():
        return True
def validate_Email(email):
    regex=regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.fullmatch(regex,email)
def validate_birth(birth):
    # today=date.today()
    regex= datetime.strptime(birth,'%d/%m/%Y')
    # current=datetime.strptime(today,"%d,%m,%Y")
    # age=today-regex
    # if age>=18:
    return True
   
def validate_password(password):
    regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    return re.fullmatch(regex,password)

    







@app.route ('/login', methods=["POST"])
def Login_data():
    data=request.get_json()
    Email=data["email"]
    Password=data["password"]
    response=Login(Email,Password)
    return make_response(response)

@app.route ('/add', methods=["POST"])
def add_money():
    data=request.get_json()
    card_number=data["Add"]
    expiry=data["expiry"]
    cv=data["CVV"]
    amount=data["Amount"]
    m_number=data["Mobile_number"]
    save=data["save_details"]
    is_validation=valid(card_number,expiry,cv,amount,m_number,save)
    if is_validation == True:
        db_insert=valid(amount)
def valid(amount):
    user_query="""ALTER TABLE details(amount=amount+amount) VALUES (%d)"""
    user_params=[]
    user_params.extend([amount])
    db_insert=db_validation(user_query,user_params)
    if "error" in db_insert:
        return "error"
    else:
        return "success"
    
def valid(card_number,expiry,cv,amount,m_number,save):
    if len(card_number)<=15:
        return "enter the valid card details"
    today=date.today()
    if today.year<=expiry.year:
        return "your card is expired"
    if len(cv)<3 and len(cv)>3:
        return "enter the proper cv"
    if amount==0:
        return "enter the amount"
    regex=re.compile("(0|91)?[6-9][0-9]{9}")
    if not re.fullmatch(regex,m_number):
        return "enter valid mobile number"
    return True


@app.route ('/minus', methods=["POST"])
def withdraw_money():
    data=request.get_json()
    account=data['']
    ifsc=data['']
    a_name=data['']
    m_number=data['']
    amount=data['']
    is_validation=validation(account,ifsc,a_name,m_number,amount)
    if is_validation == True:
        db_insert=db_minus(amount)
        if db_insert==True:
            return "success"
def db_minus(amount):
    user_query="UPDATE details WHERE Amount=Amount-amount"
    user_params=[]
    user_params.extend([amount])
    db_response=db_validation(user_query,user_params)
    if "error" in db_response:
        return "error"
    else:
        return "success"

def validation(account,ifsc,a_name,m_number,amount):
    if len(account)<11:
        return "please enter the valid account number"
    if not ifsc.isalnum():
        return "IFSC code is mismatch"
    if a_name==int and len(a_name)<=2:
        return "Please enter the proper name"
    if not validate_number(m_number):
        return "mobile number is invalid"
    if not validate_amount(amount):
        return "Sorry unable to process you have minimum balance"
def validate_number(m_number):
    regex=re.compile("(0|91)?[6-9][0-9]{9}")
    return re.fullmatch(m_number,regex)
def validate_amount(amount):
    amount_1="SELECT amount FROM details WHERE amount=?"
    if amount_1>=amount:
        return True
@app.route ('/send', methods=["POST"])
def send_money():
    return True





    
        




    
    

