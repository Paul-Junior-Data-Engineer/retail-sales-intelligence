import pandas as pd
import mysql.connector


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


def connect_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",   # 🔁 replace this
            database="retail_sales"
        )
        print("✅ Connected to MySQL")
        return conn
    except Exception as e:
        print("❌ Database connection error:", e)
        return None


def preprocess_data(df):
    # 🔥 FIXED: Handle both spaces AND hyphens
    df.columns = [col.lower().replace(" ", "_").replace("-", "_") for col in df.columns]

    print("\n🔹 Columns after cleaning:")
    print(df.columns.tolist())

    # Required columns (must match MySQL table)
    columns = [
        'order_id', 'order_date', 'ship_date', 'customer_name', 'segment',
        'country', 'city', 'state', 'region', 'product_name',
        'category', 'sub_category', 'sales', 'quantity',
        'discount', 'profit', 'order_month', 'order_year', 'profit_margin'
    ]

    # 🔥 Safety check
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        print("❌ Missing Columns:", missing_cols)
        exit()

    df = df[columns]

    # Convert date format
    df['order_date'] = pd.to_datetime(df['order_date']).dt.date
    df['ship_date'] = pd.to_datetime(df['ship_date']).dt.date

    # Handle missing values
    df = df.fillna(0)

    return df


def insert_data(df, conn):
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO sales_data (
        order_id, order_date, ship_date, customer_name, segment,
        country, city, state, region, product_name,
        category, sub_category, sales, quantity,
        discount, profit, order_month, order_year, profit_margin
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        data = [tuple(row) for row in df.to_numpy()]
        cursor.executemany(insert_query, data)
        conn.commit()

        print(f"✅ Data inserted successfully ({len(data)} rows)")

    except Exception as e:
        print("❌ Error inserting data:", e)

    finally:
        cursor.close()


def verify_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    result = cursor.fetchone()
    print(f"🔹 Total Records in DB: {result[0]}")
    cursor.close()


if __name__ == "__main__":
    file_path = "../data/clean_sales_data.csv"

    df = load_data(file_path)

    if df is not None:
        df = preprocess_data(df)

        conn = connect_mysql()

        if conn is not None:
            insert_data(df, conn)
            verify_data(conn)
            conn.close()