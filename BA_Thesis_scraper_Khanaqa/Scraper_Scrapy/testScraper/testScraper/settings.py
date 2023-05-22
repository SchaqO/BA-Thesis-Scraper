# Scrapy settings for testScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "testScraper"

SPIDER_MODULES = ["testScraper.spiders"]
NEWSPIDER_MODULE = "testScraper.spiders"

#this creates the file automatically of the scraped data without typing it as an argument in the bash
FEEDS = {
    #'booksdata.json': {'format': 'json', 'overwrite': True}
    'data/results.csv': {'format': 'csv', 'overwrite': True}
}

SCRAPEOPS_API_KEY = 'API_KEY'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50

## Insert Your List of Proxies Here
ROTATING_PROXY_LIST = [
    '104.129.192.34:8800',
    '173.230.147.173:19527',
    '182.253.159.19:4145',
]

#the information of the proxy rotating service
PROXY_USER = 'username'
PROXY_PASSWORD = 'password'
PROXY_ENDPOINT = 'gate.smartproxy.com'
PROXY_PORT = '7000'


SCRAPEOPS_PROXY_ENABLED = True
#SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}



#if you have a file with a lot of ips and ports, you can also save it ina file and get the list like shown below from the file, instead of the alternative above
#ROTATING_PROXY_LIST_PATH = '/my/path/proxies.txt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "testScraper (+http://www.yourdomain.com)"

#Set this to false if a site does not allow the ability to scrape or blocks it 
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "testScraper.middlewares.TestscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #"testScraper.middlewares.TestscraperDownloaderMiddleware": 543,
    #"testScraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400,
    "testScraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
    #'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,  #this is only if you manually use proxy addresses
    #'rotating_proxies.middlewares.BanDetectionMiddleware': 620,   #this is only if you manually use proxy addresses
    #'testScraper.middlewares.MyProxyMiddleware': 350, #for the rotating proxy service, if you use it
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400, #for the rotating proxy service, if you use it 
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #"testScraper.pipelines.TestscraperPipeline": 300,
    #"testScraper.pipelines.JsonWriterPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
