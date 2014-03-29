import feedparser
from bs4 import BeautifulSoup
'''
Converts Google News RSS Feeds into the news json format
'''
def get_summary(summary_details):
    '''
    Converts to json and back again to ensure that the json encoding is corrent
    if we just try to load it it will complain.
    '''
    c=json.dumps(summary_details)
    d=json.loads(c)
    return d['value']

def get_num_articles(last_a_tag):
    last_entry_text=last_a_tag.text
    splits=last_entry_text.split(' ')
    return splits[1]

if __name__=="__main__":
    d=feedparser.parse('sample2.rss')
    
    for e in d['entries']:
        soup=BeautifulSoup(get_summary(e['summary_detail']))

        a_tags=soup.find_all('a')
        print e['title'],len(a_tags),get_num_articles(a_tags[len(a_tags)-1])
    '''
    for a in a_tags:
        print a.get('href')
    '''
