from island import Island
from algorithms.mergesort import mergesort

class Mode2Navigator:
    """
    This class used to simulate a "sandbox" lets a few pirates plunder an island, and returns the results.
    the key strategy is same as mode1. it will sort the island one tiem before all pirates select the island.

    Data Structures used:
    - List: To store the instance of islands.
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Data Structures used:
        - List: To store the instance of islands.

        Complexity Analysis:
        - Best Case and Worst case: O(1) no loop or recursion.
        """
        self.priates = n_pirates
        self.islands = []

    def add_islands(self, islands: list[Island]):
        """
        Data Structures used:
        - List: To store the instance of islands.

        Complexity Analysis:
        - Best Case and Worst case: O(N) N is the length of islands.
        """
        for i in islands:
            self.islands.append(i)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Data Structures used:
        - List: To store the instance of islands.
        - List: To store the seleted isalnd and the crew sent to the island.

        Complexity Analysis:
        - Best Case and Worst case: O(NlogN) merge sort have O(NlogN) complexity, and the creat the list of marine-to-money ratio
            have O(N) complexity. And also have O(C) C is the number of crew, but the rate of increase less than O(NlogN)
            So the total complexity is O(NlogN).
        """
        results = []
        islands = mergesort(self.islands, key=lambda x: x.marines/x.money)
        self.islands_ratio  = [i.marines/i.money for i in self.islands]
        for _ in range(self.priates):

            
            if len(islands) != 0:
                island:Island = islands[0]

            elif island.marines <= crew and island.money > 2 * crew:
                # island is not reamin money
                results.append((island, island.marines))
                island.marines = 0
                island.money = 0
            
            elif island.marines > crew and island.money*(crew/island.money) > 2 * crew:
                # island is reamin money
                results.append((island, crew))
                island.marines -= crew
                island.money -= island.money*(crew/island.marines)
            else:
                # no island be selected today
                results.append((None, 0))
                continue
                
            self.islands = islands
        return results