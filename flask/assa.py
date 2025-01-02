import asyncio

async def coro(n):
    await asyncio.sleep(n)  # Simulate an asynchronous task
    return n

async def main():
    tasks = [asyncio.create_task(coro(i)) for i in range(3)]  # Create tasks
    results = await asyncio.gather(*tasks)  # Gather the results of all tasks
    print(results)

asyncio.run(main())  # Run the main function