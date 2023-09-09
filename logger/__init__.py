import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("CodeLib-Local Logger")

        self.format = "[%(asctime)s - %(levelname)s]  %(message)s""

        self.file_handler = logging.FileHandler("log.txt")
        self.stream_handler = logging.StreamHandler()
        self.file_handler.setLevel(logging.DEBUG)
        self.stream_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(logging.Formatter(self.format))
        self.stream_handler.setFormatter(logging.Formatter(self.format))

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)
        self.logger.setLevel(logging.DEBUG)

    def show(self):
        ...

    def log(self, class_: str, content: str):
        self.log
