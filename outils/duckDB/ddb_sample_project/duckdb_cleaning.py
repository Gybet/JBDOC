import duckdb

con = duckdb.connect()

#input
inputfile = ".\\input\\test.csv"

#output
ouputfile = ".\\output\\out_cleaned.parquet"

#requete simple de lecture de fichier
sql_query_raw = f"""
SELECT *
FROM '{inputfile}'
"""

sql_query_cleaned = f"""
SELECT id, 
        cast(coalesce(valint, 0) as integer ) as valint,  -- remplace les valeurs nulles par 0
        cast(valdate as date) as valdate,                 -- convertit les valeurs en date
        cast(valbool as boolean) as valbool,              -- convertit les valeurs en boolean
FROM '{inputfile}'
"""

#creation du fichier parquet
parquet_query = f"""
COPY ({sql_query_cleaned}) TO '{ouputfile}' (FORMAT PARQUET);
"""

print(con.sql(sql_query_raw))
print(con.sql(sql_query_cleaned))

result = con.sql(parquet_query)

print(result)