mdstat for python
=================

This short library is used to convert your ``/proc/mdstat`` file into an object
usable in Python.  It comes with a short ``mdjson`` script that dumps your file
in a JSON format.

Requirements
------------
 - Linux (or at least get mdstat files from a Linux machine)
 - Python 2.6+ (or 3.2+)

Example usage
-------------
For most use cases, you can simple run ``mdstat.parse()`` to get nested
dictionaries repesenting your local ``/proc/mdstat`` file.  If you fetch the
file remotely or need to run the parser on a stream, use ``parse_stream``.

.. code-block:: javascript

    $ mdjson
    {
        "personalities": [
            "raid10"
        ],
        "unused_devices": [],
        "devices": {
            "md127": {
                "read_only": true,
                "status": {
                    "near_copies": 2,
                    "blocks": 34359475200,
                    "raid_disks": 4,
                    "offset_copies": 0,
                    "far_copies": 1,
                    "synced": [
                        true,
                        true,
                        true,
                        true
                    ],
                    "chunks": "512K",
                    "super": "1.2",
                    "non_degraded_disks": 4
                },
                "bitmap": null,
                "resync": null,
                "active": true,
                "disks": {
                    "xvdf": {
                        "spare": true,
                        "faulty": false,
                        "write_mostly": false,
                        "number": 4,
                        "replacement": false
                    },
                    "xvdd": {
                        "spare": false,
                        "faulty": false,
                        "write_mostly": false,
                        "number": 2,
                        "replacement": false
                    },
                    "xvde": {
                        "spare": false,
                        "faulty": false,
                        "write_mostly": false,
                        "number": 3,
                        "replacement": false
                    },
                    "xvdb": {
                        "spare": false,
                        "faulty": false,
                        "write_mostly": false,
                        "number": 0,
                        "replacement": false
                    },
                    "xvdc": {
                        "spare": false,
                        "faulty": false,
                        "write_mostly": false,
                        "number": 1,
                        "replacement": false
                    }
                },
                "personality": "raid10"
            }
        }
    }

You can also use the python interface to generate a nested dictionary:

.. code-block:: python

    >>> import mdstat
    >>> mdstat.parse()
    {
        "personalities": [
            "raid1",
            "raid5",
            "raid10",
        ],
        "devices": {
            "md0": {
                "active": True,
                [... snip ...]
            }
        }
        "unused_devices": []
    }
