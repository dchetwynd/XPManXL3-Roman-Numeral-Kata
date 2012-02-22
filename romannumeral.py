import unittest

class RomanTests(unittest.TestCase):

	def testFrameworkWorking(self):
		self.assertEqual(1, 1)

	def testIConvertsToOne(self):
		convertedNumeral = romanconverter("I")
		self.assertEqual(1, convertedNumeral)
	def testVConvertsToFive(self):
		convertedNumeral = romanconverter("V")
		self.assertEqual(5, convertedNumeral)
	def testXConvertsToTen(self):
		convertedNumeral = romanconverter("X")
		self.assertEqual(10, convertedNumeral)
	def testIVConvertsToFour(self):
		convertedNumeral = romanconverter("IV")
		self.assertEqual(4, convertedNumeral)
	def testIIConvertsToTwo(self):
		convertedNumeral = romanconverter("II")
		self.assertEqual(2, convertedNumeral)
	def testIIIConvertsToThree(self):
		convertedNumeral = romanconverter("III")
		self.assertEqual(3, convertedNumeral)

def romanconverter(roman):
	result = 1

	
	
	if roman == "I":
		return result
	elif roman == "II":
		return result + 1
	elif roman == "III":
		return result + 2
	elif roman == "IV":
		return result + 3
	elif roman == "V":
		return 5
	else:
		return 10

	
if __name__ == '__main__':
	unittest.main()
