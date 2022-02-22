## 104爬蟲說明

- 輸入職業以及想查詢的頁數，將104人力銀行查詢結果，以EXCEL呈現
- 包含
  - 公司名稱
  - 職缺名稱
  - 工作地點
  - 內容
  - 薪水
  - 連結
  - 擅長工具
  - 工作技能
  - 其他條件
- 最後將擅長工具分別做統計。

## 使用方式
執行 searchJob.py
- 輸入想收尋的職業和頁數
ex:
`search('資料分析師',3)`

- 執行完後檔案會輸出在當前資料夾下
  - for_excel.xlsx
  - return_result.csv


### for_excel.xlsx 以excl表呈現
![](JOB.png)

### 並統計所需技能 return_result.csv
![](COUNT.png)

