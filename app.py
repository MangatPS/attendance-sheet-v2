from flask import Flask, render_template,jsonify
app = Flask(__name__)

EMPPLOYEE = [
  {
    'id': 1,
    'Sr. No': '1',
    'Scheme_Name': 'NPV-A1',
    'code': '707',
    'Dept_name': 'Library',
    'Name_Emp': 'Gagandeep Singh',
    'Fathers_Name': 'Rajendra Singh',
    'No. of Days': '27',
  },
  {
    'id': 2,
    'Sr. No': '2',
    'Scheme_Name': 'NPV-A1',
    'code': '707',
    'Dept_name': 'Library',
    'Name_Emp': 'Gagandeep Singh',
    'Fathers_Name': 'Rajendra Singh',
    'No. of Days': '27',
  },
  {
    'id': 3,
    'Sr. No': '3',
    'Scheme_Name': 'NPV-A1',
    'code': '707',
    'Dept_name': 'Library',
    'Name_Emp': 'Gagandeep Singh',
    'Fathers_Name': 'Rajendra Singh',
    'No. of Days': '27',
  },
  {
    'id': 4,
    'Sr. No': '4',
    'Scheme_Name': 'NPV-A1',
    'code': '707',
    'Dept_name': 'Library',
    'Name_Emp': 'Gagandeep Singh',
    'Fathers_Name': 'Rajendra Singh',
    'No. of Days': '27',
  },
  {
    'id': 5,
    'Sr. No': '5',
    'Scheme_Name': 'NPV-A1',
    'code': '707',
    'Dept_name': 'Library',
    'Name_Emp': 'Gagandeep Singh',
    'Fathers_Name': 'Rajendra Singh',
    'No. of Days': '27',
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           employee=EMPPLOYEE,
                           Dept_name='Library',)

@app.route("/api/employee")
def list_employee():
  return jsonify(EMPPLOYEE)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True, port=8080)