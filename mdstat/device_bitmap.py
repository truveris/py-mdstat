# Copyright 2015, Truveris Inc. All Rights Reserved.

from __future__ import absolute_import


def parse_device_bitmap(line):
    tokens = line.split()[1:]

    page_counts = tokens.pop(0).split("/")
    existing_pages = int(page_counts[0])
    total_pages = int(page_counts[1])

    if tokens.pop(0) != "pages":
        raise ValueError("invalid device bitmap syntax (pages): {0}"
                         .format(line))

    pages_size = tokens.pop(0)[1:-2]
    chunk_size = tokens.pop(0)

    if not tokens.pop(0).startswith("chunk"):
        raise ValueError("invalid device bitmap syntax (chunk): {0}"
                         .format(line))

    if tokens and tokens.pop(0) == "file:":
        file_ = tokens.pop(0)
    else:
        file_ = None

    return {
        "existing_pages": existing_pages,
        "total_pages": total_pages,
        "pages_size": pages_size,
        "chunk_size": chunk_size,
        "file": file_,
    }
