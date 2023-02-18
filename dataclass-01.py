from dataclasses import dataclass, field
from pprint import pprint

@dataclass
class ThingData:
	name: str
	weight: int
	price: float = 0
	dims: list = field(default_factory=list)

# __init__(), __repr__(), __eq__() - dataclass auto make these methods

pprint(ThingData.__dict__)
print()

td_1 = ThingData("Учебник по Python", 100, 1024)
td_2 = ThingData("Учебник ООП", 80, 512)
td_3 = ThingData("Учебник ООП", 80, 512)

print("td_1 == td_2:", td_1 == td_2)
print("td_2 == td_3:", td_2 == td_3)

