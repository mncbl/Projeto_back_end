import os
import pydicom
from flask import Flask, jsonify, request

# Criar o aplicativo API
app = Flask(__name__)

# Diretório para armazenar os arquivos DICOM enviados
upload_dir = 'uploads'

if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Função para obter os metadados do arquivo DICOM
def obter_metadados(arquivo_dicom):
    try:
        # Lê o arquivo DICOM
        ds = pydicom.dcmread(arquivo_dicom)
        n2 = ds.PatientName = "anonimo"
        n3 = ds.PatientID = "anonimo"
        n4 = ds.StudyDescription = "anonimo"
        n5 = ds.StudyDate = "anonimo"
        n6 = ds.PatientSex = "anonimo"

        # Coleta os metadados desejados
        metadados = {
            "PatientName": str(n2),
            "PatientID": n3,
            "StudyDescription": n4,
            "StudyDate": n5,
            "PatientSex": n6,
        }

        return jsonify(metadados)
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para enviar um arquivo DICOM e obter metadados
@app.route('/foto1', methods=['POST'])
def consultar_metadados():
    try:
        # Verifica se um arquivo DICOM foi enviado na solicitação
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo DICOM enviado"})

        file = request.files['file']

        # Verifica se o arquivo tem uma extensão DICOM
        if file.filename == '' or not file.filename.endswith('.dcm'):
            return jsonify({"error": "Arquivo inválido. Envie um arquivo DICOM (.dcm)"})

        # Salva o arquivo no diretório de upload
        uploaded_file_path = os.path.join(upload_dir, file.filename)
        file.save(uploaded_file_path)

        # Obtém os metadados do arquivo DICOM
        return obter_metadados(uploaded_file_path)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
