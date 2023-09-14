import pydicom

# Substitua 'seu_arquivo_dicom.dcm' pelo caminho para o arquivo DICOM que você deseja ler.
arquivo_dicom = 'SPECT_1h.dcm'

# Lê o arquivo DICOM
ds = pydicom.dcmread(arquivo_dicom)

ds.PatientName = "JOAQUIM SEXO"
ds.PatientID = "66666"

ds.saveas("foto.dcm")
# Exibe os metadados
print(ds)


