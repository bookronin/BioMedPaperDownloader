# you need to install Biopython:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

from Bio import Entrez
import pprint

import DownloadPaper


def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='10000',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    results = search('Chang , Cheng-Chi')
    #print results
    id_list = results['IdList']
    #print id_list
    papers = fetch_details(id_list)
 
    
    print "=========================="
    # The following are script for fetching the DOI location and article information.
    # Some article may not have a DOI therefore it will be need a "exception handling"
    # in fetching DOI part

    for i, paper in enumerate(papers):
        print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))\
        #print "Article Information : " + paper["MedlineCitation"]["Article"]
        if len(paper["MedlineCitation"]["Article"]['ELocationID']) != 0:
            article_title = paper['MedlineCitation']['Article']['ArticleTitle']
            article_doi = paper["MedlineCitation"]["Article"]['ELocationID'][0]
            print "DOI : " + article_doi 
            articleobject = DownloadPaper.GetArticlesFromLibGen(article_doi,article_title)
            articleobject.DownloadTheArticle()
            print "Completed!"

    # Pretty print the first paper in full
    # import json
    # print(json.dumps(papers[0], indent=2, separators=(',', ':')))