import httpx
import logging
from typing import List



from fastapi import Depends
from datetime import date, timedelta, datetime
import random
from enum import Enum

from passlib.context import CryptContext
from datetime import datetime, timedelta
from email.message import EmailMessage
import ssl
import smtplib
from config import settings 
pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


logging.basicConfig(level=logging.INFO)


emailSender = settings.email_sender
emailPassword = settings.email_password




def hash(password: str):
    return pwdContext.hash(password)


def verify(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)



def createUserName(name_of_user: str):
    minimum_capital_letter = 1
    minimum_specia_char = 2
    minimum_digits = 1
    min_len_of_username = 6
    special_chars = ['@','#','$','&']
 
    # variable to store generated username
    username = ""
 
    # remove space from name of user
    name_of_user = "".join(name_of_user.split())
 
    # convert whole name in lowercase 
    name_of_user = name_of_user.lower()
 
    # calculate minimum characters that we need to take from name of user 
    minimum_char_from_name = min_len_of_username-minimum_digits-minimum_specia_char
 
    # take required part from name 
    temp = 0
    for i in range(random.randint(minimum_char_from_name,len(name_of_user))):
        if temp < minimum_capital_letter:
            username += name_of_user[i].upper()
            temp += 1
        else:
            username += name_of_user[i]
 
    # temp_list to store digits and special_chars so that they can be shuffled before adding to username 
    temp_list = []
    # add required digits 
    for i in range(minimum_digits):
        temp_list.append(str(random.randint(0,9)))
 
    # append special characters 
    for i in range(minimum_specia_char):
        temp_list.append(special_chars[random.randint(0,len(special_chars)-1)])
 
    # shuffle list 
    random.shuffle(temp_list)
 
    username += "".join(temp_list)

    return username

# send message to user


def sendEmail(subject: str, body: str, receiver_email: str):
    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = emailSender
    message["To"] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailSender, emailPassword)
        server.send_message(message)


print(createUserName("Rahul"))

    