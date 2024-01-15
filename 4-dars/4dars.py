# d=20

# def my_func():
#     prefix="Abdulaziz"
#     print(f"{prefix} is {d}")


# my_func()


def outer():
    a=25
    name="Python"
    

    def inner(prefix):
        print(f"{name} is {prefix}")

    return inner