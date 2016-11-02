# awsasync
Some Useful AWS Async Code 


Example Usage In Getting EC2 Instance MetaData:

    In [55]: from awsasync import all_metadata_async()

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
