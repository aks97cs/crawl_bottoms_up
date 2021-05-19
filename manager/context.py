"""
    File belongs to hold all context manager
    used in the apps
"""


class JsonContextManager:

    def __init__(self, filename, mode):

        if not filename.endswith('.json'):
            raise Exception('This context manager does\'t support this file extension')
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
