import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dir = './01. Preprocessed_Data/'
data = pd.read_csv(dir + 'mergedResult_failExcluded.csv')
data_final = pd.read_csv(dir + 'mergedResult_failExcluded_differenceAdded.csv')
dir_final = dir + 'mergedResult_failExcluded_differenceAdded.csv'


def conditionPivoted(reward, hand):
    factor = []
    if(reward == True) & (hand == True):
        factor = ['rewardType', 'handShow']
    elif(reward == True) & (hand == False):
        factor = ['rewardType']
    elif(reward == False) & (hand == True):
        factor = ['handShow']
    else:
        return

    factor_pivoted = data_final.groupby(factor, as_index=False).agg(['mean', 'count', 'sum'])
    return factor_pivoted


def condition_calc(column, calc):
    print('\n======  ' + str(column) + '  ========\n')
    data_cp = conditionPivoted(True, False)
    print(data_cp[column][calc])
    print('\n')
    data_cp = conditionPivoted(False, True)
    print(data_cp[column][calc])
    print('\n')
    data_cp = conditionPivoted(True, True)
    print(data_cp[column][calc])

    return data_cp[column][calc]

def realDifferenceCalc(x):
    return abs(x.P1_realPoints - x.P2_realPoints)

def earnedDifferenceCalc(x):
    return abs(x.P1_earnedPoints - x.P2_earnedPoints)

def PointsDifference():
    data['realDifference'] = data.apply(realDifferenceCalc, axis='columns')
    data['earnedDifference'] = data.apply(earnedDifferenceCalc, axis='columns')
    #column names: P1_realPoints,P2_realPoints,P1_earnedPoints,P2_earnedPoints
    print(data)
    data.to_csv(dir + 'mergedResult_failExcluded_differenceAdded.csv', header=True, index=False)

def disPlot():
    #sns.lmplot(data=data_final, x='earnedDifference', y='FOC', hue='stalemate')
    sns.lmplot(data=data_final, x='earnedDifference', y='FOC')
    plt.show()
    #print('hello')

def main():
    #conditionPivoted()
    #playTime()
    #stalemate()s

    stalemate_df = condition_calc('stalemate', 'count')
    stalemate_df.plot.bar()
    plt.show()
    #stalemate_df.to_csv(dir + 'stalemate_calc.csv', header=True, index=True)
    
    #condition_calc('playTime', 'mean')

    #condition_calc('earnedDifference', 'sum')
    #PointsDifference()

    #print(data_final.columns)
    #disPlot()
    


if __name__ == '__main__':
    main()