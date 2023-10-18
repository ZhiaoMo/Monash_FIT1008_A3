from island import Island
from algorithms.binary_search import binary_search
from algorithms.mergesort import mergesort

class Mode1Navigator:
    """
    This class used to find the best order islands to make money. My strategy is using mergesort the key is marine/money, 
    for sort the island from highest efficiency to lowest efficiency. Then, I will select the island from the highest to lowest
    untill run out the crew.

    Data Structures used:
    - List: To store the islands and their marine-to-money ratio.
    
    Example:
        Island("A", 400, 100)
        Island("B", 300, 150)
        Island("C", 100, 5)
        Island("D", 350, 90)
        Island("E", 300, 100)
        - after sort:
        Island("C", 100, 5)
        Island("A", 400, 100)
        Island("D", 350, 90)
        Island("E", 300, 100)
        Island("B", 300, 150)

        if crew = 200
        we can get 100 + 400 + 350 + 19.4444 = 869.4444
        much more than before sort 400 + 300*(100/150) = 600
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Algorithm used:
        - Merge Sort: To sort the islands from highest efficiency to lowest efficiency with Worst Case O(NlogN) complexity.

        Complexity Analysis:
        - Best Case and Worst case: O(NlogN) merge sort have O(NlogN) complexity, and the creat the list of marine-to-money ratio
            have O(N) complexity. So the total complexity is O(NlogN).
        """
        
        self.islands = mergesort(islands, key=lambda x: x.marines/x.money)
        self.islands_ratio  = [i.marines/i.money for i in self.islands]
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Data Structures used:
        - List: To store the instance of islands.
        - List: To store the sekected isalnd and the crew sent to the island.
        Example:
            Island("A", 400, 100)
            Island("B", 300, 150)
            Island("C", 100, 5)
            Island("D", 350, 90)
            Island("E", 300, 100)
            - after sort:
            Island("C", 100, 5)
            Island("A", 400, 100)
            Island("D", 350, 90)
            Island("E", 300, 100)
            Island("B", 300, 150)

            if crew = 200
            we can get 100 + 400 + 350 + 19.4444 = 869.4444
            much more than before sort 400 + 300*(100/150) = 600

        Complexity Analysis:
        - Best Case: O(logN) N is the number of islands, becuase crew is constant, every ieration
            will reduce the number of islands possible to select by nearlly half. The conplexity 
            update the list all with O(1) complexity.
        - Worst Case: O(N) N is the number of islands, if the crew is very large, it have to iterate 
            all the islands. The conplexity update the list all with O(1) complexity.
        """
        if len(self.islands) == 0:
            raise Exception("No islands added!")
        crew_left = self.crew
        list_select_islands = []
        for island in self.islands:
            if crew_left <= island.marines:
                list_select_islands.append((island, crew_left))
                break
            else:
                crew_left -= island.marines
                list_select_islands.append((island, island.marines))
        
        return list_select_islands
        


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Data Structures used:
        - List: To store the instance of islands.
        - List: To store the money each number of crew makes.
        Complexity Analysis:
        - Best Case: O(C * logN) C is the number of crew, N is the number of islands, becuase crew is constant, every ieration
            will reduce the number of islands possible to select by nearlly half. Similar as select_islands. The conplexity 
            update the list all with O(1) complexity.
        - Worst Case: O(C * N) C is the number of crew, N is the number of islands, if the crew is very large, it have to 
            iterate all the islands. The conplexity update the list all with O(1) complexity.
        """
        money_maked = []
        for index, crew_left in enumerate(crew_numbers):
            money_maked.append(0)
            for island in self.islands:
                if crew_left <= island.marines:
                    money_maked[index] += island.money*crew_left/island.marines
                    break
                else:
                    crew_left -= island.marines
                    money_maked[index] += island.money

        return money_maked

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Data Structures used:
        - List: To store the instance of islands.
        Algorithm used:
        - Binary Search: To find the index of the island in the list with Worst Case O(logN) complexity.
        Complexity Analysis:
        - Best Case and Worst case: O(logN) N is the number of islands, get the index used binary search with O(logN) complexity.
            the update the island with O(1) complexity.
        """
        index = binary_search(self.islands_ratio, island.marines/island.money)
        self.islands[index].money = new_money
        self.islands[index].marines = new_marines

        return None

#main
if __name__ == "__main__":
    a = Island("A", 400, 100)
    b = Island("B", 300, 150)
    c = Island("C", 100, 5)
    d = Island("D", 350, 90)
    e = Island("E", 300, 100)
    # Create deepcopies of the islands
    islands = [
        Island(a.name, a.money, a.marines),
        Island(b.name, b.money, b.marines),
        Island(c.name, c.money, c.marines),
        Island(d.name, d.money, d.marines),
        Island(e.name, e.money, e.marines),
    ]
    nav = Mode1Navigator(islands, 200)
    print(nav.islands_ratio)