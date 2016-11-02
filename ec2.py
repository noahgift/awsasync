"""Generates an Async MetaData call.  Note, this isn't available in Boto3

In [56]: res = all_metadata_async()

In [57]: res
Out[57]: 
[('ami-manifest-path', <Response [200]>),
 ('instance-type', <Response [200]>),
 ('instance-id', <Response [200]>),
 ('iam', <Response [200]>),
 ('local-hostname', <Response [200]>),
 ('network', <Response [200]>),
 ('hostname', <Response [200]>),
 ('ami-id', <Response [200]>),
 ('instance-action', <Response [200]>),
 ('profile', <Response [200]>),
 ('reservation-id', <Response [200]>),
 ('security-groups', <Response [200]>),
 ('metrics', <Response [200]>),
 ('mac', <Response [200]>),
 ('public-ipv4', <Response [200]>),
 ('services', <Response [200]>),
 ('local-ipv4', <Response [200]>),
 ('placement', <Response [200]>),
 ('ami-launch-index', <Response [200]>),
 ('public-hostname', <Response [200]>),
 ('public-keys', <Response [200]>),
 ('block-device-mapping', <Response [200]>)]


"""

import requests
import trollius

def get_metadata_api_urls():
    """Retrieves the api endpoints for metadata"""

    full_urls = {}
    metadata_url = "http://169.254.169.254/latest/meta-data/"
    resp = requests.get(metadata_url)
    urls = resp.content.split()
    for url in urls:
        stripped_url = url.rstrip("/")
        full_urls[stripped_url]=(os.path.join(metadata_url, url))
    return full_urls

def _get(key_url):
    key,url = key_url
    return key, requests.get(url)

def _do_calls(urls):
    loop = trollius.get_event_loop()
    futures = []
    for url in urls:
        futures.append(loop.run_in_executor(None, _get, url))
    return futures

@trollius.coroutine
def call():
    results = []
    futures = _do_calls(get_metadata_api_urls().items())
    for future in futures:
        result = yield trollius.From(future)
        results.append(result)
    raise trollius.Return(results)

def all_metadata_async():
    """Retrieves all available metadata for an instance async"""

    loop = trollius.get_event_loop()
    res = loop.run_until_complete(call())
    return res