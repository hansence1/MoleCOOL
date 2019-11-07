import numpy as np

def open_pdb(file_location):
    """
    Open and read atom coordinates from a PDB file.

    The pdb file must specify the atom elemnt in the last column, and follow
    the conventions outline int the PDB format specification

    Parameters
    ----------
    file_location : str
        The location of the pdb file

    Returns
    -------
    symbols : list
        The atomic symbols from the PDB file
    coords : np.ndarray
        the atomic coordinates from the PDB file
    """
    
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    
    return symbols, coords
