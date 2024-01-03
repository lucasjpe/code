import asyncio

async def example_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(example_coroutine())
