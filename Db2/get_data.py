# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:26:03 2022

@author: JackCCChang
"""
import pandas as pd
import json
import subprocess 
import datetime

sql = r'''
select *
from db2ap.dtool dtool
'''
tool_start_date= datetime.date.today()
tool_start_date = pd.to_datetime(tool_start_date)
start_date = datetime.datetime(tool_start_date.year,tool_start_date.month,tool_start_date.day,7,30)
end_date = start_date + datetime.timedelta(days=1)
TOOLID_list_all=['AANI10','AANI30','AANI40','AANI50','AANI70','ACAN10','ACAN20','ACLA10','ACLA20','ACLA50',
             'ACLA60','ACLA70','ACLA80','ACLA90','ACLAA0','ACLC20','ACVD10','ACVD20','ACVD30','ACVD40',
             'ACVD50','ACVD60','ACVD70','ACVD80','ACVD90','ACVDA0','ACVDB0','ADCL10','ADEV10','ADEV20',
             'ADEVB0','ADEV40','ADEV50','ADEV60','ADEV70','ADEV80','ADEV90','ADEVA0','AEXB20','AEXP10',
             'AEXP20','AEXP30','AEXP40','AEXP50','AEXP60','AEXP70','AEXP80','AEXP90','AEXPA0','AEXPB0',
             'AEXPC0','AICP10','AICP20','AICP30','ALCV10','ALSM10','ALSR40','ALSR50','AMEL10','AMEL20',
             'AMGI10','AMKL10','AMKL20','AMKL30','AMKL50','AMKL60','AMKL70','AMOT10','AMOV10','AMOV20',
             'AMSH10','AMSH20','AMSH30','AMSH40','AMSP10','AMSR10','AMVI10','AMVI20','AOVN10','APEI20',
             'APEN30','APEP10','ARES10','ARES20','ARES30','ARES40','ARES50','ARES60','ARES70','ARES80',
             'ARES90','ARESA0','ARESB0','ARESC0','ARIE10','ARIE20','ARIE30','ARIE50','ARIE60','ARIE70',
             'ARIE80','ASOR10','ASPT10','ASPT20','ASPT30','ASPT40','ASPT50','ASPT60','ASPT70','ASPT80',
             'ASPT90','ASPTA0','ASPTB0','AST010','AST020','AST030','AST040','AST050','ASTA10','ASTA20',
             'ASTA30','ATARB0','ATARC0','ATTG20','ATTG30','AWIT20','AWIT30','AWMA20','AWMA40','AWMA50',
             'AWSN10','AWSN20','SA0010','SA0020','SA0030','SA0040','SA0050','SA0060','SA0070','SA0080',
             'SA0090','SA0100','SA0110','SA0120','SA0130','SA0140','SAC000']
sql2 = '''
SELECT TOOLID,TOOLNAME,TOOLSTAT ,TIMESTAMP(STCLDATE,STTIME) as STARTTIME,TIMESTAMP(CMCLDATE,CMTIME) as ENDTIME
FROM ADAHS1.MCLDHIS 
WHERE TIMESTAMP(STCLDATE,STTIME) BETWEEN '{start_date}' AND '{end_date}' 
AND TIMESTAMP(CMCLDATE,CMTIME) BETWEEN '{start_date}' AND '{end_date}' 
AND TOOLID IN {toolid}
ORDER BY TOOLID,TOOLNAME,STCLDATE,STTIME
'''.format(start_date = start_date,end_date = end_date,toolid = tuple(TOOLID_list_all) )




def get_data_db2(sql):
    python32_path = r'D:\Python37-32bit\python'
    script32_path = r'D:\Python37-32bit\Db2\db2.py'
    p = subprocess.Popen([python32_path, script32_path,'--sql',sql],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    p.kill()
    output = json.loads(output)
    data_df = pd.DataFrame(output)
    return data_df


df = get_data_db2(sql2)
print(df)
