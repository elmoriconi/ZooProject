import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def setUp(self) -> None:
        self.zoo_1: Zoo = Zoo()    
        self.zookeeper_1: ZooKeeper = ZooKeeper("Gianni", "Rossi", 1)
        self.fence_1: Fence = Fence(100, 25.0, "savana")
        self.animal_1: Animal = Animal("Pluto", "Canide", 5, 300.0, 1.0, "savana")
        self.animal_2: Animal = Animal("Pippo", "Canide", 5, 3.0, 1.0, "savana")

    def test_animal_dimesion(self):
        """
        controlla se un animale troppo grande viene inserito all'interno di una fence
        """
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        self.assertEqual(result, 0, message)

    def test_habitat(self):
        """
        controlla se l'habitat dell'animale corrisponde a quello della fence
        """
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: bool = (self.animal_1.habitat == self.fence_1.habitat)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        self.assertEqual(result, True, message)

    def test_add_animal(self):
        """
        controlla se l'animale è stato aggiunto nella fence
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        message: str = f"Error: the function add_animal didn't add self.animal_2 into self.fence_1"
        self.assertEqual(result, 1, message)

    def test_less_residual_area(self):
        """
        controlla se l'aria residua è stata diminuita una volta aggiunto l'animale
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        result: float = (self.fence_1.residual_area - self.animal_2.width*self.animal_2.height)
        message: str = f"Error: the fence's residual area wasn't modified after adding the animal"
        self.assertEqual(result, (self.fence_1.residual_area - 3), message)

    def test_increased_height(self):
        """
        controlla che l'altezza dell'animale sia incrementata una volta nutrito l'animale
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        self.zookeeper_1.feed(self.animal_2)
        result: float = (self.animal_2.height + ((2/100) * self.animal_2.height))
        message: str = f"Error: the animal's height wasn't modified after feeding the animal"
        self.assertEqual(result, (self.animal_2.height + ((2/100) * self.animal_2.height)), message)

    def test_increased_width(self):
        """
        controlla che la larghezza dell'animale sia incrementata una volta nutrito l'animale
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        self.zookeeper_1.feed(self.animal_2)
        result: float = (self.animal_2.width + ((2/100) * self.animal_2.width))
        message: str = f"Error: the animal's width wasn't modified after feeding the animal"
        self.assertEqual(result, (self.animal_2.width + ((2/100) * self.animal_2.width)), message)

    def test_dimension_to_feed(self):
        """
        controlla se un animale può essere nutrito o no, in base a quanto crescerebbe essendo nutrito
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        self.zookeeper_1.feed(self.animal_2)
        new_height: float = (self.animal_2.height + ((2/100) * self.animal_2.height))
        new_width: float = (self.animal_2.width + ((2/100) * self.animal_2.width))
        new_area: float = new_height * new_width
        result: bool = new_area <= self.fence_1.residual_area
        message: str = f"Error: the function feed_animal should not feed the animal"
        self.assertEqual(result, True, message)

    def test_residual_area_after_feeding(self):
        """
        controlla se l'area residua è stata modificata dopo aver nutrito l'animale
        """
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        self.zookeeper_1.feed(self.animal_2)
        new_height: float = (self.animal_2.height + ((2/100) * self.animal_2.height))
        new_width: float = (self.animal_2.width + ((2/100) * self.animal_2.width))
        new_area: float = new_height * new_width
        result: float = self.fence_1.residual_area - new_area
        message: str = f"Error: the function feed_animal didn't reduce the fence's residual area after feeding the animal"
        self.assertEqual(result, self.fence_1.residual_area - new_area, message)

    def test_health(self):
        self.zookeeper_1.add_animal(self.animal_2, self.fence_1)
        self.zookeeper_1.feed(self.animal_2)
        result: float = self.animal_2.health * 1.01
        message: str = f"Error: the function feed_animal didn't improve the animal's health after feeding the animal"
        self.assertEqual(result, self.animal_2.health * 1.01, message)

    def test_remove(self):
        """
        controlla se l'animale è stato rimosso dalla fence
        """
        self.zookeeper_1.remove_animal(self.animal_2, self.fence_1)
        result: int = len(self.fence_1.list_of_animals)
        message: str = f"Error: the function remove_animal didn't remove self.animal_2 into self.fence_1"
        self.assertEqual(result, 0, message)

    def test_more_residual_area(self):
        """
        controlla se l'aria residua è stata aumentata una volta rimosso l'animale
        """
        self.zookeeper_1.remove_animal(self.animal_2, self.fence_1)
        result: float = (self.fence_1.residual_area + self.animal_2.width*self.animal_2.height)
        message: str = f"Error: the fence's residual area wasn't modified after removing the animal"
        self.assertEqual(result, (self.fence_1.residual_area + 3), message)


if __name__ == "__main__":
    unittest.main()