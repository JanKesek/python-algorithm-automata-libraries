import unittest
import set1
class Test(unittest.TestCase):
    def test_fixed_xor(self):
        a="0x1c0111001f010100061a024b53535009181c"
        b="0x686974207468652062756c6c277320657965"
        c="0x746865206b696420646f6e277420706c6179"
        self.assertEqual(set1.fixed_xor(a,b),c)
    def test_single_byte_xor_cipher(self):
        encoded='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        sentence='cOOKING mcS LIKE A POUND OF BACON'
        self.assertEqual(set1.single_byte_xor_cipher(encoded),sentence)
if __name__ == "__main__":
    unittest.main()