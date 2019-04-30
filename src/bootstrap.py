#!/usr/bin/env python3
# -*- coding: utf-8; -*-

import sys

sys.path.insert(0, "../lib")

import os
import nltk

os.environ["NLTK_DATA"] = "../"
nltk.data.path.append("../nltk_data")

print("ok")
