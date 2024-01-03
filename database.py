from sqlalchemy import create_engine, text

# connnect to database

db_connection_string = "mysql+pymysql://1zxubg2o3g0ma07ksdjv:pscale_pw_Yq3hKU58k1eWkFnJReyryMOhTjHgJQ5qvFWw9FNKUrh@aws.connect.psdb.cloud/attendance?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)


def load_emp_from_db():
  with engine.connect() as conn:
  result = conn.execute(text("select * from employee"))
  EMPLOYEE = []
  for row in result.all():
    EMPLOYEE.append(dict(row))
  return EMPLOYEE