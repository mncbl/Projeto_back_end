import pydicom

# Substitua 'seu_arquivo_dicom.dcm' pelo caminho para o arquivo DICOM que você deseja ler.
arquivo_dicom = 'SPECT_1h.dcm'

# Lê o arquivo DICOM
ds = pydicom.dcmread(arquivo_dicom)

ds.PatientSex = "   "

ds.save_as('foto.dcm')
o = 'foto.dcm'
o = pydicom.dcmread(o)
print(o)




