# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import


def parse_device_status_disk_accounting(counts, synced):
    disk_counts = counts[1:-1].split("/", 1)
    raid_disks, non_degraded_disks = (int(c) for c in disk_counts)

    synced = [c == "U" for c in synced[1:-1]]

    return {
        "raid_disks": raid_disks,
        "non_degraded_disks": non_degraded_disks,
        "synced": synced,
    }


def parse_device_status_raid0(tokens):
    if tokens[1] == "chunks":
        chunks, tokens = tokens[0], tokens[2:]
    else:
        chunks = None

    return {
        "chunks": chunks,
    }


def parse_device_status_raid1(tokens):
    return parse_device_status_disk_accounting(tokens[0], tokens[1])


def parse_device_status_raid5(tokens):
    if tokens.pop(0) != "level":
        raise ValueError("invalid device raid4/5 syntax (level)")

    level = int(tokens.pop(0).rstrip(","))
    chunk_size = tokens.pop(0)

    if tokens.pop(0) != "chunk,":
        raise ValueError("invalid device raid4/5 syntax (chunk)")

    if tokens.pop(0) != "algorithm":
        raise ValueError("invalid device raid4/5 syntax (algorithm)")

    algorithm = int(tokens.pop(0))

    status = {
        "level": level,
        "chunk_size": chunk_size,
        "algorithm": algorithm,
    }

    status.update(parse_device_status_disk_accounting(tokens[0], tokens[1]))

    return status


parse_device_status_raid4 = parse_device_status_raid5
parse_device_status_raid6 = parse_device_status_raid5


def parse_device_status_raid10(tokens):
    if tokens[1] == "chunks":
        chunks, tokens = tokens[0], tokens[2:]
    else:
        chunks = None

    if tokens[1] == "near-copies":
        near_copies, tokens = int(tokens[0]), tokens[2:]
    else:
        near_copies = 1

    if tokens[1] == "far-copies":
        far_copies, tokens = int(tokens[0]), tokens[2:]
        offset_copies = 0
    elif tokens[1] == "offset-copies":
        offset_copies, tokens = int(tokens[0]), tokens[2:]
        far_copies = 0
    else:
        offset_copies = 0
        far_copies = 1

    status = {
        "chunks": chunks,
        "near_copies": near_copies,
        "far_copies": far_copies,
        "offset_copies": offset_copies,
    }

    status.update(parse_device_status_disk_accounting(tokens[0], tokens[1]))

    return status


def parse_device_status(line, personality):
    if not line.startswith("      "):
        raise ValueError("invalid device status line (bad prefix): {0}"
                         .format(line))

    tokens = line.split()
    blocks = int(tokens.pop(0))

    if tokens.pop(0) != "blocks":
        raise ValueError("invalid device status line (missing blocks): {0}"
                         .format(line))

    if tokens and tokens[0] == "super":
        tokens.pop(0)
        super_ = tokens.pop(0)
    else:
        super_ = None

    status = {
        "blocks": blocks,
        "super": super_,
    }

    personality_status = globals().get("parse_device_status_{0}"
                                       .format(personality))
    if tokens and personality_status:
        status.update(personality_status(tokens))

    return status
