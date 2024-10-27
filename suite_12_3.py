import unittest
import tests_12_3

mST = unittest.TestSuite()
mST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
mST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(mST)