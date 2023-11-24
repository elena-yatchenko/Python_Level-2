"""Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование."""

from datetime import datetime
import argparse
import os
from pathlib import Path
from collections import namedtuple
import logging

parser = argparse.ArgumentParser(prog="Path_info", description="Task_6 parser")
parser.add_argument("path", metavar="P", type=str, nargs="*", help="введите путь")
args = parser.parse_args()
print(f"В скрипт передано: {args}")

logging.basicConfig(level=logging.INFO, filename="directory.log", encoding="utf-8")
logger = logging.getLogger(__name__)


def directory_data(_path: str) -> namedtuple:
    logger.info(f"время запуска: {datetime.now()}")
    Directory = namedtuple(
        "Directory",
        ["name", "ext", "description", "parent"],
        defaults=["test", None, os.getcwd()],
    )

    results = []
    n_dir = 1
    n_file = 1
    for dir_path, dir_list, file_list in os.walk(_path):
        for each_dir in dir_list:
            name = each_dir
            ext = ""
            description = "directory"
            parent = dir_path.split("\\")[-1]
            dir_data = Directory(name, ext, description, parent)
            results.append(dir_data)
            logger.info(
                f"данные папки № {n_dir}: {dir_data.name}, {dir_data.ext}, {dir_data.description}, {dir_data.parent}"
            )
            n_dir += 1

        for each_file in file_list:
            name = each_file.split(".")[:-1]
            ext = each_file.split(".")[-1]
            description = "file"
            parent = dir_path.split("\\")[-1]
            dir_data = Directory(name, ext, description, parent)
            results.append(dir_data)
            logger.info(
                f"данные файла № {n_file}: {dir_data.name}, {dir_data.ext}, {dir_data.description}, {dir_data.parent}"
            )
            n_file += 1
    return results


directory_data(*args.path)

# !!!!! (см. пример реализации в !!teacher_samples_5_6)


