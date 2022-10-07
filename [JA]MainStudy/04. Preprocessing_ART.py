import pandas as pd

dir = './01. Preprocessed_Data/'
art_dir = './ART_Data/'


def JointAgency():
    df = pd.read_csv(dir + 'mergedResult_failExcluded.csv')
    #print(df.columns)
    jointAgency_df = df[['partiNumber', 'rewardType', 'handShow', 'FOC']]
    #print(jointAgency_df.columns)
    jointAgency_df.rename(columns={'partiNumber' : 'participantNumber', 'FOC' : 'jointAgency'}, inplace=True)
    print(jointAgency_df.columns)
    #print(jointAgency_df)
    #jointAgency_df.to_csv(art_dir + 'jointAgency.csv', header=True, index=False)
    jointAgency_pivoted = jointAgency_df.groupby(['participantNumber', 'rewardType', 'handShow'], as_index=False).mean()
    #print(jointAgency_pivoted)
    jointAgency_pivoted.to_csv(art_dir + 'jointAgency.csv', header=True, index=False)

def PivotResults():
    data = pd.read_csv(art_dir + './jointAgency.art.csv')
    data.rename(columns={'ART(jointAgency) for rewardType' : 'ART_JointAgency_reward', 'ART(jointAgency) for handShow' : 'ART_JointAgency_hand', 'ART(jointAgency) for rewardType*handShow' : 'ART_JointAgency_reward*hand'}, inplace=True)
    #data = data[['participantNumber', 'condition', 'ART_JointAgency']]

    #pivot table
    #data_partiNum_pivot = data.pivot_table(index='participantNumber', columns='condition', values='ART_JointAgency', aggfunc='mean')

    #column reset
    #data_partiNum_pivot.columns = ['ART_JointAgency_' + str(col) for col in data_partiNum_pivot.columns]
    #print(data_partiNum_pivot)

    #write to csv
    #data_partiNum_pivot.to_csv(art_dir + "./jointAgency_art_pivoted.csv")


def main():
    JointAgency()
    #PivotResults()


if __name__ == '__main__':
    main()