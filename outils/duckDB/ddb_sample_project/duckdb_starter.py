import duckdb

con = duckdb.connect()

#input
inputfile = ".\\input\\test.csv"

#output
ouputfile = ".\\output\\out.parquet"

#requete simple de lecture de fichier
sql_query = f"""
SELECT *
FROM '{inputfile}'
"""

#creation du fichier parquet
parquet_query = f"""
COPY ({sql_query}) TO '{ouputfile}' (FORMAT PARQUET);
"""

print(con.sql(sql_query).df())

result = con.sql(parquet_query)

print(result)