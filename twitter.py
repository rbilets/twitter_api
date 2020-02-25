import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def get_friends_locations(twitter_url, user):
    '''
    Returns list of lists with friends and their twitter locations
    '''

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    url = twurl.augment(twitter_url,
                        {'screen_name': user, 'count': '100'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    return js