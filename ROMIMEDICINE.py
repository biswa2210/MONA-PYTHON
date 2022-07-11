from apscheduler.schedulers.blocking import BlockingScheduler
sched=BlockingScheduler()
from twilio.rest import Client
account_sid = 'AC3e9e194e16b925aac7c14555456d9ed8'
auth_token = 'c2e693a51db7868302d19aa04c17aed0'
client = Client(account_sid, auth_token)
def romimedicine():
        message=client.messages.create(from_='whatsapp:+14155238886',body='Please,madam take your medicine,this is necessary for your health',to='whatsapp:+918583939774')
        message = client.messages.create(from_='whatsapp:+14155238886',body='Please,MISS ROMI TAKE IT AS SOON AS POSSIBLE',to='whatsapp:+918583939774')
sched.add_job(romimedicine, 'cron', day_of_week='mon-sun', hour=13, minute=45, end_date='2020-12-31')
sched.start()