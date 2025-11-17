
# Imagens Híbridas com Filtros de Frequência 

Este projeto implementa a geração de imagens híbridas, uma técnica que combina componentes de baixa frequência de uma imagem com componentes de alta frequência de outra. Dependendo da distância de visualização, o observador percebe uma imagem ou outra.

A implementação utiliza Transformada de Fourier (FFT) para aplicar filtros passa-baixa e passa-alta do tipo Gaussiano no domínio da frequência.

Este projeto foi desenvolvido na disciplina DIM0141 - Visão Computacional.

## Bibliotecas e pacotes
```
opencv-python
numpy
matplotlib
```
## Execução

O script recebe duas imagens como parâmetros:

```bash
python imagemHibrida.py imagem1.jpg imagem2.jpg
```



## Observações

* A técnica de imagens híbridas é inspirada no trabalho de Oliva, Torralba & Schyns (2006).

* A percepção varia conforme distância e escala.

* Funciona melhor com imagens bem alinhadas e de conteúdo complementar.
