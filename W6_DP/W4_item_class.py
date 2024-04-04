# Item class to make objects for knacpsack problem
class Item():

    def __init__(self,weight: int, value: int) -> None:
        self.weight = weight
        self.value = value

    def get_weight(self) -> int:
        return self.weight
    
    def get_value(self) -> int:
        return self.value 
    
    def __str__(self) -> str:
        return f"Item weight: {self.weight} kg\nItem value: ${self.value}"



if __name__ == "__main__":
    item1 = Item(25,100)
    print(item1)