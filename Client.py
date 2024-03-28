from AbstractFactory.ArtDecoFactory import ArtDecoFactory
from AbstractFactory.VictorianFactory import VictorianFactory
from AbstractFactory.ModernFactory import ModernFactory

def create_and_use_furniture(furniture_factory):
  chair, table, sofa = furniture_factory.create_furniture()  # Or "Table", "Sofa"
  chair.design()
  table.design()
  sofa.design()

def get_furniture_choice():
    while True:
        choice = input("Choose furniture collection (ArtDeco, Victorian, Modern): ")
        if choice in ("ArtDeco", "Victorian", "Modern"):
            return choice
        else:
            print("Invalid choice. Please try again.")

furniture_choice = get_furniture_choice()
if furniture_choice:
  if furniture_choice == "ArtDeco":
    furniture_factory = ArtDecoFactory()
  elif furniture_choice == "Victorian":
    furniture_factory = VictorianFactory()
  else:
    furniture_factory = ModernFactory()
  create_and_use_furniture(furniture_factory)
else:
  print("Exiting program due to invalid input.")