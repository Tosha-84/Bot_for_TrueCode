import asyncio
import aioschedule as schedule
import time

async def job(message='stuff', n=1):
    print("Asynchronous invocation (%s) of I'm working on:" % n, message)
    asyncio.sleep(1)

for i in range(1, 2):
    schedule.every(3).seconds.do(job, n=i)
schedule.every(5).to(10).days.do(job)
schedule.every().hour.do(job, message='things')
schedule.every().day.at("10:30").do(job)

loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(0.1)