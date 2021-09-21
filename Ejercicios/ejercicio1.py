#obtener orf de la siguiente sequencia AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

import Bio.Seq
import Bio.SeqUtils

sequence = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
codon_inicio = Seq("ATG")

pos_iniciales = nt_search(str(sequencia), codon_inicio)

for i in range(1, len(pos_iniciales)):
	sec_prot = secuencia[i:]
	proteina = seq_prot.translate(to_stop = True)

print(proteina)

#ejercicio avanzado 'elegir la cadena protéica más larga (tomando en cuenta forward y reverse)'
