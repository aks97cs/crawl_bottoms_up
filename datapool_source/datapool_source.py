"""
 File belongs to hold all the constant information
 that would consider as a main source of extracting data
 this could contain some web link [website link] or some services link [s3 in aws]
"""


class DataPollSourceConstant:

    __instance = None

    @staticmethod
    def get_instance():

        if DataPollSourceConstant.__instance is None:
            DataPollSourceConstant()
        return DataPollSourceConstant.__instance

    def __init__(self):

        if DataPollSourceConstant.__instance is not None:
            raise Exception("Singleton class does not allow creating multiple instances")
        else:
            DataPollSourceConstant.__instance = self

    def get_web_urls(self):
        pass

    def get_s3_urls(self):
        pass



