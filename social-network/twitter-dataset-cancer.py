import requests
import os
import json
import csv
# For parsing the dates received from twitter in readable formats
import dateutil.parser

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")
max_results = 100

#change params based on the endpoint you are using
query_params = {    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'author_id,text,created_at,lang,public_metrics',
                    'user.fields': '',
                    'place.fields': '',
                    'next_token': {}}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


user_ids = [1395675441671856131,229396042,4898287630,516608579]

for user_id in user_ids:

    user_timeline_url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)

    json_response = connect_to_endpoint(user_timeline_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))

    #guardar los datos en un CSV

    # Create file
    csvFile = open(str(user_id)+".csv", "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    #Create headers for the data you want to save, in this example, we only want save these columns in our dataset
    csvWriter.writerow(["author_id", "created_at", "lang", "like_count", "quote_count", "reply_count", "retweet_count", "text"])
    csvFile.close()

    def append_to_csv(json_response, fileName):

        #A counter variable
        counter = 0

        #Open OR create the target CSV file
        csvFile = open(fileName, "a", newline="", encoding='utf-8')
        csvWriter = csv.writer(csvFile)

        #Loop through each tweet
        for tweet in json_response['data']:
            
            # We will create a variable for each since some of the keys might not exist for some tweets
            # So we will account for that

            # 1. Author ID
            author_id = tweet['author_id']
    

            # 2. Time created
            created_at = dateutil.parser.parse(tweet['created_at'])

            # 3. Language
            lang = tweet['lang']

            # 4. Tweet metrics
            retweet_count = tweet['public_metrics']['retweet_count']
            reply_count = tweet['public_metrics']['reply_count']
            like_count = tweet['public_metrics']['like_count']
            quote_count = tweet['public_metrics']['quote_count']

            # 5. Tweet text
            text = tweet['text']
            
            # Assemble all data in a list
            res = [author_id, created_at, lang, like_count, quote_count, reply_count, retweet_count, text]
            
            # Append the result to the CSV file
            csvWriter.writerow(res)
            counter += 1

        # When done, close the CSV file
        csvFile.close()

    # llamar la función para añadir lineas al archivo CSV
    append_to_csv(json_response, str(user_id)+".csv")