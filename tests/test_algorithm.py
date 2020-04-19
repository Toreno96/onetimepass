import unittest

from onetimepass import algorithm


class TestHOTP(unittest.TestCase):
    def test_hotp(self):
        # Based on https://tools.ietf.org/html/rfc4226#page-32
        counter_start = 0
        expected_hotps = [
            755224,
            287082,
            359152,
            969429,
            338314,
            254676,
            287922,
            162583,
            399871,
            520489,
        ]
        for counter, expected_hotp in enumerate(expected_hotps, start=counter_start):
            with self.subTest(i=counter):
                hotp = algorithm.hotp(
                    algorithm.HOTPParameters(
                        secret=b"12345678901234567890", digits_count=6, counter=counter
                    )
                )
                self.assertEqual(hotp, expected_hotp)


class TestTOTP(unittest.TestCase):
    def test_to_hotp_parameters(self):
        pass

    def test_totp(self):
        pass
