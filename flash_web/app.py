import csv

from flask import Flask, request,send_from_directory, render_template
import searchJob as s
from openpyxl import load_workbook
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def firstPage():
    if request.method == 'GET':
        return render_template('firstpage.html')
    elif request.method == 'POST':
        jobname = request.form.get('jobname')
        return render_template('firstpage.html', jobname=jobname, requestMethod='POST')

@app.route('/search_result', methods=['POST'])
def search_result():
    jobname = request.form.get('jobname')
    page = int(request.form.get('page'))
    s.search(jobname,page)
    with open('./return_result.csv','r',encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        data = [row for row in rows]
    return render_template('table.html', rows=data)

@app.route('/count')
def count():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)