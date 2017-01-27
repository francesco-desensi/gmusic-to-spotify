#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gmusic_to_spotify
----------------------------------

Tests for `gmusic_to_spotify` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from gmusic_to_spotify import gmusic_to_spotify
from gmusic_to_spotify import cli



class TestGmusic_to_spotify(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'gmusic_to_spotify.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output