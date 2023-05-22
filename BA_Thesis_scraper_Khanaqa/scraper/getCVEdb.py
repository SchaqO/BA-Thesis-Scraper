import pandas as pd

def read_json_from_url():
    url_all = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
    df = pd.read_json(url_all)
    df.to_csv('cve/cve_all.csv')
    df.to_json('cve/cve_all.json')


def read_json_from_url_keyword(keyword):
    url_keywords = 'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch='
    df = pd.read_json(url_keywords + keyword)
    df.to_csv('cve/cve_'+ keyword + '.csv')
    df.to_json('cve/cve_'+ keyword + '.json')


keyword = "google+home"

#read_json_from_url()
read_json_from_url_keyword(keyword)
