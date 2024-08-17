import snowflake.snowpark.functions as F
def model(dbt, session):
    dbt.config(materialized = "table")
    df = dbt.ref("raw_customers")

    
    return df