

class UtilityCore:

    @staticmethod
    def verify_list_ascending_order(data_list):
        flag = False
        if data_list == sorted(data_list):
            flag = True
        return flag

    @staticmethod
    def verify_list_with_same_values(data_list):
        ele = data_list[0]
        chk = True
        for item in data_list:
            if ele != item:
                chk = False
                break
        return chk

    @staticmethod
    def check_file_content(file_to_read, text_content):
            return True
