import re
import urllib

# Check https://regex101.com/r/A326u1/5 for reference
DOMAIN_FORMAT = re.compile(
    r"(?:^(\w{1,255}):(.{1,255})@|^)"  # http basic authentication [optional]
    r"(?:(?:(?=\S{0,253}(?:$|:))"  # check full domain length to be less than or equal to 253 (starting after http basic auth, stopping before port)
    r"((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"  # check for at least one subdomain (maximum length per subdomain: 63 characters), dashes in between allowed
    r"(?:[a-z0-9]{1,63})))"  # check for top level domain, no dashes allowed
    r"|localhost)"  # accept also "localhost" only
    r"(:\d{1,5})?",  # port [optional]
    re.IGNORECASE
)
SCHEME_FORMAT = re.compile(
    r"^(ws)s?$",  # scheme: http(s) or ftp(s)
    re.IGNORECASE
)


def validate_url(url: str):
    """
    Validates if the passed string is a valid websocket url
    
    :param url: 
    :return: str
    :raise URLParseException
    """
    url: str = url.strip()

    if not url:
        raise URLParseException("No URL specified")

    if len(url) > 2048:
        raise URLParseException("URL exceeds its maximum length of 2048 characters (given length={})".format(len(url)))

    result = urllib.parse.urlparse(url)
    scheme = result.scheme
    domain = result.netloc

    if not scheme:
        raise URLParseException("No URL scheme specified")

    if not re.fullmatch(SCHEME_FORMAT, scheme):
        raise URLParseException("URL scheme must either be http(s) or ftp(s) (given scheme={})".format(scheme))

    if not domain:
        raise URLParseException("No URL domain specified")

    if not re.fullmatch(DOMAIN_FORMAT, domain):
        raise URLParseException("URL domain malformed (domain={})".format(domain))
    return url

class URLParseException(Exception):
    pass
