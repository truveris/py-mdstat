# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..device_status import (
    parse_device_status,
    parse_device_status_disk_accounting,
    parse_device_status_raid5,
    parse_device_status_raid10,
)


class TestParseDeviceStatus(unittest.TestCase):

    def test_disk_accounting(self):
        counts, synced = "[6/4]", "[_UUUU_]"
        result = parse_device_status_disk_accounting(counts, synced)
        expected = {
            "raid_disks": 6,
            "non_degraded_disks": 4,
            "synced": [False, True, True, True, True, False],
        }
        self.assertEquals(result, expected)

    def test_device_status_raid10(self):
        tokens = "512K chunks 2 near-copies [4/4] [UUUU]".split()
        expected = {
            "chunks": "512K",
            "near_copies": 2,
            "offset_copies": 0,
            "far_copies": 1,
            "raid_disks": 4,
            "non_degraded_disks": 4,
            "synced": [True, True, True, True],
        }
        result = parse_device_status_raid10(tokens)
        self.assertEquals(result, expected)

    def test_device_status_raid5(self):
        tokens = "level 5, 128k chunk, algorithm 2 [4/3] [UUU_]".split()
        expected = {
            "chunk_size": "128k",
            "level": 5,
            "algorithm": 2,
            "raid_disks": 4,
            "non_degraded_disks": 3,
            "synced": [True, True, True, False],
        }
        result = parse_device_status_raid5(tokens)
        self.assertEquals(result, expected)

    def test_device_status_bad_prefix(self):
        line = "something else"
        with self.assertRaises(ValueError):
            parse_device_status(line, None)

    def test_device_status(self):
        line = "      34359475200 blocks super 1.2"
        expected = {
            "super": "1.2",
            "blocks": 34359475200,
        }
        result = parse_device_status(line, None)
        self.assertEquals(result, expected)
