import json
from contextlib import suppress
from dataclasses import dataclass
from ipaddress import AddressValueError, IPv4Address, IPv4Network
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class ServiceIPRange:
    """
    Represents an IPv4 public network range, allocated by AWS for use with
    a specific service and region.
    """

    service: str
    region: str
    cidr: IPv4Network

    def __str__(self):
        return (f"{self.cidr} is allocated to the {self.service} "
                f"service in the {self.region} region")


def parse_ipv4_service_ranges(source: Path) -> List[ServiceIPRange]:
    """
    Given a JSON file containing AWS public IP addresses, return a list of
    ServiceIPRange objects representing all IPv4 network ranges. See also:

    https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
    """
    data = json.loads(source.read_text())
    with suppress(AddressValueError):
        prefixes = data["prefixes"]
        ipv4_service_ranges = [
            ServiceIPRange(
                service=prefix["service"],
                region=prefix["region"],
                cidr=IPv4Network(prefix["ip_prefix"]),
            )
            for prefix in prefixes
        ]
    return ipv4_service_ranges


def get_aws_service_range(address: str,
                          service_ranges: list) -> List[ServiceIPRange]:
    """
    Return a list of ServiceIPRange objects representing all AWS public
    IP ranges that contain `address`. Raise a ValueError if `address`
    is not a valid IPv4 address.
    """
    try:
        ipv4_address = IPv4Address(address)
    except AddressValueError:
        raise ValueError("Address must be a valid IPv4 address")

    return [range_ for range_ in service_ranges
            if ipv4_address in range_.cidr]