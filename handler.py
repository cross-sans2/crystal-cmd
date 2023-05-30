def handle_error(error_message, file_path):
    """
    Handle errors and save them to a file.

    Parameters:
    - error_message (str): The error message to be saved.
    - file_path (str): The path to the file where the error message will be saved.

    This function appends the error message to the specified file.
    """
    with open(file_path, 'a') as f:
        f.write(error_message + '\n')
