# item.py
class Item:
    """
    Objet ou checklist dans un lieu.
    
    Attributes:
        name (str)
        description (str)
        completed (bool)
    """
    def __init__(self, name, description, weight = 0.0):
        self.name = name
        self.description = description
        self.weight = weight

    def use(self):
        if self.completed:
            print(f"{self.name} a déjà été utilisé.")
        else:
            self.completed = True
            print(f"Vous utilisez {self.name} : {self.description}")