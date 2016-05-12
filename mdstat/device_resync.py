# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import


def parse_device_resync_progress(line):
    tokens = line.split()[1:]

    operation = tokens.pop(0)

    if tokens.pop(0) != "=":
        raise ValueError("invalid resync line (missing '='): {0}"
                         .format(line))

    progress = tokens.pop(0)
    counts = tokens.pop(0)[1:-1].split("/", 1)
    resynced = int(counts[0])
    total = int(counts[1])

    finish = tokens.pop(0).split("=")[1]
    speed = tokens.pop(0).split("=")[1]

    return {
        "operation": operation,
        "progress": progress,
        "resynced": resynced,
        "total": total,
        "finish": finish,
        "speed": speed,
    }


def parse_device_resync_standby(line):
    return {
        "operation": line.strip(),
        "progress": "0%",
        "resynced": 0,
        "total": None,
        "finish": None,
        "speed": None,
    }
