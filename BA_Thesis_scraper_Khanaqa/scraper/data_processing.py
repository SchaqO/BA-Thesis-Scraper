import pandas as pd
import os

pathToFile = 'data\\technology\\technology_subreddit.csv'
pathToFileComments = 'data\\technology\\technology_comments_subreddit.csv'

keywords = ['hacking', 'hacked', 'hacks', 'security', 'breach', 'vulnerability', 'vulnerabilities', 'attack', 'voice-squatting', 'voice squatting',
            'masquerading', 'in-communication skill switch', 'skill switch', 'in communication', 'faking', 'faking termination', 'eavesdrop', 'eavesdropping',
            'impersonate', 'impersonation', 'impersonating' ,'adversary', 'skills', 'permission', 'code-manipulation', 'code manipulation', 'stolen', 'steal',
            'stolen', 'stealing', 'listening', 'issue', 'issues', 'review', 'theft', 'thief', 'malicious', 'hidden', 'content-manipulation', 'content manipulation',
            'hide', 'network time protocol', 'NTP', 'simple network time protocol', 'SNTP', 'network-time-protocl', 'spoofing', 'deepfake', 'scam', 'deception',
            'deceptions', 'victim', 'victims', 'fooled', 'consequence', 'consequences', 'data breach', 'compromise', 'compromised', 'spear', 'skill-squatting',
            'skill squatting', 'skill squat', 'skill-squat', 'squattable', 'squatted', 'spyware', 'malware', 'risk', 'security risk', 'firmware', 'loophole', 'backdoor']

google_assistant_keywords = ['google assistant', 'google home', 'google nest', 'nest device', 'voice match', 'smart home google', 'smart home nest', 'virtual assistant', 'smart assistant', 'virtual voice assistant', 'smart voice assistant', 'virtual assistant technology', 'speech synthezizer', 'smart speaker']
alexa_keywords = ['alexa', 'echo dot', 'echo device', 'dot device', 'amazon echo', 'amazon dot', 'smart home alexa', 'smart home echo', 'virtual assistant', 'smart assistant', 'virtual voice assistant', 'smart voice assistant', 'virtual assistant technology', 'speech synthezizer', 'smart speaker']



#for files that are already within Alexa or Google Assistants scope
def filter_csv_file(file):
    df = pd.read_csv(file)

    filter1 = df['title'].str.contains('|'.join(keywords), case=False, na=False)
    filter2 = df['body'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df1 = df[filter1]
    filtered_df2 = df[filter2]

    #maybe merge instead of concat is better? check later
    filtered_df = pd.concat([filtered_df1, filtered_df2], axis=0)
    filtered_df = filtered_df.reset_index(drop=True)

    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFile)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + '_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


#for files that are already within Alexa or Google Assistants scope
def filter_comments_csv_file(file):
    df = pd.read_csv(file)
    filter = df['comment_body'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileComments)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + '_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


#for files outside of an alexa only scope, to filter for alexa
def filter_csv_file_alexa(file):
    df = pd.read_csv(file)
    
    #filter based on the 'title' column containing "alexa" and any of the keywords
    filter1 = df['title'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)
    #filter based on the 'body' column containing "alexa" and any of the keywords
    filter2 = df['body'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['body'].str.contains('|'.join(keywords), case=False, na=False)
    
    filtered_df1 = df[filter1]
    filtered_df2 = df[filter2]

    #maybe merge instead of concat is better? check later
    filtered_df = pd.concat([filtered_df1, filtered_df2], axis=0)
    filtered_df = filtered_df.reset_index(drop=True)
    
    # Save the filtered data to a new CSV file
    parent_folder = 'filteredData\Alexa'
    output_file_path = os.path.join(parent_folder, os.path.basename(pathToFile).replace('.csv', '_filtered.csv'))
    filtered_df.to_csv(output_file_path, index=False)
    
    print("Filtered data saved to:", output_file_path)

#for files outside of an alexa only scope, to filter for alexa
def filter_comments_csv_file_alexa(file):
    df = pd.read_csv(file)
    filter = df['comment_body'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['comment_body'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileComments)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData\Alexa'

    output_file_path = os.path.join(parent_folder, sub_name + '_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


# For files outside of an google assistants only scope, to filter for google assistants
def filter_csv_file_googleAssistant(file):
    df = pd.read_csv(file)
    
    # Filter based on the 'title' column containing "alexa" and any of the keywords
    filter1 = df['title'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['title'].str.contains('|'.join(keywords), case=False, na=False)
    # Filter based on the 'body' column containing "alexa" and any of the keywords
    filter2 = df['body'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['body'].str.contains('|'.join(keywords), case=False, na=False)
    
    filtered_df1 = df[filter1]
    filtered_df2 = df[filter2]

    #maybe merge instead of concat is better? check later
    filtered_df = pd.concat([filtered_df1, filtered_df2], axis=0)
    filtered_df = filtered_df.reset_index(drop=True)
    
    # save the filtered data to a new CSV file
    parent_folder = 'filteredData\Google_Assistant'
    output_file_path = os.path.join(parent_folder, os.path.basename(pathToFile).replace('.csv', '_filtered.csv'))
    filtered_df.to_csv(output_file_path, index=False)
    
    print("Filtered data saved to:", output_file_path)

#for files outside of an google assistants only scope, to filter for google assistants
def filter_comments_csv_file_googleAssistant(file):
    df = pd.read_csv(file)
    filter = df['comment_body'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['comment_body'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileComments)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData\Google_Assistant'

    output_file_path = os.path.join(parent_folder, sub_name + '_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


def dataSize(pathToFile):
    df = pd.read_csv(pathToFile)
    numLine = len(df)
    print(numLine)


#dataSize(pathToFileComments)

#filter_csv_file(pathToFile)
#filter_comments_csv_file(pathToFileComments)

#filter_csv_file_alexa(pathToFile)
#filter_comments_csv_file_alexa(pathToFileComments)

#filter_csv_file_googleAssistant(pathToFile)
#filter_comments_csv_file_googleAssistant(pathToFileComments)


pathToFileCVE = 'cve\\cve_all.csv'
def filter_cve_vulnerabilities_alexa(file):
    df = pd.read_csv(file)
    filter = df['vulnerabilities'].str.contains('|'.join(alexa_keywords), case=False, na=False) & df['vulnerabilities'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileCVE)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + '_alexa_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


def filter_cve_vulnerabilities_googleAssistant(file):
    df = pd.read_csv(file)
    filter = df['vulnerabilities'].str.contains('|'.join(google_assistant_keywords), case=False, na=False) & df['vulnerabilities'].str.contains('|'.join(keywords), case=False, na=False)

    filtered_df = df[filter]
 
    #dirname = os.path.dirname(pathToFile)
    sub_name = os.path.basename(pathToFileCVE)
    sub_name = sub_name.rstrip('.csv')
    parent_folder = 'filteredData'

    output_file_path = os.path.join(parent_folder, sub_name + '_googleAssistant_filtered.csv')
    filtered_df.to_csv(output_file_path, index=False)

    print("Filtered data saved to:", output_file_path)


filter_cve_vulnerabilities_alexa(pathToFileCVE)
filter_cve_vulnerabilities_googleAssistant(pathToFileCVE)