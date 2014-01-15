import sys, os
from time import sleep

jarpath = '.' #path the jar files to import
jars = [
    '/htmlunit-2.13/lib/cssparser-0.9.11.jar',
    '/htmlunit-2.13/lib/nekohtml-1.9.19.jar',
    '/htmlunit-2.13/lib/httpmime-4.3.1.jar',
    '/htmlunit-2.13/lib/commons-io-2.4.jar',
    '/htmlunit-2.13/lib/httpcore-4.3.jar',
    '/htmlunit-2.13/lib/xalan-2.7.1.jar',
    '/htmlunit-2.13/lib/xml-apis-1.4.01.jar',
    '/htmlunit-2.13/lib/jetty-io-8.1.12.v20130726.jar',
    '/htmlunit-2.13/lib/commons-lang3-3.1.jar',
    '/htmlunit-2.13/lib/sac-1.3.jar',
    '/htmlunit-2.13/lib/httpclient-4.3.1.jar',
    '/htmlunit-2.13/lib/htmlunit-2.13.jar',
    '/htmlunit-2.13/lib/serializer-2.7.1.jar',
    '/htmlunit-2.13/lib/htmlunit-core-js-2.13.jar',
    '/htmlunit-2.13/lib/jetty-http-8.1.12.v20130726.jar',
    '/htmlunit-2.13/lib/jetty-websocket-8.1.12.v20130726.jar',
    '/htmlunit-2.13/lib/jetty-util-8.1.12.v20130726.jar',
    '/htmlunit-2.13/lib/commons-logging-1.1.3.jar',
    '/htmlunit-2.13/lib/xercesImpl-2.11.0.jar',
    '/htmlunit-2.13/lib/commons-codec-1.8.jar',
    '/htmlunit-2.13/lib/commons-collections-3.2.1.jar'
]

def loadjars(): #appends jars to jython path
    for jar in jars:
        print(jarpath+jar)
        container = jarpath+jar
        sys.path.append(container)

loadjars()

import com.gargoylesoftware.htmlunit.WebClient as WebClient
webclient = WebClient()   

def gotopage():
    print('hello, I will visit Google')
    url = 'http://google.com'
    page = webclient.getPage(url)
    print(page)    

if __name__ == "__main__":
    gotopage()
