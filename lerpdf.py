# Bibliotecla para ler o documento
# pip install pypdf2
import PyPDF2 
  
# Abrindo o arquivo .pdf
pdf = 'arquivo.pdf'
pdfFileObj = open(pdf, 'rb') 
  
# Criando o objeto pdfReader para a classe PyPDF2
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# Printando o número de págias
print('Qtd paginas', pdfReader.numPages) 
  
# Começando da página 0 e index 0
pageObj = pdfReader.getPage(0) 

# Printando o conteudo extraido do pdf  
print(pageObj.extractText()) 
  
# Fechando o leitor 
pdfFileObj.close()