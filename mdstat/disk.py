# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import


def parse_device_disk(token):
    """Parse a single disk from the header line.

    Each disks has at least a device name and a unique number in its array,
    after that could follow a list of special flags:
        (W)  write-mostly
        (S)  spare disk
        (F)  faulty disk
        (R)  replacement disk
    Some are mutually exclusive (e.g. can't be spare and faulty).

    """
    name, token = token.split("[", 1)
    number, flags = token.split("]", 1)

    return name, {
        "number": int(number),
        "write_mostly": "W" in flags,
        "faulty": "F" in flags,
        "spare": "S" in flags,
        "replacement": "R" in flags,
    }


def parse_device_disks(tokens):
    """Parse the list of disks from the header line."""
    return dict(parse_device_disk(token) for token in tokens)
