# -*- coding: utf-8 -*-

import logging
import os
import platform


class Logger:
    def __init__(self):
        if platform.system() == "Windows":
            self.data_root = os.getenv("APPDATA")
        else:
            self.data_root = os.path.join(os.getenv("HOME"), ".local/share/")

        if not os.path.isdir(os.path.join(self.data_root, "CodeLib-Local")):
            os.mkdir(os.path.join(self.data_root, "CodeLib-Local"))

        open(os.path.join(self.data_root, "CodeLib-Local", "log.txt"), "w")

        self.logger = logging.getLogger("CodeLib-Local Logger")

        self.format = "[%(asctime)s - %(levelname)s]  %(message)s"

        self.file_handler = logging.FileHandler(os.path.join(self.data_root, "CodeLib-Local", "log.txt"), "w", encoding='utf-8')
        self.stream_handler = logging.StreamHandler()
        self.file_handler.setLevel(logging.DEBUG)
        self.stream_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(logging.Formatter(self.format))
        self.stream_handler.setFormatter(logging.Formatter(self.format))

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
        self.logger.setLevel(logging.DEBUG)

        self.allLogs = ""

    def log(self, level: int, content: str):
        self.logger.log(level=level, msg=content)
        with open(os.path.join(self.data_root, "CodeLib-Local", "log.txt"), "rt", encoding="utf-8") as f:
            self.allLogs = f.read()
