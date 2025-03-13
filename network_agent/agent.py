import time
import threading
import tests
import storage
import constants
import logger as lg

logger = lg.get_logger(filename=__name__)
idx: int = 1


def agent_loop():
    global idx
    while True:
        logger.info(f"[Agent Loop, Iteration#{idx + 1}] Executing event loop ...")
        storage.save_results(tests.get_tests())
        time.sleep(constants.INTERVAL)
        idx += 1


def start():
    threading.Thread(target=agent_loop).start()


if __name__ == "__main__":
    start()
