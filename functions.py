FILE_PATH = "todos-data.txt"


def get_data(file_path=FILE_PATH):

    """
    This function reads the data from given txt file, and returns the data as a list.
    :param file_path:
    :return:
    """

    with open(file_path) as data:
        todos_list = data.readlines()
    return todos_list


def write_data(items: list, file_path=FILE_PATH):

    """
    This function writes the given list in to the given txt file. It does not return anything!!!
    :param items:
    :param file_path:
    :return:
    """

    with open(file_path, mode="w") as data:
        data.writelines(items)


def append_data(todo: str, file_path="todos-data.txt"):

    """
    This function appends the given text to the given txt file. It does not return anything!!!
    :param todo:
    :param file_path:
    :return:
    """

    with open(file_path, mode="a") as data:
        msg = todo.title()
        data.write(f"{msg}" + "\n")
