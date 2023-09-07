import datetime

class Util:
    @staticmethod
    def get_execution_time(start_time):
        return (datetime.datetime.now() - start_time).total_seconds()
