import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f'Task {name} completed')
    return f'{name} result'

async def main():
    result = await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1),
    )
    print(result)

# Запуск
asyncio.run(main())

