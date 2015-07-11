# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from .. import parse_unused_devices


class TestParseUnusedDevices(unittest.TestCase):

    def test_wrong_prefix(self):
        line = "something else: sda sdb"
        with self.assertRaises(ValueError):
            parse_unused_devices(line)

    def test_none(self):
        line = "unused devices: <none>"
        expected = []
        output = parse_unused_devices(line)
        self.assertEquals(output, expected)

    def test_one(self):
        line = "unused devices: sda"
        expected = ["sda"]
        output = parse_unused_devices(line)
        self.assertEquals(output, expected)

    def test_many(self):
        line = "unused devices: sdb sdd sdg"
        expected = ["sdb", "sdd", "sdg"]
        output = parse_unused_devices(line)
        self.assertEquals(output, expected)
