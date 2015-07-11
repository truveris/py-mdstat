# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..disk import parse_device_disk, parse_device_disks


class TestParseDisks(unittest.TestCase):

    def test_simple(self):
        value = "sda[0]"
        expected = (
            "sda",
            {
                "number": 0,
                "write_mostly": False,
                "faulty": False,
                "spare": False,
                "replacement": False,
            }
        )
        output = parse_device_disk(value)
        self.assertEquals(output, expected)

    def test_one_flag(self):
        value = "sda[0](S)"
        expected = (
            "sda",
            {
                "number": 0,
                "write_mostly": False,
                "faulty": False,
                "spare": True,
                "replacement": False,
            }
        )
        output = parse_device_disk(value)
        self.assertEquals(output, expected)

    def test_many_flags(self):
        value = "sda[0](S)(F)(W)"
        expected = (
            "sda",
            {
                "number": 0,
                "write_mostly": True,
                "faulty": True,
                "spare": True,
                "replacement": False,
            }
        )
        output = parse_device_disk(value)
        self.assertEquals(output, expected)

    def test_parse_disks(self):
        tokens = [
            "sda[0]",
            "sdb[1]",
            "sdc[2](S)",
        ]
        expected = {
            "sda": {
                "number": 0,
                "write_mostly": False,
                "faulty": False,
                "spare": False,
                "replacement": False,
            },
            "sdb": {
                "number": 1,
                "write_mostly": False,
                "faulty": False,
                "spare": False,
                "replacement": False,
            },
            "sdc": {
                "number": 2,
                "write_mostly": False,
                "faulty": False,
                "spare": True,
                "replacement": False,
            },
        }
        output = parse_device_disks(tokens)
        self.assertEquals(output, expected)
