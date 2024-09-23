

# class CleanupTableData:

#     def __init__(self):
#         pass

#     def drop_missing_value(df):
#         df=df.dropna()
#         return df
    
#     def fill_missing_value_constant(df,constant):
#         df=df.fillna(constant)
#         df.to_csv('fill_missing_value_constant.csv', index=False)
#         return df
    
#     def fill_missing_value_ffill(df):
#         df=df.fillna(method='ffill')
#         df.to_csv('fill_missing_value_ffill.csv', index=False)
#         return df
    
#     def fill_missing_value_bfill(df):
#         df=df.fillna(method='bfill')
#         df.to_csv('fill_missing_value_bfill.csv', index=False)
#         return df
    
#     def fill_missing_value_interpolate(df,interpolate):
#         df=df.interpolate(method=interpolate)
#         df.to_csv('fill_missing_value_interpolate.csv', index=False)
#         return df
    

#     def custom_fill(value):
#         if pd.isnull(value):
#             return 0
#         else:
#             return value
        
#     def fill_missing_value_custom_fill(df):
#         df=  df.applymap(self.custom_fill)
#         df.to_csv('fill_missing_value_custom.csv', index=False)
#         return df    
    

#     def fill_missing_value_mean(df,columnname):
#         df[columnname].fillna(df[columnname].mean(), inplace=True)
#         df.to_csv('fill_missing_value_mean.csv', index=False)
#         return df
    

#     def drop_duplicates_data(df):
#         df = df.drop_duplicates()
#         return df
    
#     def rename_column(df,oldColumnName,NewColumnName):
#         df=df.rename(columns={oldColumnName: NewColumnName}, inplace=True)
#         return df
    

#     def RemoveColumn(df,column):
#         df=df.drop(column,axis=1)
#         return df
    
#     # TODO
#     def QueryDataframColumn(df,columnname,condation):
#         df=df.query(f'columnname == condation')
#         return df