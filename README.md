# 🔰 Introdução
Projeto de Anonimização e Segmentação de imagens DICOM(.dcm) através da proposta da empresa Dosimagem filiado a universidade IBMEC-RJ. 

# 👱 Colaboradores

1. Arthur Camaz 
2. Bruno Rocha 
3. Bruno Xavier 
4. Caio Medeiros 
5. Ian Amoedo
6. Pedro Oliveira
7. Matheus Noricia

# 🧰 Ferramentas

1. Pydicom : Biblioteca utilizada para vizualizar os metadados
2. Insominia : API utilzada para anonimizar os metadados
3. 3dSlicer : Software utilizado para vizualizar imagem nearly raw raster data(.nnrd) segmentada em 3D
4. ImageJ : Software utilizado para vizuliar os metadados e imagem no formato DICOM(.dcm) 
5. SympleITK : Biblioteca utilzada para segmentar a imagem DICOM(.dcm)
6. Trello : Software utilizado para organização de tarefas.

# História do Projeto
   
## 💥 Proposta do Trabalho

A empresa Dosimagem realizou um pedido aos alunos da IBMEC realizarem um software em Python com o objetivo de anonimizar e segmentar imagens DICOM. O projeto teve como proposta ampliar os conhecimentos dos alunos e ampliar novos horizontes para a empresa Dosimagem utilizar no prática.

### O projeto foi dividido em dois casos no qual denominamos como : 

- `Problema 1`: Os laboratórios que solicitam serviços de dosimetria à Dosimagem precisam anonimizar os metadados das imagens submetidas, em respeito à Lei Geral de Proteção de Dados (LGPD). Essa tarefa toma tempo dos responsáveis pelos laboratórios e atrasa o início do trabalho da Dosimagem, uma vez que nem todos os seus clientes têm o conhecimento necessário para realizar tal tarefa.
Portanto, há a necessidade de criação de uma API REST que possa receber imagens no formato DICOM e seja capaz de anonimizar seus metadados, tais como o nome do paciente, sua data de nascimento e quaisquer outros metadados que possam ser considerados sensíveis.       

- `Problema 2`: A Dosimagem utiliza a ferramenta 3D Slicer para realizar as segmentações dos órgãos. No 3D Slicer, há uma ferramenta chamada TotalSegmentatorAI, que é capaz de realizar a segmentação de forma automática dos órgãos em poucos minutos.
A ideia, neste caso, seria desenvolver uma API REST que possa receber imagens no formato DICOM e seja capaz de segmentá-las automaticamente.
      
## 📋Organização da equipe

Com a alta demanda de tarefas no percurso deste projeto decidimos utilizar a metodoligia de Scrum/Kanban na organização das nossas tarefas para buscar melhorias e vizualizar as tarefas que estavam pendentes ou finalizadas.

[Link para Scrum/Kanban](https://trello.com/b/oZ4yhTO5/back-end)

# 🤔 Como utilizar na Prática ?

## 0. O usuário deve possuir na máquina os seguintes softwares instalados:   
  - `IDE` A IDE utilizada do projeto foi o VSCODE porém pode utilizar a IDE de seu gosto. [Link para Dowload ](https://code.visualstudio.com/download)
  -  `Insomnia` [Link para Download ](https://insomnia.rest/download)
  -  `3DSlicer` [Link para Download ](https://download.slicer.org)
  -  `Python` [Link para Dowload ](https://www.python.org/downloads/)

## 1. O usuário deve instalar e descompactar o software na máquina.
Esta etapa tem como objetivo instalar o software do nosso projeto junto com as imagens DICOM de teste.

   - `1`. O usuário baixa o software
   - `2`. Após baixar o arquivo o usuário deve descompacta o arquivo
   - 
[Baixe Aqui o Arquivo](https://github.com/mncbl/Projeto_back_end/files/13531238/Software.zip)

### Video de Demonstração

https://github.com/mncbl/Projeto_back_end/assets/101721101/5acfa16a-b789-4396-a28a-fde692c518b9

## 2. O usuário deve abrir o software em sua IDE

Esta etapa tem como objetivo inicializar o software na IDE na qual esta utilzando. 

   - `1`. O usuário deve inicializar a IDE.
   - `2`. Após inicializar sua IDE deve-se abrir o software dentro da IDE.
   - `3`. Verifique se está semelhante a imagem abaixo.

### Imagem de Demonstração

![Imagem de demonstração](https://github.com/mncbl/Projeto_back_end/assets/101721101/6448c4fd-852a-4a45-a37a-964246b43f20)

## 3. Instalar bibliotecas do software

Esta etapa tem como objetivo instalar bibliotecas no qual a linguagem Python não possue como padrão, podendo da um erro ao inicializar o programa caso não realize este passo.

   - `1`. Inicializar o Powersheel ou Prompt de Comando (cmd) no caminho da pasta do software.
     Ex: C:\Users\nome_usuario\Desktop\Projeto_back_end-main.
   - `2`. Após inicializar Powersheel ou Prompt de Comando (cmd) no endereco pasta do arquivo copie o comando abaixo de video e cole na liha de comando. 
   - `3`. Aguarde a instalação das bibliotecas e verifique se a instalação foi concluida.

   ### Comando para direcionar caminho do arquivo
      cd C:\endereco\arquivo   
      
   ### Comando de Instalação bibliotecas
      pip install -r requirements.txt

   ### Comando para verificar os arquivos
      ls

https://github.com/mncbl/Projeto_back_end/assets/101721101/36b35e61-b945-4ddc-92d4-072ab96ba0a5

## 4. Inicializar a Software para a anonimização dos metadados e configurar o Insomia para o software

Esta etapa tem como objetivo inicializar a API de anonimização e configurar o software Insomnia na utilização da API.

   - `1`. Inicializar/Compilar o arquivo meta.py. 
   - `2`. Após inicializar o progrma execute o aplicativo Insomnia. 
   - `3`. Após inicializar o Insomnia clique na opção New Collection e de um nome a sua Collection.
   - `4`. Após criar seu Prompt clique no nome do seu arquivo (no video Anonimização)localizado no canto superior esquerdo da tela.
   - `5`. Após clicar no nome do seu Prompt clique na opção Import.
   - `6`. Após clicar na opção Import baixe e importe o arquivo destacado abaixo para configurar o Prompt utilzado no projeto.

[Arquivo Prompt Insomina](https://github.com/mncbl/Projeto_back_end/files/13531454/Insomnia_2023-11-30.zip)

### Imagem demonstração console

[Imagem de demonstração ao arquivo meta.py incializado no console](https://github.com/mncbl/Projeto_back_end/assets/101721101/e9b8da0f-ca99-4538-855d-130bc8c19ab2)

### Video de Demonstração

https://github.com/mncbl/Projeto_back_end/assets/101721101/8832e7ef-325b-49b1-aa1a-ff704bd7d09a

## 5. Anonimizar dados sensíveis de determinada imagem DICOM
Esta etapa tem como objetivo realizar a operação para anonimizar dados sensíveis da imagem. 

   - `1`.  Clicar no filter POST. 
   - `2`.  Após clicar no botao filter POST, clique no quadrado onde possui um arquivo como demostração de Exemplo (SPECT_1h.dcm).
   - `3`.  Após clicar no arquivo como demostração de Exemplo (SPECT_1h.dcm), seleciona um arquivo DICOM no qual o usuário possua ou utilize um dos arquivos de exemplo na pasta do software(Os arquivos testes estao na pasta chamada inputs).
   - `4`.  Após selecionar um arquivo DICOM no qual o usuário possua ou utilize um dos arquivos de exemplo na pasta do software(Os arquivos testes estao na pasta chamada inputs),selecione o botão Send para gerar uma imagem DICOM com alguns dados sensíveis anonimizados.

   Observação : Se olhar o console no qual o arquivo meta.py será gerada estas informações e a criação da imagem DICOM anonimizada onde sera armazenada na pasta uploads do software
   
### Video Demonstração

https://github.com/mncbl/Projeto_back_end/assets/101721101/197ec963-59fd-4a33-abd3-696cc6807688
 
### Respsota do Console
   
![Passo 5.1 ](https://github.com/mncbl/Projeto_back_end/assets/101721101/38a7c49b-a9f1-4970-b54e-48625d3f94d5)

### Arquivo Gerado na pasta Uploads
   
![Passo 5 2](https://github.com/mncbl/Projeto_back_end/assets/101721101/8820ac62-a5d5-43d8-b5a3-c898d8263e63)

