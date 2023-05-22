import os
import pandas as pd
import matplotlib.pyplot as plt

folder_path_googleAssistant = 'filteredData/Google_Assistant' 
folder_path_alexa = 'filteredData/Alexa' 
folder_path_all_data = 'totalRawData'


def calculate_total_row_count(folder_path):
    total_length = 0

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):  # Consider only CSV files
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            row_count = len(df)
            total_length += row_count
            print(f"File: {file_name}, Row Count: {row_count}")

    print(f"\n\nTotal Row Count: {total_length}")

    return total_length

    
#calculate_total_row_count(folder_path_alexa)
#calculate_total_row_count(folder_path_googleAssistant)
#calculate_total_row_count(folder_path_all_data)

length_alexa = calculate_total_row_count(folder_path_alexa)
length_googleAssistant = calculate_total_row_count(folder_path_googleAssistant)

def showBarChartReports():
    virtual_assistant = ['Amazon Alexa', 'Google Assistant']
    number_of_reports = [length_alexa, length_googleAssistant]

    plt.bar(virtual_assistant, number_of_reports)
    plt.title('Virtual Assistant Vulnerability and Hacking incident reports')
    plt.xlabel('Smart home assistant')
    plt.ylabel('Number of reports')
    plt.show()

showBarChartReports()