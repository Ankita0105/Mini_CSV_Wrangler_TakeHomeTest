#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_Mini_CSV_Wrangler
----------------------------------

Tests for `Mini_CSV_Wrangler` module.
"""

import unittest

import Mini_CSV_Wrangler
from Mini_CSV_Wrangler import CSV_wrangler
from Mini_CSV_Wrangler.CSV_wrangler import wrangleCSV


class TestMini_csv_wrangler(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(Mini_CSV_Wrangler.__version__)
        wrangleCSV('/Users/ankitasharma/PycharProjects/Mini_CSV_Wrangler_TakeHomeTest/Mini_CSV_Wrangler/configdata.txt')



    def tearDown(self):
        pass
