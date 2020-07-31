import unittest
import CSVtoJson
import filecmp

class Test_csv(unittest.TestCase):

    csvFilePath = r'Bikes.csv'
    jsonFilePath = r'JsonBikes.json'
    csvFilePath2 = r'Bikes2.csv'

    def test_CSVtoJson(self):
        CSVtoJson.csvToJson(self.csvFilePath, self.jsonFilePath)
        CSVtoJson.jsonToCSV(self.jsonFilePath, self.csvFilePath2)

        flag = filecmp.cmp(self.csvFilePath, self.csvFilePath2)
        self.assertEqual(flag, True)


if __name__ == '__main__':
    unittest.main()
