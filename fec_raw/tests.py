#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase


class FecTest(TestCase):

    def test_fake(self):
        self.assertEqual(2+2, 4)
