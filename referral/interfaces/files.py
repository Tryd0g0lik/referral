"""
Project has dynamic name of js file.
Here we receive a js-file name.
"""
import os


def receive_pathname_js_file() -> str:
    """
    Project has dynamic name of js file.
    Below, a pathname receive to the JS file.
    If a file not find, then, name 'not_JS_file.js' will be
    :return: str
    """

    file_path = f"{os.getcwd()}/referral/static/scripts"
    files_js_list = os.listdir(file_path)
    file_js_name = "not_JS_file.js"
    if len(files_js_list) > 0:
        file_js_name = files_js_list[0][0:]
        return f"/static/scripts/{file_js_name}"

    print("[profiles]: Something what wrong! Not JS file.")
    return f"/static/scripts/{file_js_name}"
