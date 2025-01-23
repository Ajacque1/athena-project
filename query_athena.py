from pyathena import connect
import pandas as pd
import boto3

# Athena configuration
region_name = "us-east-1"  # Region
database_name = "test-data-database"
query = "SELECT * FROM test_data_project LIMIT 10;"
s3_staging_dir = "s3://test-data-project-athena-results/"  # Created Directory

# Connect to Athena
print("Connecting to Athena...")
conn = connect(region_name=region_name, s3_staging_dir=s3_staging_dir)

# Run query and get QueryExecutionId
print("Running query...")
cursor = conn.cursor()
cursor.execute(query)
query_execution_id = cursor.query_id

# Print the QueryExecutionId
print(f"Query Execution ID: {query_execution_id}")

# Check the S3 path where the results will be stored
results_s3_path = f"{s3_staging_dir}{query_execution_id}.csv"
print(f"Results will be stored in S3 at: {results_s3_path}")

# Fetch the query results and print them
results = cursor.fetchall()
df = pd.DataFrame(results, columns=["order_id", "customer_name", "amount", "date"])
print("Query Results:")
print(df)
