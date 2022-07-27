# Testing ground

class Item:
    def __init__(self, itemID):
        self.itemID = itemID

        if(itemID == 1):
            self.name = "Box"
        elif(itemID == 2):
            self.name = "Table"
        elif(itemID == 3):
            self.name = "Orange"


if __name__ == "__main__":
    print("Hello World")
