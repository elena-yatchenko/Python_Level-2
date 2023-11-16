from Less_14_TAsk_2 import clear_text


def test_non_change:
    assert "this is a sample" == clear_text("this is a sample"), 'FAIL'


def test_register(self):
    self.assertEqual("this is a sample", clear_text("This is a sample"))


def test_punctuation(self):
    self.assertEqual("this is a sample", clear_text("this is a sample,"))


def test_another_alph(self):
    self.assertEqual("this is a sample ", clear_text("this is a sample вапвап"))


def test_all(self):
    self.assertEqual("this is a sample  ", clear_text("This is a Sample, - вапвап"))


###333

def test_non_change():
    assert "this is a sample" == clear_text("this is a sample"), "FAIL"


def test_register():
    assert "this is a sample" == clear_text("This is a sample"), "FAIL"


def test_punctuation():
    assert "this is a sample" == clear_text("this is a sample,"), "FAIL"


def test_another_alph():
    assert "this is a sample " == clear_text("this is a sample вапвап"), "FAIL"


def test_all():
    assert "this is a sample  " == clear_text("This is a Sample, - вапвап"), "FAIL"


if __name__ == '__main__':
    pytest.main(['-sv'])