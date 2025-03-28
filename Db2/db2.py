# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:51:38 2022

@author: JackCCChang
"""

import pyodbc
import pandas as pd
import argparse
parser = argparse.ArgumentParser(description='db2')
parser.add_argument("--sql",
                    help="sql_input",
                    type=str)
FLAGS = parser.parse_args()
my_sql = FLAGS.sql
cnx = pyodbc.connect(
        'Driver={IBM DB2 ODBC Driver}; '
        'Hostname=10.84.66.214; '
        'Port=21001; '
        'Protocol=TCPIP; '
        'Database=adahs1; '
        'CurrentSchema=schema; '
        'UID=aryrpt; '
        'PWD = aryrpt;'
        )

#cnxn = pyodbc.connect('DSN=ADAHS1;UID=aryrpt;PWD=aryrpt')
df= pd.read_sql(my_sql,cnx)
cnx.close()
df = df.apply(lambda x:x.astype(str))
print(df.to_json())
