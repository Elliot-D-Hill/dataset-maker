import pandas as pd


class DatasetMaker:

    def __init__(self, raw_path, processed_path):
        self.raw_path = raw_path
        self.processed_path = processed_path

    def read_dataframe(self):
        extension = str(self.raw_path).split('.')[-1]
        if extension == 'tsv':
            return pd.read_csv(self.raw_path, sep='\t')
        elif extension == 'csv':
            return pd.read_csv(self.raw_path, sep=',')

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
            self.read_dataframe()
            .pipe(self.format_dataframe)
            .pipe(self.filter_dataframe)
            .pipe(self.transform_dataframe)
            .pipe(self.organize_dataframe)
            .to_csv(self.processed_path, index=False)
        )
