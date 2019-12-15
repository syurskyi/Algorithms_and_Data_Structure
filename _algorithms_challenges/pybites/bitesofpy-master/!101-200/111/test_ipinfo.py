import json
from unittest.mock import patch, Mock

import requests

from Previous.ipinfo import get_ip_country


@patch.object(requests, 'get')
def test_ipinfo_mexican_ip(mockget):
    # hardcoding a requests response
    content = (b'{\n  "ip": "187.190.38.36",\n  "hostname": "domain.net",\n'
               b'  "city": "Mexico City",\n  "region": "Mexico City",\n  '
               b'"country": "MX",\n ' b'"loc": "11.0000,-00.1111",\n  '
               b'"postal": "12345",\n  "org": "some org"\n}')
    mockget.return_value = Mock(content=content,
                                text=content.decode("utf-8"),
                                json=lambda: json.loads(content),
                                status_code=200)
    assert get_ip_country('187.190.38.36') == 'MX'


@patch.object(requests, 'get')
def test_ipinfo_japan_ip(mockget):
    # and another IP in Japan
    content = (b'{\n  "ip": "185.161.200.10",\n  "city": "Tokyo",\n  '
               b'"region": "Tokyo",\n ' b'"country": "JP",\n  "loc": '
               b'"00.1111,11.0000",\n  "postal": "123-4567",\n  '
               b'"org": "some other org"\n}')
    mockget.return_value = Mock(content=content,
                                text=content.decode("utf-8"),
                                json=lambda: json.loads(content),
                                status_code=200)
    assert get_ip_country('185.161.200.10') == 'JP'