from flask import Flask, render_template,jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
  EMPPLOYEE = load_emp_from_db()
    return render_template('home.html', 
                      employee=EMPPLOYEE,
                    dept_name='Library')

@app.route("/api/employee")
def list_employee():
  return jsonify(EMPPLOYEE)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)