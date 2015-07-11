# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..device_bitmap import parse_device_bitmap


class TestParseDeviceBitmap(unittest.TestCase):

    def test_wrong_syntax(self):
        line = "any random gibberish"
        with self.assertRaises(ValueError):
            parse_device_bitmap(line)

    def test_simple(self):
        line = "      bitmap: 17/30 pages [68KB], 65536KB chunk"
        expected = {
            "existing_pages": 17,
            "total_pages": 30,
            "pages_size": "68KB",
            "chunk_size": "65536KB",
            "file": None,
        }
        result = parse_device_bitmap(line)
        self.assertEquals(result, expected)

    def test_with_file(self):
        line = "      bitmap: 17/30 pages [68KB], 65536KB chunk, file: a_file"
        expected = {
            "existing_pages": 17,
            "total_pages": 30,
            "pages_size": "68KB",
            "chunk_size": "65536KB",
            "file": "a_file",
        }
        result = parse_device_bitmap(line)
        self.assertEquals(result, expected)
