import pydicom

# Substitua 'seu_arquivo_dicom.dcm' pelo caminho para o arquivo DICOM que você deseja ler.
arquivo_dicom = 'SPECT_1h.dcm'

# Lê o arquivo DICOM
ds = pydicom.dcmread(arquivo_dicom)

ds.PatientName = "None"
ds.PatientID = "None"
ds.PatientBirthDate = "None"
ds.PatientSex = "None"
ds.PatientAge = "None"
# PatientSize e PatientWeight ja estão anonimizados

# Exibe os metadados
print(ds)

ds.save_as('foto.dcm')
o = 'foto.dcm'
o = pydicom.dcmread(o)
print(o)


