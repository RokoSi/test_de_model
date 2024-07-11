# -*- coding: utf-8 -*-
import logging
import os

from cli import main_menu
from src.ka_ca import get_msg, get_msg_json

from src.settings import settings

log = logging.getLogger(__name__)

log_dir = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)


def main():
    get_msg()
    #get_msg_json()
    main_menu(settings)


if __name__ == "__main__":
    main()
