from Bio import SeqIO



path1="/home/davidfm/Py/Curso-Python-2/Archivos/sample.fastq"
#guardar ids de records bajo umbral
mala_calidad = []
umbral = 40
for record in SeqIO.parse(path, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
    if (promedio < umbral):
        mala_calidad.append((promedio, record.id))


path2="/home/davidfm/Py/Curso-Python-2/Archivos/aichi.gb"
from Bio import SeqIO
for gb_record in SeqIO.parse(path2, "genbank"):
    print('ID', gb_record.id)
    print('Secuencia', str(gb_record.seq)[0:30],'...')
    print('Longitud', len(gb_record))

for annotation, value in gb_record.letter_annotations.items():
	print(annotation,value)

