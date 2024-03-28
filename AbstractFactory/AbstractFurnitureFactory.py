from abc import abstractmethod

class AbstractFurnitureFactory():

  @abstractmethod
  def create_furniture(self):
    pass