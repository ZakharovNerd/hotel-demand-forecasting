import psycopg2

def connect_to_postgres():
    
    conn = psycopg2.connect(
        host="79.174.88.2",
        port="15743",
        database="hotels",
        user="admin",
        password="Pa$$w0rd")

    cursor = conn.cursor()

    import csv

    # Construct the SQL query to unite all tables
    # This is a simplified example and should be modified according to your actual needs

    sql_query = """
    SELECT
        co.date AS order_date,
        co.hotel_id AS hotel_id,
        co.customer_id AS order_customer_id
    FROM
        customers_orders co


    """

    # Use Pandas to execute the query and load the data into a DataFrame
    return pd.read_sql_query(sql_query, conn)