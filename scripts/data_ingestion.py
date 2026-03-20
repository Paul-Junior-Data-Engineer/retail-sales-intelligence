import pandas as pd


def load_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


def inspect_data(df):
    print("\n🔹 Dataset Shape:")
    print(df.shape)

    print("\n🔹 Columns:")
    print(df.columns.tolist())

    print("\n🔹 Data Types:")
    print(df.dtypes)

    print("\n🔹 First 5 Rows:")
    print(df.head())


if __name__ == "__main__":
    file_path = "../data/raw_sales_data.csv"

    df = load_data(file_path)

    if df is not None:
        inspect_data(df)