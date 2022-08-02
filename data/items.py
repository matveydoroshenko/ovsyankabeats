from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    price: int


link = Item(
    id=1,
    title="Доступ к курсу",
    price=1,
)

items = (link,)
