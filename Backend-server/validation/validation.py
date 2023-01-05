# from flask import jsonify
# import re
# from datetime import datetime
# from datetime import date
# from Database.connecting import db_validation
# def Register(First,Last,Email,DOB,Password,Confirm_password):
#     validation=valid(First,Last,Email,DOB,Password,Confirm_password)
#     if validation==True:
#         db_insert=validate_insert(First,Last,Email,DOB,Password)
#     else:
#         return"failed"
# def validate_insert(first,last,email,dob,password):
#      user_query="""INSERT INTO Register (FirstName, LastName, Email,DOB,credentials) VALUES (%s, %s, %s, %s, %s)"""
#      user_params=[]
#      user_params.extend([first,last,email,dob,password])
#      db_res=db_validation(user_query,user_params)
#      if "error" in db_res:
#         return"some error happens"
#      else:
#         return "Registration success"
           





# def valid(first,last,email,dOB,password,confirm_password):
#      if not validate_name(first):
#          return "enter the proper name"
#      if not validate_lastname(last):
#          return "enter the proper last name"
#      if not validate_Email(email):
#          return "enter the proper email id"
#      if not validate_birth(dOB):
#          return "Please enter the proper date of birth"
#      if not validate_password(password):
#          return "please enter the proper password"
#      if password!=confirm_password:
#          return "password mismatch"
   
# def validate_insert(first,last,email,dob,password):
#      user_query="""INSERT INTO Register (FirstName, LastName, Email,DOB,credentials) VALUES (%s, %s, %s, %s, %s)"""
#      user_params=[]
#      user_params.extend([first,last,email,dob,password])
#      db_res=db_validation(user_query,user_params)
#      if "error" in db_res:
#         return"some error happens"
#      else:
#         return "Registration success"
           




# def validate_name(first):
#     if first.isnumeric():
#         return False
#     if " " in first:
#         return False
#     if first.isalnum():
#         return True
# def validate_lastname(Last):
#     if Last.isnumeric():
#         return False
#     if " " in Last:
#         return False
#     if Last.isalnum():
#         return True
# def validate_Email(email):
#     regex=regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
#     return re.fullmatch(regex,email)
# def validate_birth(birth):
#     # today=date.today()
#     regex= datetime.strptime(birth,'%d/%m/%Y')
#     # current=datetime.strptime(today,"%d,%m,%Y")
#     # age=today-regex
#     # if age>=18:
#     return True  
# def validate_password(password):
#     regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
#     return re.fullmatch(regex,password)

