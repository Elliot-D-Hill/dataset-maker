from pandas import read_csv


class DatasetMaker:

    def filter_dataframe(self, df):
        return df

    def format_dataframe(self, df):
        return df

    def transform_dataframe(self, df):
        return df

    def organize_dataframe(self, df):
        return df

    def make_dataset(self, df):
        return (df
                .pipe(self.format_dataframe)
                .pipe(self.filter_dataframe)
                .pipe(self.transform_dataframe)
                .pipe(self.organize_dataframe)
                )


def read_dataframe(filepath):
    extension = str(filepath).split('.')[-1]
    if extension == 'tsv':
        return read_csv(filepath, sep='\t')
    elif extension == 'csv':
        return read_csv(filepath, sep=',')
