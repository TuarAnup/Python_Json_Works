import json
import pandas as pd
import numpy as np
import os

with open('loans.json') as f:
    data = json.load(f)
    df = pd.DataFrame(data)

def Calculations(df):
    Output = {'LoanAmountSummary':{},'SubjectAppraisedAmountSummary':{},'InterestRateSummary':{}}
    for cols in ['LoanAmount','SubjectAppraisedAmount','InterestRate']:
        colm = cols+'Summary'
        Output[colm]['Sum']=np.sum(df[cols])
        Output[colm]['Average']=np.mean(df[cols])
        Output[colm]['Median']=np.median(df[cols])
        Output[colm]['Minimun']=np.min(df[cols])
        Output[colm]['Maximum']=np.max(df[cols])
    
    return Output
# Calculations(df)
 ##Task 1
# monthlySummary=Calculations(df)
# with open("monthlySummary.json", "w") as outfile: 
#     json.dump(monthlySummary, outfile)
    
    
# ##Task2
gb=df.groupby(['SubjectState'])
# print((gb.groups.keys()))
monthlyByState = dict.fromkeys(gb.groups.keys())
# print(monthlyByState)
for state in gb.groups.keys():
    # print(state)
    
    tmp = gb.get_group(state).reset_index(drop=True)
    #print(tmp)
    state_output = Calculations(tmp)
    monthlyByState[state]=state_output
    
#  print(monthlyByState)
with open("monthlyByState.json", "w") as outfile: 
    json.dump(monthlyByState, outfile)
    
    