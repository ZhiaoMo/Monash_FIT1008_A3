from island import Island
from algorithms.binary_search import binary_search
from algorithms.mergesort import mergesort

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        

        self.islands = mergesort(islands, key=lambda x: x.marines/x.money)
        self.islands_ratio  = [i.money/i.marines for i in self.islands]
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        if len(self.islands) == 0:
            return []
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
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
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