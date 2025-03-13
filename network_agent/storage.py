import csv
from datetime import datetime
import constants
import logger as lg

logger = lg.get_logger(filename=__name__)

datetime.strptime("31/01/22 23:59:59.999999", "%d/%m/%y %H:%M:%S.%f")


def save_results(data: dict):
    with open(constants.NETWORK_AGENT_STATS_FILE, mode="a", newline="") as f:
        row = [v["method"]() for v in data.values()]
        date = datetime.now().strftime("%a %d %b %Y %I:%M:%S %p")
        row.insert(0, str(date))
        csv.writer(f).writerow(row)
