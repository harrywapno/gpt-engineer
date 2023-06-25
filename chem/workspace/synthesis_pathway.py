from typing import List
from chemical_compound import ChemicalCompound

class SynthesisPathway:
    def __init__(self, starting_material: ChemicalCompound, final_product: ChemicalCompound):
        self.starting_material = starting_material
        self.intermediates = []
        self.final_product = final_product

    def add_intermediate(self, intermediate: ChemicalCompound):
        self.intermediates.append(intermediate)
