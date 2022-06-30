import csv
import os


class UserLoader:

    user_list = []
    csv_file_path = os.getcwd() + "/PerformanceTestingWithLocust/data/user.csv"

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(UserLoader.csv_file_path))
        for line_elem in reader:
            UserLoader.user_list.append(line_elem)

    @staticmethod
    def get_user():
        if len(UserLoader.user_list) < 1:
            UserLoader.load_users()
        user_obj = UserLoader.user_list.pop()
        return user_obj
