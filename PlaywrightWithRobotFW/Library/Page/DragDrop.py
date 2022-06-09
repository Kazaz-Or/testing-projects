
class DragDrop:
    drag_item_locator = "#todrag >> text=Draggable"
    drop_zone = "#mydropzone"
    dropped_item = "#droppedlist >> span"

    @staticmethod
    def drag_item(page, element_number):
        drag_item = DragDrop.drag_item_locator + " " + element_number
        page.drag_and_drop(drag_item, DragDrop.drop_zone)

    @staticmethod
    def get_dragged_items(page):
        dropped_list_values = []
        element_list = page.query_selector_all(DragDrop.dropped_item)
        for element in element_list:
            data = element.text_content()
            dropped_list_values.append(data)
        return dropped_list_values
