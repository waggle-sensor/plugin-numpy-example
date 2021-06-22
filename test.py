from main import process_frame
import numpy as np
import cv2
import unittest

# This is an example of building a test suite using Python's unittest module.
class MyTestCase(unittest.TestCase):

    def example_test(self):
        frame = cv2.imread("test.jpg")
        results = process_frame(frame)
        self.assertLessEqual(results["min"][0], results["max"][0])
        self.assertLessEqual(results["min"][1], results["max"][1])
        self.assertLessEqual(results["min"][2], results["max"][2])
    
    # You can add your own something_test functions below to expand the test!

# This will run all the tests when this file is executed.
if __name__ == "__main__":
    unittest.main()
