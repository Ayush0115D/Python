import asyncio
from concurrent.futures import ThreadPoolExecutor
def encrypt(data):
    return f"encrypted_{data[::-1]}"
async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result=await loop.run_in_executor(pool, encrypt, "my_secret_data")
        print(f"{result}")

if __name__=="__main__":
    asyncio.run(main())