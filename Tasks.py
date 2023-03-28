import unittest

#Task1
def filter_list(input_list):
    return [item for item in input_list if isinstance(item, int) and item >= 0]

#Task2
def first_non_repeating_letter(s):
    s_lower = s.lower()
    for c in s:
        if s_lower.count(c.lower()) == 1:
            return c
    return ""

#Task3
def digital_root(n):
    if n < 10:
        return n

    digit_sum = sum(int(d) for d in str(n))

    return digital_root(digit_sum)

#Task4
def count_pairs_with_sum(arr, target):
    freq = {}
    count = 0
    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    return count

#Task5
def meeting(s):
    names = [name.upper() for name in s.split(';')]

    names = [(name.split(':')[0], name.split(':')[1]) for name in names]

    names = sorted(names, key=lambda x: (x[1], x[0]))

    return ''.join(['(' + name[1] + ', ' + name[0] + ')' for name in names])

#ExtraTask1
def next_bigger_number(num):
    digits = [int(d) for d in str(num)]

    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i < 0:
        return -1

    j = len(digits) - 1
    while j >= 0 and digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]

    digits[i + 1:] = reversed(digits[i + 1:])

    return int(''.join([str(d) for d in digits]))

#ExtraTask2
def int_to_ip(addr):
    binary = format(addr, '032b')

    octets = [binary[i:i + 8] for i in range(0, 32, 8)]

    decimal_octets = [int(octet, 2) for octet in octets]

    ipv4 = '.'.join(map(str, decimal_octets))

    return ipv4


class Test(unittest.TestCase):
    def test_task1(self):
        self.assertLessEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
        self.assertLessEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertLessEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])

    def test_task2(self):
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('ABBA'), '')

    def test_task3(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(493193), 2)

    def test_task4(self):
        self.assertEqual(count_pairs_with_sum([1, 3, 6, 2, 2, 0, 4, 5], 5), 4)
        self.assertEqual(count_pairs_with_sum([1, 3, 6, 2, 2, 0, 4, 5], 6), 4)
        self.assertEqual(count_pairs_with_sum([1, 3, 6, 2, 2, 0, 4, 5], -5), 0)

    def test_task5(self):
        self.assertEqual(meeting('Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'), '(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)')
        self.assertEqual(meeting('Anna:Likhachova;Ivan:Sierov;Misha:Perviy;Andriy:Shevtsov'), '(LIKHACHOVA, ANNA)(PERVIY, MISHA)(SHEVTSOV, ANDRIY)(SIEROV, IVAN)')
        self.assertEqual(meeting('Charlie:Smith;Bob:Marley;Alisa:Ivanova'), '(IVANOVA, ALISA)(MARLEY, BOB)(SMITH, CHARLIE)')

    def test_extratask1(self):
        self.assertEqual(next_bigger_number(12), 21)
        self.assertEqual(next_bigger_number(513), 531)
        self.assertEqual(next_bigger_number(2017), 2071)

    def test_extratask2(self):
        self.assertEqual(int_to_ip(2149583361), '128.32.10.1')
        self.assertEqual(int_to_ip(32), '0.0.0.32')
        self.assertEqual(int_to_ip(0), '0.0.0.0')
