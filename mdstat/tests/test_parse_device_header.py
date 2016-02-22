# Copyright 2015-2016, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..device_header import parse_device_header


class TestParseDeviceHeader(unittest.TestCase):

    def test_wrong_prefix(self):
        line = "something else: sda sdb"
        with self.assertRaises(ValueError):
            parse_device_header(line)

    def test_wrong_format(self):
        line = "md0 - foo bar"
        with self.assertRaises(ValueError):
            parse_device_header(line)

    def test_one(self):
        line = "md0 : active raid1 sdf1[1] sde1[0]"
        expected = (
            "md0",
            None,
            {
                "active": True,
                "personality": "raid1",
                "read_only": False,
                "disks": {
                    "sdf1": {
                        "number": 1,
                        "write_mostly": False,
                        "faulty": False,
                        "spare": False,
                        "replacement": False,
                    },
                    "sde1": {
                        "number": 0,
                        "write_mostly": False,
                        "faulty": False,
                        "spare": False,
                        "replacement": False,
                    }
                }
            }
        )
        output = parse_device_header(line)
        self.assertEquals(output, expected)

    def test_no_disks(self):
        line = "md1 : active raid5 super 1.2 level 5, 512k chunk, algorithm 2 [4/0] [____]"
        expected = (
            "md1",
            "      0 blocks super 1.2 level 5, 512k chunk, algorithm 2 [4/0] [____]",
            {
                "active": True,
                "personality": "raid5",
                "read_only": False,
                "disks": {}
            }
        )
        output = parse_device_header(line)
        self.assertEquals(output, expected)
