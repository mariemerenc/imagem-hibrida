# Instruções

- Siga fielmente a entrada e a saída solicitadas.

# Tarefa 7

Nesta tarefa você deverá implementar a técnica de imagens híbridas (https://vision.csee.wvu.edu/classes/cs674-f17/assignments/assignment1/OlivaTorralb_Hybrid_Siggraph06.pdf) [1]

- imagemHibrida.py:

	- **entrada:** o nome de dois arquivos de imagens. Ambas devem possuir mesmo tamanho.
		- Caso acrescente parâmetros adicionais, descrevê-los na seção parâmetros deste README.md
	- **saída:** exibir na tela a imagem híbrida, construída conforme a seguir (começo da seção 2 de [1]):
		- A hybrid image (H) is obtained by combining two images (I1 and I2), one filtered with a low-pass filter (G1) and the second one filtered with a high-pass filter (1-G2): H = I1G1 + I2(1-G2), the operations are defined in the Fourier domain.
	- **observação:** detalhes adicionais descritos no artigo são opcionais.

# Parâmetros


# Referências

[1] Oliva, Aude, Antonio Torralba, and Philippe G. Schyns. "Hybrid images." ACM Transactions on Graphics (TOG) 25.3 (2006): 527-532.
