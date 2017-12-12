import unittest
import congestionfinder.congestion
import patchfinder.patch
import logging

logging.getLogger().level = logging.DEBUG


class TestCongestion(unittest.TestCase):
    def test_filterLargeCongestions(self):
        logging.debug("Starting test_filterLargeCongestions()")
        input = patchfinder.patch.Patch(1, 999, 1, 999)
        patch1 = patchfinder.patch.Patch(1, 2, 3, 4)
        patch2 = patchfinder.patch.Patch(5, 5, 5, 5)
        expected = input
        output = congestionfinder.congestion.filterLargeCongestions([input, patch1, patch2], 100)[0]
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)
        logging.debug("Ending test_filterLargeCongestions()")

    def test_addMargins(self):
        logging.debug("Starting test_addMargins()")
        patch1 = patchfinder.patch.Patch(1, 2, 3, 4)
        patch2 = patchfinder.patch.Patch(5, 5, 5, 5)
        input = [patch1, patch2]
        patch2 = patchfinder.patch.Patch(0, 4, 0, 7)
        patch3 = patchfinder.patch.Patch(3, 6, 2, 8)
        expected = [patch2, patch3]
        output = congestionfinder.congestion.addMargins(input, 2, 3, 0, 6, 0, 10)
        logging.debug("input: " + " - ".join(str(x) for x in input))
        logging.debug("expected: " + " - ".join(str(x) for x in expected))
        logging.debug("output: " + " - ".join(str(x) for x in output))
        self.assertEqual(expected, output)
        logging.debug("Ending test_addMargins()")


if __name__ == '__main__':
    unittest.main()
