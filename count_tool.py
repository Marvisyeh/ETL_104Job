def cal_tool(df):
    import csv
    toolDict = {}
    for row in df['所需工具']:
        rows = row.split('、')
        for item in rows:
            if item in toolDict:
                toolDict[item]+=1
            else:
                toolDict[item]=1
    retool = sorted(toolDict.items(), key=lambda x: x[1], reverse=True)
    li = [list(i) for i in retool]
    print(li)
    with open('./numTool.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(li)

if __name__=='__main__':
    import pandas as pd
    df = pd.read_csv('./re104.csv', lineterminator='\n')
    cal_tool(df)
