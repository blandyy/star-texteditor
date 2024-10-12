# -*- coding: utf-8 -*-
import chardet


def detect_encoding(file_path: str) -> str:
    with open(file_path, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"]
        # confidence = result["confidence"]
        return encoding
