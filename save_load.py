"""存檔與載入：data/ 的 JSON 檔和 db 互相轉換，是唯一會讀寫檔案的地方。"""

import data_formats


def load_data(data_dir: str) -> dict:
    """讀取 data_dir 裡的 courses.json、students.json、classrooms.json、enrollments.json，組成 db。

    參數：
        data_dir：資料夾路徑，例如 "data"

    回傳：
        db

    例子：
        db = load_data("data")

    對應需求：F6
    """
    raise NotImplementedError


def save_data(db: dict, data_dir: str) -> None:
    """把 db 寫進 data_dir 的四個 JSON 檔。

    參數：
        db：全部資料
        data_dir：資料夾路徑，例如 "data"

    回傳：
        無

    例子：
        save_data(db, "data") 之後 load_data("data") → 得到和 db 一樣的資料

    對應需求：F6
    """
    raise NotImplementedError
