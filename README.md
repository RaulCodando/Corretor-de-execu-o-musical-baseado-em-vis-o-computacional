# Corretor de postura para violonistas baseado em computer vision

Sistema de visão computacional e machine learning para avaliação de postura e posicionamento de violonistas em tempo real.

O sistema combina detecção de pose corporal, rastreamento de mãos e detecção do violão para extrair features estruturais e avaliar a qualidade da execução instrumental.

## Requisitos

- Python 3.11.x

### Dependências principais

```bash
mediapipe==0.10.9
opencv-python==4.13.0.92
numpy==2.4.4
pandas==3.0.2
scikit-learn==1.8.0
matplotlib==3.10.9
```

## Tecnologias

- MediaPipe Pose → detecção de pose corporal
- MediaPipe Hands → detecção de mãos e dedos
- YOLO → detecção do violão
- OpenCV → captura de vídeo em tempo real
- Scikit-learn → modelo de classificação
- Pandas → organização do dataset

## Treinamento do modelo

1. Coleta de imagens/vídeos de violonistas
2. Extração de landmarks com MediaPipe Pose e Hands
3. Detecção do violão com YOLO
4. Extração de features (ângulos, distâncias, posições relativas)
5. Construção do dataset estruturado (CSV com Pandas)
6. Treinamento do modelo com Scikit-learn

## Sistema em tempo real

Input (câmera)
    ↓
MediaPipe Pose
    ↓
MediaPipe Hands
    ↓
YOLO (violão)
    ↓
Extração de features
    ↓
Modelo de ML
    ↓
Feedback de postura

## Features

- ângulos articulares (cotovelo, punho, ombro)
- posição relativa das mãos
- posição do violão
- distâncias entre mãos e instrumento
- alinhamento corporal