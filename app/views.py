from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from app.models import *
from app.publicacoes_com_metadados import *
import re, json

# Lista de Entidades Possíveis
entity_list = [ 'ADV', 'ADVS',
                'ADVOGADA', 'ADVOGADO',
                'AGRAVADA', 'AGRAVADO',
                'AGRAVANTE',
                'AUTOR',
                'EXEQUENTE',
                'EXECUTADO',
                'MEMBRO',
                'RECORRENTE',
                'RECORRIDO',
                'RELATOR',
                'REU',
            ]

# Lista com os padrões de texto
pattern_list = [
    re.compile(r'(^\s*(N?)(\s*)##([0-9\-\.]+)##(\s*)-([\s\w])*\.){1}', re.IGNORECASE), # Primeiro Padrão (Serve para o 1º conteúdo)
    re.compile(r'(^[\s]*[\w\.\s]+\:[\s]*##[0-9\-\.]+##[ \t]*[\n]+)|(^\s*##[0-9\-\.]+##[\s\S]*?\n(\s*\w+\:))', re.IGNORECASE), # Segundo Padrão (Serve para o 2º e para o 4º conteúdo)
    re.compile(r'^[\s]*[\w\.]*[\s]*##[0-9\-\.]+##[\s]*-[\s]*[\w]*[\s\S]*(\sX\s){1}[\w\s]+', re.IGNORECASE), # Terceiro Padrão (Serve para o 3º conteúdo) 
    re.compile(r'^\s*\d*[\s\-]*##[0-9\-\.]+##[ \t]*\n+\s*\w*\:{1}', re.IGNORECASE), # Quarto Padrão (Serve para o 5º conteúdo)
    re.compile(r'^[\s\S]*?(\sN\s){1}##[0-9\-\.]+## *\n+\s*\w*\:{1}', re.IGNORECASE), # Quinto Padrão (Serve para o 6º conteúdo)
] 

def get_text_pattern(content):
    ''' Essa função recebe o conteúdo do texto e busca na lista de padrões qual tipo de grupo este texto pertence '''

    # Retorna o índice do padrão na pattern_list (começando do 1)
    for i, pattern in enumerate(pattern_list, start=1):
        if re.search(pattern, content):
            return i
    
    # Retorna False se não encontrar o padrão
    return False


def create_metadata(content):
    ''' Essa função cria o dicionário Metadados da classe Publicacao '''

    # Pega o padrão de texto baseado no conteúdo
    text_pattern = get_text_pattern(content)
    metadados = {}

    # Verifica se há o padrão de texto
    if text_pattern:

        # Primeiro padrão de texto
        if text_pattern == 1:
            for entity in entity_list:

                if entity != 'ADVS':
                    metadata_pattern = r'(?<=' + entity + r'\:)[\s\S^-]*?(?=[\s]*-)'
                    metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                    metadata = re.findall(metadata_pattern, content)

                # Tratamento especial para Advs
                else:
                    metadata_pattern = r'(?<=' + entity + r'\:)[\s\S]*'
                    metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                    metadata = re.search(metadata_pattern, content)
                    metadata = re.split(r'[-,]', metadata.group())
                    
                if metadata:
                    # Chama função recorrente de criação de metadata
                    create_metadata_list(metadados, metadata, entity)


        # Segundo padrão de texto
        elif text_pattern == 2:
            for entity in entity_list:

                metadata_pattern = entity + r'[\.]*\:([\s\S]*?)(?=\n)'
                metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                metadata = re.findall(metadata_pattern, content)

                if metadata:
                    # Chama função recorrente de criação de metadata
                    create_metadata_list(metadados, metadata, entity)


        # Terceiro padrão de texto
        elif text_pattern == 3:
            # Este não usa nenhum termo direto para entidades, então requer um tratamento especial

            # Autor
            metadata_pattern = r'(?<=\d##)[\s\S]+?(?=\()'
            metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
            metadata = re.findall(metadata_pattern, content)

            if metadata:
                for i in range(len(metadata)):
                    metadata[i] = re.sub(r'^[\s]*-[\s]*', '', metadata[i])

                create_metadata_list(metadados, metadata, 'AUTOR')

            # Reu
            metadata_pattern = r'(?<=\sX\s)[\s\S]+?(?=\()'
            metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
            metadata = re.findall(metadata_pattern, content)

            if metadata:
                create_metadata_list(metadados, metadata, 'REU')

            # ADVS
            metadata_pattern = r'((?<=Adv\(s\)\.)[\s\S]*(?=\sX\s)|(?<=Adv\(s\)\.)[\s\S]*?(?=[\w]*\:))'
            metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
            metadata = re.findall(metadata_pattern, content)
    
            if metadata:

                # Pega a lista gerada e dá um split em cada uma (caso tenha mais de um advogado em cada lista)
                aux = []
                for m in metadata:
                    m = re.split(r'[,;]', m)
                    for n in m:
                        n = re.sub(r'Dr\(a\).', '', n)
                        aux.append(n)

                metadata = aux

                create_metadata_list(metadados, metadata, 'ADV')

 
        # Quarto padrão de texto
        elif text_pattern == 4:
            for entity in entity_list:

                # ADV recebe um tratamento especial neste caso
                if entity == 'ADV' or entity == 'ADVS':
                    metadata_pattern = r'(?<=' + entity + r')\s*[\-\:]\s*[\s\w\,]*'
                    metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                    metadata = re.search(metadata_pattern, content)
                    
                    if metadata:
                        metadata = metadata.group()
                        metadata = re.sub(r'^\s*-\s*', '', metadata)
                        metadata = re.split(r'[\,\;\-]', metadata)
                    
                    if metadata:
                        # Chama função recorrente de criação de metadata
                        create_metadata_list(metadados, metadata, entity)

                else:
                    metadata_pattern = entity + r'\:[\s\S]*?[\;\n\.]'
                    metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                    metadata = re.findall(metadata_pattern, content)
                    
                    if metadata:
                        # Chama função recorrente de criação de metadata
                        create_metadata_list(metadados, metadata, entity)
                    

        elif text_pattern == 5:
            for entity in entity_list: 

                metadata_pattern = r'(?<!do\(a\) )' + entity + r'\:[\w\s\-\,]*(?=\n[ \t]*([\w\s\(\)]*\:|VISTA))'
                metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                metadata = re.search(metadata_pattern, content)

                if metadata:
                    metadata = metadata.group()
                    metadata = re.sub(r'^[\w]*\:', '', metadata)
                    metadata = re.split(r',', metadata) 
                    
                    create_metadata_list(metadados, metadata, entity)
                    
                metadata_pattern = r'((?<=Advogado do\(a\)\s)' + entity + r'\:[\w\s\-\,]*(?=\n[ \t]*([\w\s\(\)]*\:|VISTA))|(?<=Advogados do\(a\)\s)' + entity + r'\:[\w\s\-\,]*(?=\n[ \t]*([\w\s\(\)]*\:|VISTA)))'

                metadata_pattern = re.compile(metadata_pattern, re.IGNORECASE)
                metadata = re.search(metadata_pattern, content)

                if metadata:
                    metadata = metadata.group()
                    metadata = re.sub(r'^[\w]*\:', '', metadata)
                    metadata = re.split(r',', metadata) 
                    
                    create_metadata_list(metadados, metadata, 'Advogado')


    # Envia uma mensagem de alerta caso nenhum metadado tenha sido encontrado
    if not metadados:
        metadados['Erro'] = ['Nenhum Metadado Encontrado!']
 
    return metadados


def create_metadata_list(metadata_dict, metadata, entity):

    # Cria uma lista de metadados da entidade
    if entity not in metadata_dict:
        metadata_dict[entity] = []

    for m in metadata:
        m = re.sub(r'[\n\t]', '', m) # Remove as quebras de linha
        m = m.strip() # Remove os espaços do início / fim da string
        m = m.upper() # Coloca os dados em uppercase

        if m not in metadata_dict[entity]:
            metadata_dict[entity].append(m)
            

class Main(View):
    template_name = 'app/index.html'

    def get(self, request): 
        # Recria os metadados das publicações do arquivo publicacoes_com_metadados.py a partir de seu conteúdo (apenas para fins de teste mesmo)
        pub2 = []
        for publicacao in publicacoes:
            pub2.append( Publicacao( publicacao.conteudo, create_metadata(publicacao.conteudo) ) ) 

        return render(request, self.template_name, {'publicacoes': pub2} )
