from prefect import flow,task

@task
def print_task():
    return ("Hello World Task")

@flow

def get_results():
    res = 10+5
    return res

@flow
def print_results():
    res = get_results()
    val = print_results()
    print(val + str(res))


if __name__ == "__main__":
    print_results()