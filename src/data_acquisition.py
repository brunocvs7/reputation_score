# Libs
import twint


# Functions
def get_tweets(query, since, until):
    """Function to get tweets using a query (string with terms) and
       two dates, specifying a range to search .

    Parameters:
    query (string): query with terms to be used in the search.
    since (string): string with the initial date.
    until (string): string with the last date.

    Returns:
    tweet_df (dataframe): A pandas dataframe containing all information about
                          the tweets found with the query and within the range
                          of dates passed.
    """
    c = twint.Config()
    c.Search = query
    c.Since = since
    c.Until = until
    c.Pandas = True
    twint.run.Search(c)
    tweet_df = twint.storage.panda.Tweets_df
    return tweet_df