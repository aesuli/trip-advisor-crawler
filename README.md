# Trip Advisor crawler

This is a simple crawler script for Trip Advisor.

It is aimed at researchers and students that want to experiment with text mining problems on review data.


**usage:** trip-advisor-crawler.py [-h] [-f] [-r MAXRETRIES] [-t TIMEOUT]
                               [-a {Hotel,Restaurant}]
                               [-p PAUSE] [-m MAXREVIEWS] -o OUT
                               ID [ID ...]

## required arguments:

  -o OUT, --out OUT     Output base path

  ID                    IDs for which to download reviews

### ID format:
* *domain:locationcode* e.g. *com:187893* = reviews form any hotel in Tuscany, from the com domain
* *domain:locationcode:citycode* e.g. *jp:187899:187899* = reviews from any hotel in the city of Pisa from the jp domain
* *domain:locationcode:citycode:hotelcode* e.g. *it:187899:187899:662603* = all reviews for a specific hotel from the it domain
* *domain:locationcode:citycode:hotelcode:reviewcode* e.g. *it:187899:187899:662603:322965103* = a single specific review

## optional arguments:

  -h, --help            show help message and exit

  -f, --force           Force download even if already successfully downloaded

  -a {Hotel,Restaurant}, --activity {Hotel,Restaurant}
                        Type of activity to crawl (default: Hotel)

  -r MAXRETRIES, --maxretries MAXRETRIES
                        Max retries to download a file. Default: 3

  -t TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds for http connections. Default: 180

  -p PAUSE, --pause PAUSE
                        Seconds to wait between http requests. Default: 0.2

  -m MAXREVIEWS, --maxreviews MAXREVIEWS
                        Maximum number of reviews per item to download.
                        Default:unlimited
