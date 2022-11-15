import logging


def create_logger():
    """
    создает и настраивает логгер
    """

    # Создание логгера
    logger = logging.getLogger("api")
    logger.setLevel("INFO")

    # Добавление обработчика – ошибки отображаются в консоле
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    # Добавление обработчика – ошибки записываются в файл
    file_handler = logging.FileHandler("logs/api.log", encoding='UTF-8')
    logger.addHandler(file_handler)

    # Создание форматтера и настройка вывода для обработчиков
    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)


def logger_viewers():
    """
    Logger для main.views
    """

    logger = logging.getLogger("main")
    logger.setLevel("INFO")

    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("logs/log.ini", encoding='UTF-8')
    logger.addHandler(file_handler)

    formatter_one = logging.Formatter("%(asctime)s : %(levelname)s :%(message)s")
    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)


