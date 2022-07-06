#pip install git+https://github.com/Commonists/pageview-api.git
import pageviewapi

result=pageviewapi.per_article('es.wikipedia', 'Joe Biden', '20220701', '20220705',
                        access='all-access', agent='all-agents', granularity='daily')

for item in result.items():
    for article in item[1]:
        timestamp=article['timestamp'][:8] #first 8 digits
        views=article['views']
        print(timestamp)
        print(views)

