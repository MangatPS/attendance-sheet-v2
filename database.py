from sqlalchemy import create_engine, text

# connnect to database

db_connection_string = "mysql+pymysql://svgnsd00kxpijs5hgw3j:pscale_pw_UUL9rMKaKM7Y6ALnyX8X41RXmyQ05nkJqB04VixbR1D@aws.connect.psdb.cloud/attendance?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

with engine.connect() as conn:
  result = conn.execute(text("select * from employee"))
  #print(result.all())

  result_dicts = []
for row in result.all():
  result_dicts.append(row._asdict())
print(result_dicts)