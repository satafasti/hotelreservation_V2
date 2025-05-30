import os
import shutil
import pandas as pd
import model
import data_access
import business_logic
import sqlite3
from contextlib import closing

db_path = "./database/hotel_reservation_sample.db"
working_db = "./database/working.db"

shutil.copyfile(db_path, working_db)

os.environ["DB_FILE"] = working_db