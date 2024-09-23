# from ComplaintClassification.components.DataVisualizationComponentes import DataVisualizationComponentes
# from ComplaintClassification.services.DataIngestionFileFactoryServices import DataIngestionFileFactoryServices

# class DataIngestionFacadeComponentes:
#     def __init__(self):
#         self.dataIngestionFileFactoryServices = DataIngestionFileFactoryServices()
#         self.dataVisualizationComponentes= DataVisualizationComponentes()
    

#     def extract_data(self,source_type,loader_type):
#         if source_type == 'database':
#             pass
#         elif source_type == 'api':
#             pass
#         elif source_type == 'file':
#             data=self.dataIngestionFileFactoryServices.extract_data(loader_type)
#             data= DataIngestionFacadeComponentes.clean_data(data)
#             # self.dataVisualizationComponentes.draw_bar_plot(data)
#             # self.dataVisualizationComponentes.draw_word_cloud(data)

#             return str(len(data))
#         else:
#             raise ValueError("Invalid source type")
#         pass
    
#     def clean_data(data):
#         print('Original rows:'+str(str(len(data))))
#         # Check for missing values
#         if data.isnull().sum().any():
#             print('Drop rows with any missing values')
#             # data.fillna(data.mean(), inplace=True)
#             # data_filled_median = data.fillna(data.median())
#             # data_filled_zero = data.fillna(0)
#             data = data.dropna()
#             # data = data.dropna(axis=1)
#             print('After Drop rows with any missing values rows:'+str(len(data)))
#         # Check for duplicate rows
#         if data.duplicated().sum().any():
#             data = data.drop_duplicates()
#             print('After Drop duplicate rows:'+str(len(data)))    
        
#         # Check for unrealistic values/ Validate Value Ranges
#         # print(data[data['Number of Bedrooms'] <= 0])
#         # print(data[data['Age of House'] < 0])
#         # print(data[data['Price'] <= 0])
#         return data


    

        