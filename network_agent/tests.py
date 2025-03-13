import subprocess
import socket
import time
import requests
import logger as lg
import pandas as pd

logger = lg.get_logger(filename=__name__)


def ping(host="8.8.8.8", count=4):
    logger.info(f"[Test, Ping]: Executing the 'Ping' test ...")
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), host], capture_output=True, text=True
        ).stdout
        return result.split("/")[-3]
    except Exception as ex:
        logger.error(f"[Test, Ping]: Exception received: {ex}")
        return str(ex)


def dns_lookup(domain="google.com"):
    logger.info(f"[Test, DNS Lookup]: Executing the 'DNS Lookup' test ...")
    start = time.time()
    try:
        socket.gethostbyname(domain)
        return round(time.time() - start, 4)
    except Exception as ex:
        logger.error(f"[Test, DNS Lookup]: Exception received: {ex}")
        return str(ex)


def http_latency(url="https://www.google.com"):
    logger.info(f"[Test, HTTP Latency]: Executing the 'HTTP Latency' test ...")
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        return round(time.time() - start, 4) if response.ok else None
    except Exception as ex:
        logger.error(f"[Test, HTTP Latency]: Exception received: {ex}")
        return str(ex)


def get_tests():
    return {
        "ping": {
            "method": ping,
            "display_name": "Ping",
        },
        "dns_lookup_time": {
            "method": dns_lookup,
            "display_name": "DNS Lookup Time",
        },
        "http_latency": {
            "method": http_latency,
            "display_name": "HTTP Latency",
        },
    }


def normalize_df(dataframe: pd.DataFrame):
    tests = get_tests()
    for v in tests.values():
        display_name: str = v["display_name"]
        numerator = dataframe[display_name] - dataframe[display_name].min()
        denominator = dataframe[display_name].max() - dataframe[display_name].min()
        dataframe[display_name] = numerator / denominator
    return dataframe
