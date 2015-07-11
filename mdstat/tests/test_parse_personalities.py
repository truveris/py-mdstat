# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from .. import parse_personalities


class TestParsePersonalities(unittest.TestCase):

    def test_wrong_prefix(self):
        line = "something else: sda sdb"
        with self.assertRaises(ValueError):
            parse_personalities(line)

    def test_none(self):
        line = "Personalities : "
        expected = []
        output = parse_personalities(line)
        self.assertEquals(output, expected)

    def test_one(self):
        line = "Personalities : [raid0]"
        expected = ["raid0"]
        output = parse_personalities(line)
        self.assertEquals(output, expected)

    def test_many(self):
        line = "Personalities : [raid0] [raid1] [raid5] [raid10]"
        expected = ["raid0", "raid1", "raid5", "raid10"]
        output = parse_personalities(line)
        self.assertEquals(output, expected)
