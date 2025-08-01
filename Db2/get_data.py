# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:26:03 2022

@author: JackCCChang
"""
import pandas as pd
import json
import subprocess 
import datetime






def get_data_db2(sql):
    python32_path = r'D:\Python37-32bit\python'
    script32_path = r'D:\Python37-32bit\Db2\db2.py'
    p = subprocess.Popen([python32_path, script32_path,'--sql',sql],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    p.kill()
    output = json.loads(output)
    data_df = pd.DataFrame(output)
    return data_df


df = get_data_db2(sql)
print(df)
