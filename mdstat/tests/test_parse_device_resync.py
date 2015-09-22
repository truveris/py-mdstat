# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import

import unittest

from ..device_resync import (
    parse_device_resync_progress,
    parse_device_resync_standby,
)


class TestParseDeviceResync(unittest.TestCase):

    def test_wrong_syntax(self):
        line = "any random gibberish"
        with self.assertRaises(ValueError):
            parse_device_resync_progress(line)

    def test_simple_progress(self):
        line = (
            "      [==>..................]  recovery = 12.6% "
            "(37043392/292945152) finish=127.5min speed=33440K/sec"
        )
        expected = {
            "operation": "recovery",
            "progress": "12.6%",
            "resynced": 37043392,
            "total": 292945152,
            "finish": "127.5min",
            "speed": "33440K/sec",
        }
        result = parse_device_resync_progress(line)
        self.assertEquals(result, expected)

    def test_simple_standby(self):
        line = (
            "      \tresync=PENDING"
        )
        expected = {
            "operation": "resync=PENDING",
            "progress": "0%",
            "resynced": 0,
            "total": None,
            "finish": None,
            "speed": None,
        }
        result = parse_device_resync_standby(line)
        self.assertEquals(result, expected)
