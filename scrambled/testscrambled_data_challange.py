from unittest import TestCase
from scrambled_data_challange import scramblecount


class TestScrambledDataChallenge(TestCase):
    def test_scramblecount_case1(self):
        str = "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt"
        dictWord = "axpaj"
        self.assertTrue(1 == scramblecount(dictWord, str))

    def test_scramblecount_case2(self):
        str = "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt"
        dictList = ["axpaj", "dnrbt"]
        actualCount = 0
        for dictionary in dictList:
            actualCount += scramblecount(dictionary, str)

        self.assertEquals(actualCount, 2, "testcase passed")
