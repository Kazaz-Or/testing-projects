

class FileDownload:

    textarea = "#textbox"
    genBtn = "button:has-text(\"Generate File\")"
    downloadLnk = "#link-to-download"

    @staticmethod
    def enter_data_in_textarea(page, value):
        page.fill(FileDownload.textarea, value)
        page.keyboard.type(' ')

    @staticmethod
    def generate_download_link(page):
        page.click(FileDownload.genBtn)

    @staticmethod
    def download_file(page, save_as_file_name):
        with page.expect_download() as download_info:
            page.click(FileDownload.downloadLnk)
        download = download_info.value
        filepath = str(download.path())
        save_file_path = filepath.split("temp")[0] + "temp/" + save_as_file_name
        download.save_as(save_file_path)
        return save_file_path
