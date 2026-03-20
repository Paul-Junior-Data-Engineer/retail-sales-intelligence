import pandas as pd

def validate_clean_data(file_path):
    df = pd.read_csv(file_path)

    print("✅ Data Loaded Successfully\n")

    print("🔹 Shape of Dataset:")
    print(df.shape)

    print("\n🔹 Columns:")
    print(df.columns.tolist())

    print("\n🔹 Data Types:")
    print(df.dtypes)

    print("\n🔹 First 5 Rows:")
    print(df.head())

    print("\n🔹 Missing Values:")
    print(df.isnull().sum())

    print("\n🔹 Sample Data:")
    print(df.sample(5))


if __name__ == "__main__":
    file_path = "../data/clean_sales_data.csv"
    validate_clean_data(file_path)