# Copyright 2015-2016, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

from .device import parse_device
from .utils import group_lines


__version__ = "1.0.4"


def parse_unused_devices(line):
    if not line.startswith("unused devices: "):
        raise ValueError("invalid unused device line: {0}"
                         .format(line))

    names = line.split()[2:]
    if "<none>" in names:
        names.remove("<none>")

    return names


def parse_personalities(line):
    if not line.startswith("Personalities : "):
        raise ValueError("invalid personalities line: {0}"
                         .format(line))

    tokens = line.split()[2:]
    return [t[1:-1] for t in tokens if t.startswith("[")]


def parse_lines(lines):
    # First and last lines are special, parse them first.
    personalities = parse_personalities(lines.pop(0))
    unused_devices = parse_unused_devices(lines.pop())

    # Split the device by empty lines and parse them separately.
    devices = {}
    for device_lines in group_lines(lines):
        name, device = parse_device(device_lines)
        devices[name] = device

    return {
        "personalities": personalities,
        "unused_devices": unused_devices,
        "devices": devices,
    }


def parse_stream(fp):
    return parse_lines([l.rstrip("\r\n") for l in fp])


def parse(path="/proc/mdstat"):
    with open(path) as fp:
        return parse_stream(fp)
