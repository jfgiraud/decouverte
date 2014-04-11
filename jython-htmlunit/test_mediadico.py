# -*- coding: utf-8 -*-

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
        #print(jarpath+jar)
        container = jarpath+jar
        sys.path.append(container)

loadjars()

import java.util.logging.Logger as Logger
import java.util.logging.Level as Level

Logger.getLogger("com.gargoylesoftware").setLevel(Level.OFF);


import com.gargoylesoftware.htmlunit.WebClient as WebClient
webclient = WebClient()   

def get_page(page, url):
    if page is None:
        return webclient.getPage(url)
    else:
        return page.getPage(url)
    
def get_first_by_xpath(page, xpath_fmt, *kargs):
    xpath = xpath_fmt % kargs
    inputs = page.getByXPath(xpath)
    #if not inputs:
    #    raise Exception("L'élément recherché n'a pas été trouvé.")
    return inputs[0]

if __name__ == "__main__":
    page = get_page(None, 'http://www.mediadico.com')
    print(page.asXml())    
    url = get_first_by_xpath(page, "//a[text()='Conjugaisons']/@href")
    page = get_page(page, url)
    print(page.asXml())
