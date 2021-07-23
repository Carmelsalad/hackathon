import os
import random

import numpy as np
import pandas as pd
import shortuuid

from constants import ReportType, TEST_DIR, TRAIN_DIR
from hackathon_randomize import find_sf, round_sf, match_dtype


class Generator:
    def __init__(self, anomaly_prob):
        self._anomaly_prob = anomaly_prob

    def _is_anomaly(self) -> bool:
        return random.uniform(0, 1) < self._anomaly_prob

    def _get_df(self, filename: str, is_long: bool) -> pd.DataFrame:
        test_df = pd.read_csv(os.path.join(TEST_DIR, filename))
        if not is_long:  # test data
            df = test_df
        else:  # get last 10% - 40% of train data and append test data afterwards
            train_df = pd.read_csv(os.path.join(TRAIN_DIR, filename))
            train_count = len(train_df.index)
            train_extract_count = int(train_count * random.uniform(0.1, 0.4))
            extracted_df = train_df.tail(train_extract_count)
            df = extracted_df.append(test_df)

        return df

    def _generate_anomalous_value(self, value):
        weight = random.randint(50, 100)

        if random.uniform(0, 1) < 0.5:
            fake_value = value / weight
        else:
            fake_value = value * weight
        this_sf = find_sf(value)
        fake_value_rounded = round_sf(fake_value, this_sf)
        return match_dtype(value, fake_value_rounded)

    def _generate_anomaly(self, df: pd.DataFrame) -> pd.DataFrame:
        anomalous_row_count = max(1, int(len(df.index) * random.uniform(0, 0.1)))
        # Randomly get row indices to generate anomaly
        anomalous_row_indices = random.sample(range(len(df.index)), anomalous_row_count)

        untouched_col_names = ['SimFinId', 'Year', 'Date']
        changeable_cols = []
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            changeable = True
            for untouched in untouched_col_names:
                if col.find(untouched) != -1:
                    changeable = False
                    break

            if changeable:
                changeable_cols.append(col)

        for index in anomalous_row_indices:
            random.shuffle(changeable_cols)
            for col in changeable_cols:
                # Assume there is at least one non-null numeric value to
                # convert to anomaly
                if np.isnan(df.at[index, col]):
                    continue

                df.at[index, col] = self._generate_anomalous_value(df.at[index, col])
                break

        return df

    def generate_report(self, ticker: str, rp_type: ReportType, is_long: bool) -> (str, pd.DataFrame):
        origin_filename = f'{rp_type.filename_prefix}_{ticker}'
        origin_filename_ext = origin_filename + '.csv'
        df = self._get_df(origin_filename_ext, is_long)

        uid = shortuuid.uuid()
        filename = f'{origin_filename}_{str(uid)}'

        if self._is_anomaly():
            filename += '_anomalous.csv'
            df = self._generate_anomaly(df)
        else:
            filename += '.csv'

        return filename, df
