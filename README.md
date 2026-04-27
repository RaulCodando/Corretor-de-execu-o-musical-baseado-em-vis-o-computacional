# Corretor de postura para violonistas baseado em computer vision
Sistema baseado em visão computacional e aprendizagem de máquina para avaliação de postura e posicionamento de violonistas em tempo real.

Este projeto utiliza matplotlib para a criação e treinamento do modelo classificador, YOLO para detecção e métrica do violão, MediaPipe para a detecção e estimativa da postura e posicionamento de mãos e dedos do violonista e OpenCV para entrada de vídeo via câmera.

O sistema analisa:
- Postura geral
- Posicionamento das mãos
- Relação com o violão

## Tecnologias

- MediaPipe Pose → detecção de landmarks do corpo
- MediaPipe Hands → detecção de mãos e dedos
- YOLO → detecção do violão
- OpenCV → captura e exibição de vídeo
- Scikit-learn → classificação de postura
- Pandas para registro de features e manipulação das bases de dados

##Arquitetura da construção do classificador

A criação do classificador segue o seguinte pipeline:

- Banco de imagens coletadas para uso no treinamento
- Extração dos dados da postura com MediaPipePose
- Extração dos dados do posicionamento das mãos com MediaPipeHands
- Extração dos dados de métrica do violão com YOLO
- Criação da base de dados contendo as features extraídas, utilizando Pandas
- Criação e treinamento do modelo utilizando Scikit-Learn

##Arquitetura do sistema principal

## Arquitetura

O sistema segue o seguinte pipeline:

Input (vídeo/imagem)
    ↓
Detecção de pose (MediaPipe)
    ↓
Detecção de mãos (MediaPipe)
    ↓
Detecção de violão (YOLO)
    ↓
Extração de features
    ↓
Classificação (ML)
    ↓
Feedback ao usuário

##Fluxo

## Fluxo

1. Capturar frame da câmera
2. Processar pose com MediaPipe
3. Detectar mãos
4. Detectar violão com YOLO
5. Extrair features:
   - ângulos
   - distâncias
   - posições relativas
6. Enviar para o modelo de ML
7. Exibir resultado na tela
