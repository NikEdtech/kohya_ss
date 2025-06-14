import os
import logging
import time
import sys

from rich.theme import Theme
from rich.logging import RichHandler
from rich.console import Console
from rich.pretty import install as pretty_install
from rich.traceback import install as traceback_install

log = None


def setup_logging(clean=False, debug=False):
    global log

    if log is not None:
        return log

    # безопасный путь для логов
    log_file = "/tmp/kohya_setup.log"

    try:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        if clean and os.path.isfile(log_file):
            os.remove(log_file)
        time.sleep(0.1)  # prevent race condition
    except Exception as e:
        print(f"Log setup warning: {e}")

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(pathname)s | %(message)s",
        filename=log_file,
        filemode="a",
        encoding="utf-8",
        force=True,
    )

    console = Console(
        log_time=True,
        log_time_format="%H:%M:%S-%f",
        theme=Theme(
            {
                "traceback.border": "black",
                "traceback.border.syntax_error": "black",
                "inspect.value.border": "black",
            }
        ),
    )
    pretty_install(console=console)
    traceback_install(
        console=console,
        extra_lines=1,
        width=console.width,
        word_wrap=False,
        indent_guides=False,
        suppress=[],
    )
    rh = RichHandler(
        show_time=True,
        omit_repeated_times=False,
        show_level=True,
        show_path=False,
        markup=False,
        rich_tracebacks=True,
        log_time_format="%H:%M:%S-%f",
        level=logging.DEBUG if debug else logging.INFO,
        console=console,
    )
    rh.set_name(logging.DEBUG if debug else logging.INFO)
    log = logging.getLogger("sd")
    log.addHandler(rh)

    return log
