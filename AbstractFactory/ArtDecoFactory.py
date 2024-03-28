from .AbstractFurnitureFactory import AbstractFurnitureFactory
from Product.Chair import Chair
from Product.Sofa import Sofa
from Product.Table import Table

class ArtDecoFactory(AbstractFurnitureFactory):
    
    def create_furniture(self):
        return ArtDecoChair(), ArtDecoTable(), ArtDecoSofa()

class ArtDecoChair(Chair):

  def design(self):
    print("Designing an Art Deco chair")

class ArtDecoTable(Table):

  def design(self):
    print("Designing an Art Deco table")

class ArtDecoSofa(Sofa):

  def design(self):
    print("Designing an Art Deco sofa")

 