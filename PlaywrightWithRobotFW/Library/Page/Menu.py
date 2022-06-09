
class Menu:
    first_menu_locator = "#treemenu >> text=FIRST"
    second_menu_locator = "#treemenu >> text=SECOND"

    @staticmethod
    def navigate_menu_item(page, first_level_menu, second_level_menu):
        first_menu = Menu.first_menu_locator.replace('FIRST', first_level_menu)
        second_menu = Menu.second_menu_locator.replace('SECOND', second_level_menu)
        page.locator(first_menu).click()
        page.locator(second_menu).click()
