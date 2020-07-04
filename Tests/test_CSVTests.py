import unittest
from CsvReader.CsvReader import CsvReader
from pprint import pprint
from pathlib import Path


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/subtraction.csv')

    def test_return_data_as_objects(self):
        data = self.csv_reader.return_data_as_class('value1')
        self.assertIsInstance(data, list)
        test_data = ClassFactory('value1', self.csv_reader.data[0])

        for value1 in data:
            self.assertEqual(value1.__name__, test_data.__name__)


if __name__ == '__main__':
    unittest.main()
