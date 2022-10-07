import pandas as pd

dir = './01. Preprocessed_Data/'

def FailRate():
    df = pd.read_csv(dir + 'mergedResult.csv')
    condition_pivot = df.pivot_table(index='condition', values='gameClear', aggfunc='sum')
    condition_pivot['FailRate'] = condition_pivot['gameClear'].apply(lambda x : (640-x)/640*100)
    condition_pivot.to_csv("./failRate.csv")
    #print(condition_pivot)

def ExcludeFailTrials():
    df = pd.read_csv(dir + 'mergedResult.csv')
    df_onlySuccess = df.loc[df['gameClear'] == True]
    #print(df_onlySuccess)
    df_onlySuccess.to_csv(dir + 'mergedResult_failExcluded.csv', header=True, index=False)

def PivotResults():
    data = pd.read_csv(dir + './mergedResult_failExcluded.csv')

    #pivot table
    data_partiNum_pivot = data.pivot_table(index='partiNumber', columns='condition', values=['FOC','competitiveness','rewardFairness'], aggfunc='mean')
    #print(data_partiNum_pivot)

    #column reset
    data_partiNum_pivot.columns = [col[0] + '_' + str(col[1]) for col in data_partiNum_pivot.columns]
    #print(data_partiNum_pivot)

    #write to csv
    data_partiNum_pivot.to_csv(dir + "./mergedResult_failExcluded_pivoted.csv")

def main():
    #FailRate()
    ExcludeFailTrials()
    #PivotResults()


if __name__ == '__main__':
    main()