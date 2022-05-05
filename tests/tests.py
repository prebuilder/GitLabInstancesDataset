#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import GitLabInstancesDataset
from GitLabInstancesDataset import isGitLab, _convertToTuple


class Tests(unittest.TestCase):
	def testDomainNameNormalization(self):
		self.assertEqual(("ni", "said", "who", "knight"), _convertToTuple("knigHt.wHo.saId.Ni"))

	def testContainsGitLab(self):
		self.assertFalse(isGitLab("gitlab.com"))

	def testInSet(self):
		self.assertTrue(isGitLab("salsa.debian.org"))


if __name__ == "__main__":
	unittest.main()
