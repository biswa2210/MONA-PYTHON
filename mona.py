#IN WHATSAPP, WISH ME TO ME THROUGH TWILIO....(MONA)
#add phone number in listphno and a sms type 'join ask-chamber' to whatsapp:+14155238886
from twilio.rest import Client
import os
import time
import emoji
import datetime
from twilio.rest import Client
#wish me
h=datetime.datetime.now().hour
if h >= 0 and h <= 12:
    string="GOOD MORNING"
elif h > 12 and h < 18:
    string="GOOD AFTERNOON"
else:
    string="GOOD EVENING"
listphno=['whatsapp:+916290272740','whatsapp:+919051942981','whatsapp:+918583939774']
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = 'AC3e9e194e16b925aac7c14555456d9ed8'
auth_token = 'c2e693a51db7868302d19aa04c17aed0'
client = Client(account_sid, auth_token)
def wishme():
    for phno in listphno:
        message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=string,
                                  to=phno
                              )
    for phno in listphno:
        message = client.messages.create(
                                          from_='whatsapp:+14155238886',
                                          body=f'I AM MONA,I AM YOUR GOOD VIRTUAL FRIEND,I SHALL CARE YOUR HEALTH AND REMIND YOUR IMPORTANT TASKS,AND PLEASE DO NOT REPLY ME BECAUSE I AM NOT ABLE TO GIVE ANY ANSWERS AND CANNOT DO ANY WORK ASPER YOUR GIVEN COMMAND,I AM YOUR WELL WISHER ONLY....{emoji.emojize(":grinning_face_with_big_eyes:")}',
                                          to=phno
                                      )

def reminddrinkme():
    for phno in listphno:
        message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=f'Please,Drink water now,It is good for your health {emoji.emojize(":thumbs_up:")}{emoji.emojize(":thumbs_up:")}{emoji.emojize(":thumbs_up:")}{emoji.emojize(":thumbs_up:")}',
                                  to=phno
                              )

wishme()
time.sleep(16)
for phno in listphno:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Drinking water is good for your health,so I shall remind you to drink water every two hours {emoji.emojize(":thumbs_up:")}',
        to=phno
    )
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(reminddrinkme, 'interval', hours=2)
sched.start()

#ROMI MEDICINE reminder
def romimedicine():
    message=client.messages.create(from_='whatsapp:+14155238886',body='Please,madam take your medicine,this is necessary for your health',to='whatsapp:+918583939774')
    message = client.messages.create(from_='whatsapp:+14155238886',body='Please,MISS ROMI TAKE IT AS SOON AS POSSIBLE',to='whatsapp:+918583939774')
sched.add_job(romimedicine, 'cron', day_of_week='mon-sun', hour=13, minute=45, end_date='2020-12-31')
sched.start()