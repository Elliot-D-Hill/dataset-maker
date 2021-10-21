import pandas as pd


class DatasetMaker:

    def __init__(self, raw_path, processed_path):
        self.raw_path = raw_path
        self.processed_path = processed_path

    def get_dataframe(self):
        return read_dataframe(self.raw_path)

    def filter_dataframe(self, df):
        return df

    def format_dataframe(self, df):
        return df

    def transform_dataframe(self, df):
        return df

    def organize_dataframe(self, df):
        return df

    def make_processed_dataset(self):
        (
            self.get_dataframe()
            .pipe(self.format_dataframe)
            .pipe(self.filter_dataframe)
            .pipe(self.transform_dataframe)
            .pipe(self.organize_dataframe)
            .to_csv(self.processed_path, index=False)
        )


def read_dataframe(filepath):
    extension = str(filepath).split('.')[-1]
    if extension == 'tsv':
        return pd.read_csv(filepath, sep='\t')
    elif extension == 'csv':
        return pd.read_csv(filepath, sep=',')
