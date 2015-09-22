# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

from .device_header import parse_device_header
from .device_status import parse_device_status
from .device_bitmap import parse_device_bitmap
from .device_resync import (
    parse_device_resync_progress,
    parse_device_resync_standby,
)


def parse_device(lines):
    """Parse all the lines of a device block.

    A device block is composed of a header line with the name of the device and
    at least one extra line describing the device and its status.  The extra
    lines have a varying format depending on the status and personality of the
    device (e.g. RAID1 vs RAID5, healthy vs recovery/resync).

    """
    name, device = parse_device_header(lines.pop(0))

    status = parse_device_status(lines.pop(0), device["personality"])
    bitmap = None
    resync = None

    for line in lines:
        if line.startswith("      bitmap:"):
            bitmap = parse_device_bitmap(line)
        elif line.startswith("      ["):
            resync = parse_device_resync_progress(line)
        elif line.startswith("      \tresync="):
            resync = parse_device_resync_standby(line)
        else:
            raise NotImplementedError("unknown device line: {}".format(line))

    device.update({
        "status": status,
        "bitmap": bitmap,
        "resync": resync,
    })

    return (name, device)
