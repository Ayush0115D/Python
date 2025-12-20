import asyncio
import threading
import time
def background_work():
   while True:
     time.sleep(2)
     print("logging the system health...")

async def fetch_orders():
  await asyncio.sleep(3)
  print("Orders fetched.")

threading.Thread(target=background_work, daemon=True).start()
asyncio.run(fetch_orders())