FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(todos_arg)
