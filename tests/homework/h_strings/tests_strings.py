import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    
    def test_get_hamming_distance(self):
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        hamming_distance = 7
        distance = get_hamming_distance(dna1, dna2)
        self.assertEqual(distance, hamming_distance)

    def test_get_dna_complement():
        dna = "AAAACCCGGT"
        dna_complement = "ACCGGGTTTT"

        complement = get_dna_complement(dna)
        assert complement == dna_complement, f"Expected complement: {dna_complement}, Got: {complement}"

    test_get_hamming_distance('GAGCCTACTAACGGGAT')
    test_get_dna_complement('AAAACCCGGT')

