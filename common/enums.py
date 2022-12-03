
from enum import Enum

class Message(Enum):
    server_error = "INTERNAL SERVER ERROR"
    incorrect_password = "PASSWORD IS INCORRECT"
    success = "SUCCESSFULL"
    try_with_correct_data = "PLEASE TRY WITH CORRECT DATA"
    user_exists = "USER ALREADY EXISTS"
    user_not_exists = "USER DOES NOT EXISTS"
    record_not_found = "RECORD NOT FOUND"
    email_exists = "USER WITH THIS EMAIL ALREADY EXISTS"
    phone_exists = "USER WITH THIS PHONE ALREADY EXISTS"
    query_params_missing = "QUERY PARAM IS MISSING"