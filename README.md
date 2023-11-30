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

# 🤔 Como utilizar o Projeto ?

## 1. O usuário deve possuir na máquina na qual esta utilizando os seguintes softwares instalados:   
  - `IDE`: A IDE utilizada do projeto foi o VSCODE porém pode utilizar a IDE de seu gosto. ([Link para Dowload VSCODE](https://code.visualstudio.com/download)
  -    
