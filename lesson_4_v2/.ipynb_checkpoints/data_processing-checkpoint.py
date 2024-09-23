import pandas as pd

class Data_processing:

    @staticmethod
    def DevideToColumns(file_path, sep='\t'):
        df = pd.read_csv(file_path, sep=sep)
        return df

    @staticmethod
    def EmptyData(dataset):
        column_names = dataset.columns.tolist()
        for column in column_names:
            nulls = dataset[column].isnull().sum()
            print(f'в столбце {column} - {nulls} пустых значений')

    @staticmethod
    def RemoveRowsWithMissingValues(dataset):
        return dataset.dropna(inplace=True)
         
    # не используется
    @staticmethod
    def FulFill(dataset):
        column_names = dataset.columns.tolist()
        print('Заменены пустые значения:')
        for column in column_names:
            if dataset[column].dtypes == object:
                top = dataset[column].mode()[0]
                dataset[column].fillna(top, inplace=True)
                print(f'в столбце {column} - мода {top} - категориальное значение')
            else:
                median_value = dataset[column].median()
                dataset[column].fillna(median_value, inplace=True)
                print(f'в столбце {column} - медиана {median_value}')