import os
from enum import Enum
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
TRAIN_DIR = os.path.join(CURRENT_DIR, 'hackathon_train')
TEST_DIR = os.path.join(CURRENT_DIR, 'hackathon_test')

BUCKET_NAME = 'hackathon-raw'

class ReportType(str, Enum):
    BALANCE = 'balance'
    INCOME = 'income'
    CASH_FLOW = 'cashflow'

    def __str__(self):
        return self.value

    @property
    def filename_prefix(self):
        return f'df_{self.value}'
