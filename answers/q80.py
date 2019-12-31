#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import zlib


def question80CompressDecompress(data):
    compress = zlib.compress(data)
    print(compress)
    print(zlib.decompress(compress))


question80CompressDecompress(
        b'hello world!hello world!hello world!hello world!')
