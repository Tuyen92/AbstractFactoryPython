from .AbstractFurnitureFactory import AbstractFurnitureFactory
from Product.Chair import Chair
from Product.Sofa import Sofa
from Product.Table import Table

class VictorianFactory(AbstractFurnitureFactory):

  def create_furniture(self):
    return VictorianChair(), VictorianTable(), VictorianSofa()

class VictorianChair(Chair):

  def design(self):
    print("Designing a Vitorian chair")

class VictorianTable(Table):

  def design(self):
    print("Designing a Vitorian table")

class VictorianSofa(Sofa):

  def design(self):
    print("Designing a Vitorian sofa")