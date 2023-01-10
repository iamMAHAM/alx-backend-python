#!/usr/bin/env python3
"""module : measuring time"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    float random numbers
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    taking_time = time.perf_counter()

    alls = taking_time - start
    
    return alls
