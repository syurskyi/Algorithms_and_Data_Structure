import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_ServiceIPRange():
    serv = ServiceIPRange(
        service='Tester',
        region='Bolton',
        cidr=IPv4Network('158.152.1.0/24')
    )
    assert str(serv) == '158.152.1.0/24 is allocated to the Tester service in the Bolton region'


def test_parse_ipv4_service_ranges(json_file):
    services = parse_ipv4_service_ranges(json_file)
    assert len(services) == 1886
    assert services[0].region == 'eu-west-1'
    assert services[0].service == 'AMAZON'


def test_get_aws_service_range(json_file):
    services = parse_ipv4_service_ranges(json_file)
    service_range = get_aws_service_range('13.248.118.1', services)
    assert len(service_range) == 2
    assert set(s.region for s in service_range) == {'eu-west-1'}
    assert set(s.service for s in service_range) == {'AMAZON', 'GLOBALACCELERATOR'}
    assert get_aws_service_range('158.152.1.65', services) == []
    with pytest.raises(ValueError) as exc:
        get_aws_service_range('0.0.0.256', services)
    assert 'Address must be a valid IPv4 address' in str(exc.value)
