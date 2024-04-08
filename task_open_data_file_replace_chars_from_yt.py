def print_and_upper_case_dec(func, *args):
    def wrapper(*args):
        modified_func = func(*args).upper()
        print(modified_func)
        return modified_func
    return wrapper


def process_dataset(file_name: str, process_fn):
    try:
        # with open(file=file_name, mode='r+', encoding='utf-8') as datafile:
        #     lines = [process_record(l) for l in datafile]
        #     datafile.seek(0)
        #     datafile.writelines(lines)
        with open(file=file_name, mode='r', encoding='utf-8') as datafile:
            for line in datafile.readlines():
                process_fn(line)
    except FileNotFoundError as e:
        print(f"Error!!! {e}")


@print_and_upper_case_dec
def process_record(record: str):
    # 1. to lowercase
    # 2. 'o' -> 'z'
    return record.lower().replace('z', 'z')


process_dataset("data.txt", process_record)
