
import unittest
from validation_utils import ValidationUtils as vu

class ValidationUtilsTest(unittest.TestCase):
    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_hoge(self):
        self.assertEqual('hoge', vu.hoge())
    

if __name__ == "__main__":
    unittest.main()