import unittest
import datetime

class Testing123(unittest.TestCase):

    def test_symbol(self):
        symbol = input("\nWhat is the stock symbol for the company? ")
        self.assertTrue(symbol.isupper())
        self.assertTrue(symbol.isalpha())
        self.assertTrue(0<len(symbol)<=7)

    def test_chartType(self):
        chartType = int(input("\nWhat type of chart?\n1. Bar\n2. Line\nSelection: "))
        self.assertTrue(chartType==1 or chartType ==2)

    def test_timeSeries(self):
        timeSeries = int(input("\nWhat time series would you like to specify?\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\nSelection: "))
        self.assertTrue(timeSeries==1 or timeSeries ==2 or timeSeries==3 or timeSeries==4)

    def test_startDate(self):
        start_Date = input("\nWhat is the start date? Format: YYYY-MM-DD: ")
        startDate = datetime.datetime.strptime(start_Date, "%Y-%m-%d")
        self.assertIsInstance(startDate, datetime.date)

    def test_endDate(self):
        end_Date = input("\nWhat is the end date? Format: YYYY-MM-DD: ")
        endDate = datetime.datetime.strptime(end_Date, "%Y-%m-%d")
        self.assertIsInstance(endDate, datetime.datetime)
        

if __name__ == '__main__':
    unittest.main()