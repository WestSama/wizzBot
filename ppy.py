import datetime, asyncio

async def schedule():
    now = datetime.datetime.now()
    then = now.replace(hour=16, minute=1)
    waitTime = (then-now).total_seconds()
    await asyncio.sleep(waitTime)
    print("Hello")

schedule()