

class PagePopup:
    follow_twitter_btn = "text=Follow On Twitter"
    sign_up_twtr = "text=Sign up for Twitter"

    parent_demo_home_btn = "text=Demo Home"

    @staticmethod
    def sign_up_twitter_popup(page):
        with page.expect_popup() as popup_info:
            page.click(PagePopup.follow_twitter_btn)
        pop_up_page = popup_info.value

        pop_up_page.click(PagePopup.sign_up_twtr)

        page.click(PagePopup.parent_demo_home_btn)
        pop_up_page.close()





