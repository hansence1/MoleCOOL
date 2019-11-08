import numpy as np
import pytest
import molecool

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H']
    
    calculated_mass = molecool.molecule.calculate_molecular_mass(symbols)

    actual_mass = molecool.data.atomic_weights['C'] + molecool.data.atomic_weights['H'] +\
         molecool.data.atomic_weights['H'] + molecool.data.atomic_weights['H']
    
    assert actual_mass == calculated_mass