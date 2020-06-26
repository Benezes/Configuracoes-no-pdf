# Bibliotecla para ler o documento
import PyPDF2 
  
# Abrindo o arquivo .pdf
pdf = 'arquivo.pdf'
pdfFileObj = open(pdf, 'rb') 
  
# Criando o objeto pdfReader para a classe PyPDF2
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# atribuindo  o número de págias a uma variavel
qtdpaginas = pdfReader.numPages 
  
# Começando da página 0 e index 0
pageObj = pdfReader.getPage(0) 

# Atribuindo o texto extraido a uma variavel  
texto_extraido = pageObj.extractText()

# Fechando o leitor 
pdfFileObj.close()

# Criando o documento .txt
arq = open("arquivoPDF.txt", "w")

# Escrevendo valores nele
arq.write(texto_extraido)

#para inserir quebra de linha
arq.write("\n")

# Fechando o arquivo .txt
arq.close
