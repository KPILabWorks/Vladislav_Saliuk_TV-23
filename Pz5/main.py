import random
import time
from concurrent.futures import ProcessPoolExecutor


def process_item(item):
    if item % 2 == 0:
        result = 1
        for i in range(1, item + 1):
            result *= i
        return result
    return None


def process_large_dataset_in_one_thread(data):
    return [process_item(item) for item in data if item % 2 == 0]


def process_large_dataset_multiprocessing(data, num_processes=4):
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = executor.map(process_item, data, chunksize=len(data) // num_processes)

    return [r for r in results if r is not None]


if __name__ == "__main__":
    dataset = [random.randint(1000, 5000) for _ in range(100000)]

    start_time = time.perf_counter()
    processed_in_one_thread = process_large_dataset_in_one_thread(dataset)
    end_time = time.perf_counter()

    print(f"Кількість оброблених елементів в одному потоці: {len(processed_in_one_thread)}")
    print(f"Час обробки в одному потоці: {end_time - start_time:.2f} секунд\n")

    start_time = time.perf_counter()
    processed_in_multiprocessing = process_large_dataset_multiprocessing(dataset)
    end_time = time.perf_counter()

    print(f"Кількість оброблених елементів в багатопроцесорній обробці: {len(processed_in_multiprocessing)}")
    print(f"Час обробки в багатопроцесорній обробці: {end_time - start_time:.2f} секунд\n")
