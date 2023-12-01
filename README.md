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
      1. O usuário baixa o software
      2. Após baixar o arquivo o usuário deve descompacta o arquivo
[Baixe Aqui o Arquivo](https://github.com/mncbl/Projeto_back_end/files/13516656/Software.zip)

https://github.com/mncbl/Projeto_back_end/assets/101721101/5acfa16a-b789-4396-a28a-fde692c518b9

## 2. O usuário deve abrir o software em sua IDE

      1. O usuário deve inicializar a IDE.
      2. Após inicializar sua IDE deve-se abrir o software dentro da IDE.
      3. Verifique se está semelhante a imagem abaixo.

[Imagem de demonstração](https://github.com/mncbl/Projeto_back_end/assets/101721101/6448c4fd-852a-4a45-a37a-964246b43f20)

   ## 3. Instalar bibliotecas do software

         1. Inicializar o Powersheel ou Prompt de Comando (cmd) no caminho da pasta do software
         Ex: C:\Users\nome_usuario\Desktop\Projeto_back_end-main
         2. Após inicializar Powersheel ou Prompt de Comando (cmd) no endereco pasta do arquivo copie o comando abaixo de video e cole na liha de comando 
         3. Aguarde a instalação das bibliotecas e verifique se a instalação foi concluida

   ### Comando para direcionar caminho do arquivo
      cd C:\endereco\arquivo   
      
   ### Comando de Instalação bibliotecas
      pip install -r requirements.txt

   ### Comando para verificar o arquivo
      ls


