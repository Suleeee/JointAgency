# -*- coding: utf-8 -*-
import pandas as pd
import os

dir = './OutputData/'

def pivotResults():
    data = pd.read_csv('./mergedResult.csv')

    #pivot table
    data_partiNum_pivot = data.pivot_table(index='partiNumber', columns='condition', values=['FOC','competitiveness','rewardFairness'], aggfunc='mean')
    #print(data_partiNum_pivot)

    #column reset
    data_partiNum_pivot.columns = [col[0] + '_' + str(col[1]) for col in data_partiNum_pivot.columns]
    #print(data_partiNum_pivot)

    #write to csv
    data_partiNum_pivot.to_csv("./mergedResult_pivoted.csv")


def mergeResults():
    csvFileList = getCsvList(dir)

    participantResult = pd.DataFrame({'A' : []})
    for f in csvFileList:
        data = pd.read_csv(dir + f)
        participantResult = pd.concat([participantResult, data])

    del participantResult['A']

    #participantResult['condition'] = participantResult.apply(conditionColumn, axis='columns')
    participantResult = additionalChanges(participantResult)

    participantResult.to_csv("./mergedResult.csv", header=True, index=False)
    
    print(participantResult)

    return participantResult

def additionalChanges(df):
    df['condition'] = df.apply(conditionColumn, axis='columns')
    #print(df.dtypes)
    #df = df.astype({'condition': str})
    #print(df.dtypes)
    return df

def conditionColumn(x):
    if (x.rewardType == 0) and (x.handShow == 0):
        return "00"
    elif (x.rewardType == 0) and (x.handShow == 1):
        return "01"
    elif (x.rewardType == 1) and (x.handShow == 0):
        return "10"
    elif (x.rewardType == 1) and (x.handShow == 1):
        return "11"


# Read csv File Names
def getCsvList(path_dir):
    file_list = os.listdir(path_dir)
    file_list.sort(key=lambda x: int(x[18:19]))
    csvList = []

    for f in file_list:
        if f.find('.csv') != -1:
            csvList.append(f)

    return csvList


def main():
    #mergeResults()
    #print(mergedResult['playTime'].quantile(q=0.6, interpolation='nearest'))
    pivotResults()


if __name__ == '__main__':
    main()