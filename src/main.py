# -*- coding: utf-8 -*-
import logging
import os
import random
import time

from cli import count_user_add_menu
from settings import settings

log_dir = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8",
    level=logging.INFO,
    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
log = logging.getLogger(__name__)


def main():

    i = 0
    while True:
        count_user_add_menu(settings.url, random.randint(1, 3))
        i = i + 1
        log.info(f"Счетчик: {i}")
        time.sleep(5)


if __name__ == "__main__":
    main()
