import pandas as pd
import os


pathToFileFox = 'C:\\Users\\Schako\\Desktop\\practiceScraper_Scrapy\\testScraper\\testScraper\\data\\foxNews_toFilter.csv'
pathToFileYComb = 'C:\\Users\\Schako\\Desktop\\practiceScraper_Scrapy\\testScraper\\testScraper\\data\\results_ycomb_toFilter.csv'
pathFileToDuckJSON = 'C:\\Users\\Schako\\Desktop\\practiceScraper_Scrapy\\testScraper\\testScraper\\data\\resultsDuckDuck_Alexa.json'


keywords = ['hacking', 'hacked', 'hacks', 'security', 'breach', 'vulnerability', 'vulnerabilities', 'attack', 'voice-squatting', 'voice squatting',
            'masquerading', 'in-communication skill switch', 'skill switch', 'in communication', 'faking', 'faking termination', 'eavesdrop', 'eavesdropping',
            'impersonate', 'impersonation', 'impersonating' ,'adversary', 'skills', 'permission', 'code-manipulation', 'code manipulation', 'stolen', 'steal',
            'stolen', 'stealing', 'listening', 'issue', 'issues', 'review', 'theft', 'thief', 'malicious', 'hidden', 'content-manipulation', 'content manipulation',
            'hide', 'network time protocol', 'NTP', 'simple network time protocol', 'SNTP', 'network-time-protocl', 'spoofing', 'deepfake', 'scam', 'deception',
            'deceptions', 'victim', 'victims', 'fooled', 'consequence', 'consequences', 'data breach', 'compromise', 'compromised', 'spear', 'skill-squatting',
            'skill squatting', 'skill squat', 'skill-squat', 'squattable', 'squatted', 'spyware', 'malware', 'risk', 'security risk', 'firmware', 'loophole', 'backdoor']

google_assistant_keywords = ['google assistant', 'google home', 'google nest', 'nest device', 'voice match', 'smart home google', 'smart home nest', 'virtual assistant', 'smart assistant', 'virtual voice assistant', 'smart voice assistant', 'virtual assistant technology', 'speech synthezizer', 'smart speaker']
alexa_keywords = ['alexa', 'echo dot', 'echo device', 'dot device', 'amazon echo', 'amazon dot', 'smart home alexa', 'smart home echo', 'virtual assistant', 'smart assistant', 'virtual voice assistant', 'smart voice assistant', 'virtual assistant technology', 'speech synthezizer', 'smart speaker']


def filter__csv_file_fox_alexa(file):
    df = pd.read_csv(file)
    
    #filter based on the 'title' column containing "alexa" and any of the keywords
    filter1 = df['title'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)
    #filter based on the 'body' column containing "alexa" and any of the keywords
    filter2 = df['content'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['content'].str.contains('|'.join(keywords), case=False, na=False)
    
    filtered_df1 = df[filter1]
    filtered_df2 = df[filter2]

    #maybe merge instead of concat is better? check later
    filtered_df = pd.concat([filtered_df1, filtered_df2], axis=0)
    filtered_df = filtered_df.reset_index(drop=True)
    
    # Save the filtered data to a new CSV file
    parent_folder = 'filteredData'
    output_file_path = os.path.join(parent_folder, os.path.basename(pathToFileFox).replace('.csv', 'alexa_filtered.csv'))
    filtered_df.to_csv(output_file_path, index=False)
    
    print("Filtered data saved to:", output_file_path)

def filter__csv_file_fox_googleAssistant(file):
    df = pd.read_csv(file)
    
    #filter based on the 'title' column containing "alexa" and any of the keywords
    filter1 = df['title'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)
    #filter based on the 'body' column containing "alexa" and any of the keywords
    filter2 = df['content'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['content'].str.contains('|'.join(keywords), case=False, na=False)
    
    filtered_df1 = df[filter1]
    filtered_df2 = df[filter2]

    #maybe merge instead of concat is better? check later
    filtered_df = pd.concat([filtered_df1, filtered_df2], axis=0)
    filtered_df = filtered_df.reset_index(drop=True)
    
    # Save the filtered data to a new CSV file
    parent_folder = 'filteredData'
    output_file_path = os.path.join(parent_folder, os.path.basename(pathToFileFox).replace('.csv', 'googleAssistatn_filtered.csv'))
    filtered_df.to_csv(output_file_path, index=False)
    
    print("Filtered data saved to:", output_file_path)


def filter_comments_csv_file_ycomb_alexa(file):
    df = pd.read_csv(file)
    filter = df['title'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileYComb)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + 'alexa_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)

def filter_comments_csv_file_ycomb_googleAssistant(file):
    df = pd.read_csv(file)
    filter = df['title'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileYComb)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + 'googleAssistant_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)

def duckJSONtoCSV(file):
    df = pd.read_json(file)

    sub_name = os.path.basename(pathFileToDuckJSON)
    sub_name = sub_name.rstrip('.json')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + 'duckJSON_filtered.csv')
    df.to_csv(output_file_path, index=False)



#duckJSONtoCSV(pathFileToDuckJSON)

#filter__csv_file_fox_alexa(pathToFileFox)
#filter__csv_file_fox_googleAssistant(pathToFileFox)
#filter_comments_csv_file_ycomb_alexa(pathToFileYComb)
#filter_comments_csv_file_ycomb_googleAssistant(pathToFileYComb)