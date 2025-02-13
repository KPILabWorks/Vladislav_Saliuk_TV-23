import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Час виконання: {self.elapsed_time:.6f} секунд")


file_path = "script/script5.py"

with open(file_path, "r", encoding="utf-8") as file:
    code = file.read()

with Timer():
    exec(code)
