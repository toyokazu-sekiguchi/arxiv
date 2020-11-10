import arxiv

id_list = ['1908.03013']
#author_name = 'KAGRA Collaboration' 
author_name = 'T. Sekiguchi'

l = arxiv.query(id_list=id_list)
authors = l[0]['authors']
offset = (0 if('Collaboration' in authors[0]) else 1)
n = len(authors)-1+offset
print('The total number of authors is {}'.format(n))
try:
    i = authors.index(author_name)+offset
    print('The index of {} is {}'.format(author_name,i))
except:
    print('{} is not found in author list'.format(author_name))
