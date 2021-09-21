#Estructura 3d de proteínas
#
#Ocupamos difracción de ondas para conocer aberturas entre átomos
#
#Simulaciones PhET: nos simula el proceso de difracción de manera gráfica
#https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interfernece_en.html
#
#Es necesario ajustar la longitud de onda al tamaño del objeto a observar 
#
#Dado que necesitamos una estructura ordenada y repetida para generar una difracción útil
#es necesario cristalizar proteínas para aplicar este método
#
#Dados los tamaños de los atomos, las ondas que se pueden difractar bien sobre ellos son
#Rayos X
#
#Proteín Data Bank - base de datos de estructura tridimensional de proteínas. Tiene
#archivos PDB
#
#En BioPython tendremos objetos Structure que seguirá un formado SMRCA:
#-structure
#-model
#-chain
#-residue
#¿Como generarlo? creamos objeto PDBParser con un QUIET (evita que se mencionen errores (que casi siempre hay))

from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure("prot_1fat", "/home/davidfm/Py/Curso-Python-2/Archivos/1fat.pdb")


#Podemos ver cuantos modelos hay en este objeto

print(struc.child_dict) #Atributo que nos devuelve un diccionario de los modelos que tiene la proteina
print(struc.child_list) #Lo mismo pero en lista

#En el 'header' encontraremos toda la información de metadatos

print(struc.header.keys())
print(struc.header['structure_method']) #Dado que es un diccionario se pueden acceder a sus elementos por sus llaves
print(struc.header['resolution'])


struc_1kwc = parser.get_structure("prot_1kwc", "/home/davidfm/Py/Curso-Python-2/Archivos/1kcw.pdb")

print(struc_1kwc.header['structure_method'])
print(struc_1kwc.header['resolution'])
print(struc_1kwc.header.items())
print(struc_1kwc.get_id())



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#