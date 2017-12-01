import unittest
import congestionfinder.bpsdetector
import logging

logging.getLogger().level = logging.DEBUG


class TestBPSDetector(unittest.TestCase):
    def test_getBPSCode(self):
        input = "00D00C03405B18200005"
        expected = input
        bpsDetector = congestionfinder.bpsdetector.BPSDetector(input)
        output = bpsDetector.getBPSCode()
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)

    def test_getRoadNumber(self):
        input = "00D00C03405B18200005"
        expected = 12
        bpsDetector = congestionfinder.bpsdetector.BPSDetector(input)
        output = bpsDetector.getRoadNumber()
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)

    def test_getHectometer(self):
        input = "00D00C03405B18200005"
        expected = 208
        bpsDetector = congestionfinder.bpsdetector.BPSDetector(input)
        output = bpsDetector.getHectometer()
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)

    def test_getAdditionalMeters(self):
        input = "00D00C03405B18200005"
        expected = 91
        bpsDetector = congestionfinder.bpsdetector.BPSDetector(input)
        output = bpsDetector.getAdditionalMeters()
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)

    def test_getMeter(self):
        input = "00D00C03405B18200005"
        expected = 20891
        bpsDetector = congestionfinder.bpsdetector.BPSDetector(input)
        output = bpsDetector.getMeter()
        logging.debug("input: " + str(input))
        logging.debug("expected: " + str(expected))
        logging.debug("output: " + str(output))
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()