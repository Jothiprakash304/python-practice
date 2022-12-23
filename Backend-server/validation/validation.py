# from flask import jsonify
# import re
# import datetime
# from datetime import date
# from Database.connecting import db_validation


# def Register(First,Last):
#     user_data_validation=Valid(First,Last)
# #     if user_data_validation == True:
# #         db_insert=add_database(First,Last,Email,DOB,Password)
# #         return db_insert
       
# #     else:
# #         return "invalid"
# # def add_database(First,Last,Email,DOB,Password):
# #     user_query="""INSERT INTO Register (FirstName, LastName, Email,DOB,CREDENTIALS) VALUES (%s, %s, %s, %s, %s)"""
# #     user_params=[]
# #     user_params.extend([First,Last,Email,DOB,Password])
# #     db_res=db_validation(user_query,user_params)
# #     print(db_res)
# #     if "error" in db_res:
# #         return "error"
# #     else:
# #         return "success"
    



# def Valid(First,Last):
#     if not validate_First_name(First):
#         return "enter the proper first name"
#     if not validate_Last_name(Last):
#         return "enter the proper Last name"
#     # if not validate_DOB(DOB):
#     #     return "your are below the age of our Requirements"
#     # if not validate_email(email):
#     #     return f"Please enter {'Email'} email id"
#     # if not validate_password(Password):
#     #     return f"Please enter valid {'Password'} password"
#     # if Password!=Confirm_password:
#     #     return "password mismatch"
#     return True




# def validate_First_name(First_name):
#     if First_name.isnumeric():
#         return False
#     if " " in First_name:
#         return False
#     if First_name.isalnum():
#         return True
# def validate_Last_name(Last_name):
#      if Last_name.isnumeric():
#         return False
#      if " " in Last_name:
#         return False
#      if Last_name.isalnum():
#         return True
# # def validate_DOB(DOB):
# #     current=datetime.datetime.strptime(date.today().day,date.today().month,date.today().year)
# #     date_of_birth = datetime.datetime.strptime(DOB, "%d/%m/%Y")
# #     age=current-date_of_birth
# #     if age>=18:
# #         return True
# # def validate_email(Email_id):
# #     regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# #     return re.fullmatch(regex,Email_id)

# # def validate_password(Password):
# #     if (len(Password)>10):
# #         return True
# #     return True
   
