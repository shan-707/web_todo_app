FILEPATH = "E:\Python_Course\To-Do_App\To-Do data file.txt"

def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of To-Do items"""
    with open(filepath, 'r') as fh:
        tasks_local = fh.readlines()
    return tasks_local

def write_todos(todos, filepath = FILEPATH):
    """Open file in write mode and write the To-Do in the file.
    (Will truncate existing data before adding new data)
    """
    with open(filepath, 'w') as fh:
        fh.writelines(todos)