# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

from .disk import parse_device_disks


def parse_device_header(line):
    tokens = line.split()

    name = tokens.pop(0)

    if not name.startswith("md"):
        raise ValueError("invalid device header line: {}"
                         .format(line))

    if tokens.pop(0) != ":":
        raise ValueError("invalid device header format (missing ':'): {}"
                         .format(line))

    active = (tokens.pop(0) == "active")

    if tokens[0] in ["(read-only)", "(auto-read-only)"]:
        tokens.pop(0)
        read_only = True
    else:
        read_only = False

    if "[" not in tokens[0]:
        personality = tokens.pop(0)
    else:
        personality = None

    return name, {
        "active": active,
        "read_only": read_only,
        "personality": personality,
        "disks": parse_device_disks(tokens),
    }
