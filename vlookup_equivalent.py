import pandas as pd


def run_main():
    df = pd.DataFrame()
    df['columnA'] = ['disease1', 'disease2', 'disease3']
    df['columnB'] = ['disease4', 'disease6', 'disease5']
    df['participantIds'] = [112, 154, 182]
    df['idsToCheck'] = [182, 112, 154]

    df['columnACheck'] = [df.columnA.iloc[df[df.participantIds == idToCheck].index[0]] for idToCheck in df.idsToCheck.tolist()]
    df['columnBCheck'] = [df.columnB.iloc[df[df.participantIds == idToCheck].index[0]] for idToCheck in df.idsToCheck.tolist()]

    print(df)

if __name__ == '__man__':
    run_main()
