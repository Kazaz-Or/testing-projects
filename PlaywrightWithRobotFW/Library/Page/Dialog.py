
class Dialog:

    alert_box_click_me = "text=Click me!"
    confirm_box_click_me = ":nth-match(:text(\"Click me!\"), 2)"
    prompt_box_click_me = "text=Click for Prompt Box"
    prompt_message = None

    @staticmethod
    def init_dialog_accept(page):
        page.on("dialog", Dialog.handle_dialog)

    @staticmethod
    def handle_dialog(dialog):
        print("DIALOG TYPE = " + dialog.type)
        print("DIALOG MESSAGE = " + dialog.message)
        dialog.accept(Dialog.prompt_message)

    @staticmethod
    def set_prompt_message(message):
        Dialog.prompt_message = message

    @staticmethod
    def click_for_alert_box(page):
        page.click(Dialog.alert_box_click_me)

    @staticmethod
    def click_for_confirm_box(page):
        page.click(Dialog.confirm_box_click_me)

    @staticmethod
    def click_for_prompt_box(page):
        page.click(Dialog.prompt_box_click_me)
