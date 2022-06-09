

class TableSortSearch:

    entries_select = "select[name=\"example_length\"]"
    search_box = "input[type=\"search\"]"
    sorted_column = "#example >> td[class=\"sorting_1\"]"

    @staticmethod
    def select_table_entries(page, value):
        page.select_option(TableSortSearch.entries_select, value)

    @staticmethod
    def sort_column(page, column_name):
        page.click("text=" + column_name)

    @staticmethod
    def search_table_data(page, data):
        page.fill(TableSortSearch.search_box, data)

    @staticmethod
    def get_sorted_data_list(page):
        data_list_values = []
        element_list = page.query_selector_all(TableSortSearch.sorted_column)
        for element in element_list:
            data = element.text_content()
            data_list_values.append(data)
        return data_list_values
