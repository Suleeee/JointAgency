# -*- coding: utf-8 -*-
import pandas as pd

dir = './01. Preprocessed_Data'

def ReverseValues(col):
    return 7-col

# 역문항 코딩 
def ReverseCoding():
    df = pd.read_csv(dir + './Main_SPQ.csv')
    targetQ_lst = ['Q7', 'Q8', 'Q11', 'Q12', 'Q17', 'Q18', 'Q21', 'Q22']
    #print(df.loc[:, targetQ_lst])
    df[targetQ_lst] = df[targetQ_lst].apply(ReverseValues)
    #print(df.loc[:, targetQ_lst])
    df.to_csv(dir + './Main_SPQ_reversed.csv', index=False)

def CombineValues():
    df = pd.read_csv(dir + './Main_SPQ_reversed.csv')
    df['SPQ'] = df.loc[:,'Q1':'Q36'].sum(axis=1)
    df['S1_CoPresence'] = df.loc[:,'Q1':'Q6'].sum(axis=1)
    df['S2_Attention'] = df.loc[:,'Q7':'Q12'].sum(axis=1)
    df['S3_Message'] = df.loc[:,'Q13':'Q18'].sum(axis=1)
    df['S4_Affection'] = df.loc[:,'Q19':'Q24'].sum(axis=1)
    df['S5_Emotion'] = df.loc[:,'Q25':'Q30'].sum(axis=1)
    df['S6_Behavior'] = df.loc[:,'Q31':'Q36'].sum(axis=1)
    #df['SectionAverage'] = df.loc[:, ['S1_CoPresence', 'S2_Attention', 'S3_Message', 'S4_Affection', 'S5_Emotion', 'S6_Behavior']].mean(axis=1)
    df['SPQ_SectionAverage'] = df['SPQ'].apply(lambda x : x/6)
    #print(df)
    final_df = df.loc[:, ['ParticipantNumber', 'BlockNumber', 'Condition', 'SPQ', 'S1_CoPresence', 'S2_Attention', 'S3_Message', 'S4_Affection', 'S5_Emotion', 'S6_Behavior', 'SPQ_SectionAverage']]
    #final_df = df.loc[:, ['ParticipantNumber', 'BlockNumber', 'Condition', 'SectionAverage']]
    #print(final_df)
    final_df.to_csv(dir + './Main_SPQ_scoreAdded.csv', index=False)

def PivotResults():
    df = pd.read_csv(dir + './Main_SPQ_scoreAdded.csv')

    #pivot table
    df = df.pivot_table(index='ParticipantNumber', columns='Condition', values=['S1_CoPresence', 'S2_Attention', 'S3_Message', 'S4_Affection', 'S5_Emotion', 'S6_Behavior', 'SPQ_SectionAverage', 'SPQ'])
    #print(df)

    #column reset
    print(df.columns)
    #df.columns = ['SPQ_' + str(col) for col in df.columns]
    df.columns = [str(col[0]) + '_' +  str(col[1]) for col in df.columns]
    print(df.columns)
    #print(df)

    #write to csv
    df.to_csv(dir + "./Main_SPQ_sectionsDivided_pivoted.csv")

def FinalMerged():
    VRQ_df = pd.read_csv(dir + './mergedResult_failExcluded_pivoted.csv')
    SPQ_df = pd.read_csv(dir + './Main_SPQ_sectionsDivided_pivoted.csv')
    final_df = pd.concat([VRQ_df, SPQ_df], axis=1)
    del final_df['ParticipantNumber']
    final_df.rename(columns={'partiNumber' : 'ParticipantNumber', 'competitiveness_0': 'cooperativeness_0', 'competitiveness_1': 'cooperativeness_1', 'competitiveness_10': 'cooperativeness_10', 'competitiveness_11': 'cooperativeness_11'}, inplace=True)
    #print(final_df)
    final_df.to_csv('./Final_merged_v4.csv', index=False)



def main():
    #ReverseCoding()
    #CombineValues()
    #PivotResults()
    FinalMerged()


if __name__ == '__main__':
    main()