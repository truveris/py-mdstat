# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import


def group_lines(lines):
    """Split a list of lines using empty lines as separators."""
    groups = []
    group = []

    for line in lines:
        if line.strip() == "":
            groups.append(group[:])
            group = []
            continue
        group.append(line)

    if group:
        groups.append(group[:])

    return groups
