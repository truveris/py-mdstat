# Copyright 2015-2016, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

from .disk import parse_device_disks


def parse_device_header(line):
    tokens = line.split()

    name = tokens.pop(0)

    if not name.startswith("md"):
        raise ValueError("invalid device header line: {0}"
                         .format(line))

    if tokens.pop(0) != ":":
        raise ValueError("invalid device header format (missing ':'): {0}"
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

    # If the list of disk is empty, the status line is merged with the header,
    # return it so we can parse it as such.
    if "[" not in tokens[0]:
        status_line = "      0 blocks " + " ".join(tokens)
        disks = {}
    else:
        status_line = None
        disks = parse_device_disks(tokens)

    return name, status_line, {
        "active": active,
        "read_only": read_only,
        "personality": personality,
        "disks": disks,
    }
