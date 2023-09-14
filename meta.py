import pydicom

# Substitua 'seu_arquivo_dicom.dcm' pelo caminho para o arquivo DICOM que você deseja ler.
arquivo_dicom = 'SPECT_1h.dcm'

# Lê o arquivo DICOM
ds = pydicom.dcmread(arquivo_dicom)

ds.PatientName = "None"
ds.PatientID = "None"

# Exibe os metadados
print(ds)


