import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_file="raw_data.csv", output_file="processed_data.csv"):
    df = pd.read_csv(input_file)

    # Handle missing values
    df.fillna(method="ffill", inplace=True)

    # Normalize numerical fields
    scaler = StandardScaler()
    df[["Temperature", "Wind Speed"]] = scaler.fit_transform(df[["Temperature", "Wind Speed"]])

    df.to_csv(output_file, index=False)
    print("Data preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
