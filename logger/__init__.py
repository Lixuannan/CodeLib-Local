import logging


class Logger:
    def __init__(self):
        open("log.txt", "w")

        self.logger = logging.getLogger("CodeLib-Local Logger")

        self.format = "[%(asctime)s - %(levelname)s]  %(message)s"

        self.file_handler = logging.FileHandler("log.txt", encoding='utf-8')
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
        with open("log.txt", "rt") as f:
            self.allLogs = f.read()
