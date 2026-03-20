import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, encoding='latin1')


def check_missing_values(df):
    print("\n🔹 Missing Values:")
    print(df.isnull().sum())


def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"\n🔹 Duplicates Removed: {before - after}")
    return df


def convert_data_types(df):
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df


def feature_engineering(df):
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Year'] = df['Order Date'].dt.year
    df['Profit Margin'] = df['Profit'] / df['Sales']
    df['Profit Margin'] = df['Profit Margin'].fillna(0)
    return df


def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\n✅ Cleaned data saved to {output_path}")


if __name__ == "__main__":
    input_path = "../data/raw_sales_data.csv"
    output_path = "../data/clean_sales_data.csv"

    df = load_data(input_path)

    check_missing_values(df)

    df = remove_duplicates(df)

    df = convert_data_types(df)

    df = feature_engineering(df)

    save_clean_data(df, output_path)