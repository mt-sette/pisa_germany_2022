import pandas as pd

def clean_pisa_data(dataframe):
    """Clean PISA dataset by dropping missing values, normalizing columns, and renaming."""
    # Drop rows with any missing values
    dataframe = dataframe.dropna()

    # Drop unnecessary columns
    dataframe = dataframe.drop(columns=["CNT", "Unnamed: 0"])

    # Normalize Language Column: German (148) -> 1, Missing (999) -> 0, Others -> 2
    dataframe["LANGN"] = dataframe["LANGN"].replace({148: 1, 999: 0})
    dataframe["LANGN"] = dataframe["LANGN"].apply(lambda x: 2 if x not in [0, 1] else x)

    # Rename gender column
    dataframe = dataframe.rename(columns={"ST004D01T": "GENDER"})

    return dataframe


df = pd.read_csv("../data/raw/pisa_germany_STU_QQQ.csv")
df_cleaned = clean_pisa_data(df)
df_cleaned.to_csv("../data/clean/pisa_germany_cleaned.csv", index=False)
