import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    # Setting up the global references for Dog and Animal
    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
        self.animal = Animal("Lucy", "canine")

    # Testing that there are instances of Dog and Animal
    def test_animal_creation(self):

        murph = Dog("Murph")
        self.assertIsInstance(murph, Dog)
        self.assertIsInstance(murph, Animal)

    # Testing that when we pass in a number of legs, that is the number of legs returned
    def test_animal_can_set_legs(self):

        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6 )

    # Testing the walk calculation by passing in number of legs , then seeing if that number of legs is returned and then seeing if the speed is what we expect
    def test_animal_can_calc_walk(self):

        self.bob.set_legs(4)
        self.bob.walk()
        self.assertEqual(self.bob.legs, 4)
        self.assertEqual(self.bob.speed, .8 )

    # Testing to see if the species we pass in is returned back to us
    def test_animal_can_set_species(self):

        self.animal.set_species("human")
        self.assertEqual(self.animal.species, "human")
        # The value in species was changed to human so this should return as Failed (below)
        # self.assertEqual(self.animal.species, "canine")

    # Testing to see if we are getting the species we expect
    def test_animal_can_get_species(self):

        self.animal.get_species()
        self.assertEqual(self.animal.species, "canine")
        # The default species is canine so this should return as Failed (below)
        # self.assertEqual(self.animal.species, "human")




if __name__ == '__main__':
    unittest.main()