def log_executor(func, *args):
    def printer(*args):
        print("Arguments:", args)
        return func(*args)
    return printer


@log_executor
def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(f"Result: {result}")
