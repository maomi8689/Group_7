"""
資料格式：課程、學生、教室、選課紀錄的欄位，以及空的 db。
只定義欄位，不檢查資料、不讀寫檔案。
"""

from dataclasses import dataclass


@dataclass
class Course:
    """一門課程。"""

    course_id: str
    course_name: str
    credit: int
    is_required: bool
    instructor: str
    students_limit: int
    classroom: str
    schedule: dict[str, list[int]]  # {星期 "1"～"7": [節次 1～12]}，a、b、c 存成 10、11、12


@dataclass
class Student:
    """一位學生（已選課程從 db["enrollments"] 計算）。"""

    student_id: str
    name: str
    major: str
    credit_limit: int = 24


@dataclass
class Classroom:
    """一間教室。"""

    classroom_id: str
    capacity: int
    equipment: list[str]
    building: str


@dataclass
class Enrollment:
    """一筆選課紀錄：哪位學生選了哪門課。"""

    student_id: str
    course_id: str


def empty_db() -> dict:
    """建立一個空的 db。

    參數：
        無

    回傳：
        {"courses": {}, "students": {}, "classrooms": {}, "enrollments": []}

    例子：
        db = empty_db()

    對應需求：資料格式
    """
    return {"courses": {}, "students": {}, "classrooms": {}, "enrollments": []}
