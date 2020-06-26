# Importando o método canvas da biblioteca reportlab (para saber mais sobre os métodos clique aqui);
# pip install reportlab
from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        # Canvas.Canvas(arquivo.pdf) cria um objeto canvas que irá gerar um arquivo pdf com o nome e local inserido. No exemplo armazenamos o objeto na variável pdf;
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            # A função drawString(y,x,texto) utiliza na folha do pdf um plano cartesiano com eixos X e Y (a página possui 595.27 de largura e 841.89 de altura no padrão A4). Então basicamente demos uma posição y = 247 e x = 700 para centralizar na tela, depois para cada nome,idade na lista iremos escrever cada um começando na posição 700 e descrescendo o x toda vez que terminar de escrevar uma linha com o nome e a idade;    
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        # pdf.setTitle(titulo) adicionará um título no pdf;
        pdf.setTitle(nome_pdf)
        # pdf.setFont(Nome da font, tamanho) irá selecionar a fonte e o seu tamanho para os itens;
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de borracha atualizada')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
# pdf.Save() salvará as modificações feitas no caminho especificado do objeto canvas.Canvas();
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

# Criamos uma variável chamada lista do tipo dicionário inserindo alguns valores;
lista = {'Gabriel': '20', 'Martinis': '24', 'Dantas': '22','Maikon':'29 '}

# Invocamos a função GeneratePDF(lista) passando a variável lista como argumento;
GeneratePDF(lista)
