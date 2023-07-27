from prefect import flow, task
from prefect.blocks.system import String
string_block = String.load("string-block")

@task
def create_message():
    msg = string_block.value
    return msg

@flow
def create_subflow():
    value = 100
    return value

@flow
def hello_world():
    val = create_subflow()
    msg = create_message()
    res = msg + str(val)
    print(res)
if __name__ == "__main__":
    hello_world()