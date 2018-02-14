from falsy.jlog.jlog import JLog
import requests
#import urllib2
#import untangle
#import re

log = JLog().bind()

#def get_it(name):
#    log.debug('get it')

def get_it(name):
    return {
        'get': name
    }

def get(name):
    print("hello world!")


    url = 'http://httpbin.org/get'

    #url4 = 'http://142.133.174.149:8888/AfgIotTestSuites.TestSuiteAfgIotEnafPsk?suite'
    r = requests.get(url)
    data = r.text

    # f = open('Test_logs.xml', 'w') # in string-format
    # f.write(data)
    # f.close()

    return data


def post_it(name):
    log.debug('post it')
    return {
        'post': name
    }
