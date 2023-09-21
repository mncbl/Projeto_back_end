import pydicom
from flask import Flask, jsonify

# Criar o aplicativo API
app = Flask(__name__)

# Substitua 'seu_arquivo_dicom.dcm' pelo caminho para o arquivo DICOM que você deseja ler.
arquivo_dicom = 'SPECT_1h.dcm'

# Função para obter os metadados do arquivo DICOM
def obter_metadados():
    try:
        # Lê o arquivo DICOM
        ds = pydicom.dcmread(arquivo_dicom)
        n2=ds.PatientName=" anonimo"  
        n3=ds.PatientID=" anonimo "  
        n4=ds.StudyDescription=" anonimo "  
        n5=ds.StudyDate=" anonimo "  
        n6=ds.PatientSex=" anonimo "  
        
        # Coleta os metadados desejados
        metadados = {
            "PatientName": str(n2),
            "PatientID": n3,
            "StudyDescription":n4,
            "StudyDate": n5,
            "PatientSex": n6 ,
      
        }
        
        return jsonify(metadados)
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para consultar metadados
@app.route('/foto1', methods=['GET'])
def consultar_metadados():
    return obter_metadados()

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
