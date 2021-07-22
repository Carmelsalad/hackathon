import logging
import random
import sys
import time
from io import StringIO

import boto3
import pandas as pd
import schedule
from dotenv import load_dotenv

from constants import ReportType, BUCKET_NAME
from report_generation import Generator

load_dotenv()

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)


class Uploader:
    def __init__(self):
        self._s3 = boto3.resource('s3')

    def upload(self):
        generator = Generator(0.3)
        object_name, df = generator.generate_report(
            self._get_ticker(),
            self._get_report_type(),
            False
        )

        buffer = StringIO()
        df.to_csv(buffer)
        self._s3.Object(BUCKET_NAME, object_name).put(Body=buffer.getvalue())
        logging.info(f"Upload report {object_name} to s3 successfully")

    def _get_report_type(self) -> ReportType:
        return random.choice(list(ReportType))

    def _get_ticker(self) -> str:
        ticker_list = pd.read_csv('df_income_filtered.csv').Ticker.unique()
        return random.choice(ticker_list)


uploader = Uploader()


def upload():
    uploader.upload()


if __name__ == '__main__':
    schedule.every(1).minutes.do(upload)
    logging.info("Starting scheduler")
    while True:
        schedule.run_pending()
        time.sleep(1)
