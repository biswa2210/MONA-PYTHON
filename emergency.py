from apscheduler.schedulers.blocking import BlockingScheduler
sched=BlockingScheduler()
from twilio.rest import Client
account_sid = 'AC3e9e194e16b925aac7c14555456d9ed8'
auth_token = 'c2e693a51db7868302d19aa04c17aed0'
client = Client(account_sid, auth_token)
listphno=['whatsapp:+916290272740','whatsapp:+919051942981','whatsapp:+918583939774']


def emergengy():
    for phno in listphno:
        message=client.messages.create(from_='whatsapp:+14155238886',body='I am in maintenance',to=phno)
        message = client.messages.create(from_='whatsapp:+14155238886',body='I WILL ACTIVATE LATER PLEASE FORGIVE ME,I AM IN MAINTENENCE,AND MY OS IS NOT WORKING ALL TIME SO I AM NOT ABLE TO REMIND EVERY THING,I AM ONLY A CONCEPT OF MY BOSS BISWA,OK BYE TAKE CARE',to=phno)
emergengy()