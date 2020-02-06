import unittest
from _lib import *
import HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner

class SmokeTests(unittest.TestCase):

    def test_100_Start_Browser(self):
        print("XXXXXXXXX Test started XXXXXXXXX")
        Browser.Start("google.com")
        sleep(5)
        Browser.Maximize()

    def test_200_Form_Login(self):
        print("XXXXXXXXX Test started XXXXXXXXX")
        Form_Login_UI.Start("file:///C:/Users/vkotenko/Desktop/PythonCourse/Sikuli_all/mini-framework/1_SampleWebpage.html")
        sleep(5)
        Form_Login_UI.Maximize()
        Form_Login_UI.ClickButton()

suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
HtmlXmlTestRunner.HTMLTestRunner(file(r"Report.html", "w")).run(suite)










# # It's not the shortest version, but for sure it works stable for years :)
# # Recommended to use it
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
#     

#     # Use it to add manually test cases - handy when debugging a specific part of the set
#	  #suite = unittest.TestSuite()
#     #suite.addTest(SmokeTests('test_100_Start_Browser'))
#     #suite.addTest(SmokeTests('test_200_Form_Login'))

#     outfile = open("Report.html", "w")
#     runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Description")
#     runner.run(suite)
#     outfile.close()

