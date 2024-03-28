from .AbstractFurnitureFactory import AbstractFurnitureFactory
from Product.Chair import Chair
from Product.Sofa import Sofa
from Product.Table import Table

class ModernFactory(AbstractFurnitureFactory):

  def create_furniture(self):
    return ModernChair(), ModernTable(), ModernSofa()

class ModernChair(Chair):

  def design(self):
    print("Designing a Modern chair")

class ModernTable(Table):

  def design(self):
    print("Designing a Modern table")

class ModernSofa(Sofa):

  def design(self):
    print("Designing a Modern sofa")