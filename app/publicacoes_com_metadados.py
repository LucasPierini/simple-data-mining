# python --version: 3.6.8


class Publicacao:
    def __init__(self, conteudo, metadados):
        self.conteudo = conteudo
        self.metadados = metadados


publicacoes = [
    Publicacao(
        conteudo="""
        N  ##2073874-23.2019.8.26.0000##  -  Processo  Digital.  Peticoes  para  juntada  devem  ser  apresentadas  exclusivamente  
         por meio eletronico, nos termos do artigo 7 da Res. 551/2011 - Agravo de Instrumento - Piracicaba - Agravante: M. C. da  
         S. (Menor) - Agravada: S. M. de E. - Magistrado(a) Dora Aparecida Martins - Deram provimento ao recurso. V. U.  - AGRAVO  
         DE INSTRUMENTO. DECISAO AGRAVADA QUE INDEFERIU A TUTELA PARA COMPELIR O MUNICIPIO A EFETIVACAO DA  
         MATRICULA  DA  IMPETRANTE  EM  CRECHE,  PROXIMA  DA  RESIDENCIA,  EM  PERIODO  INTEGRAL.  REFORMA  CABIVEL.  
         INTELIGENCIA DOS ARTIGOS 205, 208, IV, E 211, Paragrafo 2, CONSTITUICAO FEDERAL, E DOS ARTIGOS 53, V, 54, IV, E 208, III,  
         ESTATUTO  DA  CRIANCA  E  DO ADOLESCENTE.  PERIODO  INTEGRAL  QUE TEM  O  CONDAO  DE  PROPICIAR  A  CRIANCA  
         AMBIENTE  SEGURO  E  ADEQUADO  PARA  SEU  DESENVOLVIMENTO,  ALEM  DE  POSSIBILITAR  AOS  PAIS  REALIZACAO  
         DE  ATIVIDADE  LABORATIVA  REGULAR.  MULTA  DIARIA  IMPOSTA  EX  OFFICIO  EM  R$  100, 00,  EM  HOMENAGEM  AOS  
         PRINCIPIOS  DA  RAZOABILIDADE  E  PROPORCIONALIDADE,  COM  VISTAS  A  CONSECUCAO  DE  SUA  FINALIDADE,  
         CUMPRIR A OBRIGACAO IMPOSTA. RECURSO PROVIDO. - Advs: Defensoria Publica do Estado de Sao Paulo (OAB: 99999/ 
         DP) - Rodrigo Prado Marques (OAB: 270206/SP) (Procurador) - Richard Alex Montilha da Silva (OAB: 193534/SP) (Procurador)  
         - Gilvania Rodrigues Cobus (OAB: 135517/SP) (Procurador) - Palacio da Justica - Sala 309
        """,
        metadados={
            'AGRAVANTE': [
                'M. C. DA S. (MENOR)',
            ],
            'AGRAVADA': [
                'S. M. DE E.'
            ],
            'ADV': [
                'DEFENSORIA PUBLICA DO ESTADO DE SAO PAULO (OAB: 99999/ DP)',
                'RODRIGO PRADO MARQUES (OAB: 270206/SP) (PROCURADOR)',
                'RICHARD ALEX MONTILHA DA SILVA (OAB: 193534/SP) (PROCURADOR)',
                'GILVANIA RODRIGUES COBUS (OAB: 135517/SP) (PROCURADOR)',
                'PALACIO DA JUSTICA',
                'SALA 309',
            ]
        },
    ),
    Publicacao(
        conteudo="""
        NO. PROCESSO......: ##201901007657## 
        PROCESSO ORIGEM..: 201988701392 
        PROCEDENCIA.......: 1 JUIZADO ESPECIAL CIVEL E CRIMINAL DE SOCORRO 
        RELATOR.......: DRA. LIVIA SANTOS RIBEIRO 
        MEMBRO.......: DR. ALDO DE ALBUQUERQUE MELLO 
        MEMBRO.......: DR. PABLO MORENO CARVALHO DA LUZ 
        RECORRENTE.......: OMNI FINANCEIRA 
        ADVOGADO.......: NEILDES ARAUJO AGUIAR DI GESU - OAB: 217897/SP 
        RECORRIDO.......: MARIA IRLANEIDE DE JESUS LEANDRO 
        ADVOGADO.......: GABRIEL MANHAES SILVA - OAB: 1082-A-/SE 
        EMENTA: 
        VOTO/EMENTA: RECURSO INOMINADO DA PARTE DEMANDADA. DIREITO DO CONSUMIDOR. NEGATIVACAO POR DEBITO ORIGINADO DE RELACAO CONTRATUAL 
        NAO RECONHECIDA. ONUS PROBATORIO RELATIVO A EXISTENCIA DO CONTRATO DO FORNECEDOR. INTELIGENCIA DO ART. 373, II E Paragrafo 1, DO CPC E DO ART. 14, Paragrafo 
        3,   DO   CDC.
        """,
        metadados={
            'RELATOR': ['DRA. LIVIA SANTOS RIBEIRO'],
            'MEMBRO': [
                'DR. ALDO DE ALBUQUERQUE MELLO',
                'DR. PABLO MORENO CARVALHO DA LUZ',
            ],
            'RECORRENTE': ['OMNI FINANCEIRA'],
            'ADVOGADO': [
                'NEILDES ARAUJO AGUIAR DI GESU - OAB: 217897/SP',
                'GABRIEL MANHAES SILVA - OAB: 1082-A-/SE',
            ],
            'RECORRIDO': ['MARIA IRLANEIDE DE JESUS LEANDRO'],
        },
    ),
    Publicacao(
        conteudo="""
        Proc.  ##0247795-20.2017.8.19.0001##  -  RENATO  RIBEIRO  GAUDIOSO  E  OUTRO  (Adv(s).  Dr(a).  HELIO  VILLELA  DUPLAN  
         (OAB/RJ-043838) X KRAFT FOODS BRASIL LTDA E OUTRO (Adv(s). Dr(a). FELIPE ZORZAN ALVES (OAB/SP-182184), Dr(a). JORGE  
         ANDRE FERREIRA MARQUES (OAB/RJ-056947), Dr(a). JORGE ROBSON ALVES DE OLIVEIRA (OAB/RJ-092653)  Despacho: Intime-se  
         pessoalmente a parte autora para dar regular andamento ao feito no prazo de 5 dias sob pena de extincao e baixa
        """,
        metadados={
            'AUTOR': ['RENATO RIBEIRO GAUDIOSO E OUTRO'],
            'REU': ['KRAFT FOODS BRASIL LTDA E OUTRO'],
            'ADV': [
                'HELIO VILLELA DUPLAN (OAB/RJ-043838)',
                'FELIPE ZORZAN ALVES (OAB/SP-182184)',
                'JORGE ANDRE FERREIRA MARQUES (OAB/RJ-056947)',
                'JORGE ROBSON ALVES DE OLIVEIRA (OAB/RJ-092653)',
            ]
        },
    ),
    Publicacao(
        conteudo="""            
        ##8000412-39.2017.8.05.0014## Procedimento Do Juizado Especial Civel 
        Jurisdicao: Araci 
        Autor: Pedro Mateus De Santana 
        Advogado: Tassia Rebecca Freitas Mota Almeida (OAB:0033935/BA) 
        Advogado: Leon Ramiro Silva E Silva (OAB:0027797/BA) 
        Reu: Banco Do Brasil /sa 
        Advogado: Marcos Caldas Martins Chagas (OAB:0047104/BA) 
        Intimacao: 
        JUIZO DE DIREITO DA COMARCA DE ARACI- BAHIA 
        Processo n ##8000412-39.2017.8.05.0014## 
        Haja vista o retorno dos autos, intimem-se as partes, por seus Procuradores, no prazo de 15 (quinze) dias, para requererem o  
        que entenderem necessario. 
        Por fi m, em homenagem aos principios de economia e de celeridade processuais, atribuo a este Despacho FORCA DE MANDA- 
        DO DE INTIMACAO/CITACAO, o que dispensa a expedicao de mandados ou quaisquer outras diligencias. 
        Findo o prazo, a conclusao. 
        Araci, 03 de junho de 2019. 
        Manuela Rodrigues Fernandes 
        Juiza de Direito Designada 
        PODER JUDICIARIO 
        TRIBUNAL DE JUSTICA DO ESTADO DA BAHIA 
        V DOS FEITOS DE REL DE CONS CIV E COMERCIAIS DE ARACI 
        INTIMACAO
        """,
        metadados={
            'ADVOGADO': [
                "MARCOS CALDAS MARTINS CHAGAS (OAB:0047104/BA)",
                "TASSIA REBECCA FREITAS MOTA ALMEIDA (OAB:0033935/BA)",
                "LEON RAMIRO SILVA E SILVA (OAB:0027797/BA)",
            ],
            'AUTOR': ["PEDRO MATEUS DE SANTANA"],
            'REU': ["BANCO DO BRASIL /SA"],
        },
    ),
    Publicacao(
        conteudo="""
            00013 - ##0009241-62.2017.8.13.0002## 
            Exequente: Lindeia Bernardes Zica Pires; 
            Executado: Luciene Aparecida Martins Fernandes 
            Intimacao. Prazo de 0005 dia(s). Fica o procurador 
            da parte exequente intimada para que, no prazo de 
            05 (cinco) dias, forneca o endereco atualizado de sua 
            cliente. Adv - Rafael Richard Melo Paiva, Cleonan 
            Humberto de Oliveira, Marcos da Costa Resende.
        """,
        metadados={
            'EXEQUENTE': [
                'LINDEIA BERNARDES ZICA PIRES'
            ],
            'EXECUTADO': [
                'LUCIENE APARECIDA MARTINS FERNANDES'
            ],
            'ADV': [
                'RAFAEL RICHARD MELO PAIVA',
                'CLEONAN HUMBERTO DE OLIVEIRA',
                'MARCOS DA COSTA RESENDE',
            ]
        },
    ),
    Publicacao(
        conteudo="""
        AGRAVO DE INSTRUMENTO (202) N ##5005262-25.2017.4.03.0000## 
        AGRAVANTE: COMPANHIA EXCELSIOR DE SEGUROS 
        Advogados do(a) AGRAVANTE: DENIS ATANAZIO - SP229058-A, MARIA EMILIA GONCALVES DE RUEDA - PE23748-A 
        AGRAVADO: EVA MARIA FURLANETTO RUFFO, GUILHERME SAVIO, ISABEL GREGIO DE PAULA, JOAO 
        CARLOS MARQUIORI, JOSE DORIVAL FERRARI 
        Advogado do(a) AGRAVADO: LUIZ CARLOS SILVA - SP168472-A 
        Advogado do(a) AGRAVADO: LUIZ CARLOS SILVA - SP168472-A 
        Advogado do(a) AGRAVADO: LUIZ CARLOS SILVA - SP168472-A 
        Advogado do(a) AGRAVADO: LUIZ CARLOS SILVA - SP168472-A 
        Advogado do(a) AGRAVADO: LUIZ CARLOS SILVA - SP168472-A 
        VISTA - CONTRARRAZOES 
        Certifico que os presentes autos acham-se com vista ao(s) recorrido(s) para apresentar(em) contrarrazoes ao(s) recurso(s) 
        especial(ais) e/ou extraordinario(s) interposto(s), nos termos do artigo 1.030 do Codigo de Processo Civil. 
        Sao Paulo, 14 de agosto de 2019 
        Boletim - Decisoes Terminativas Nro 7629/2019 
        DIVISAO DE AGRAVO DE INSTRUMENTO  
        SECAO DE PROCEDIMENTOS DIVERSOS - RCED 
        DECISAO(OES) PROFERIDA(S) PELA VICE-PRESIDENCIA  
        RECURSO(S) ESPECIAL(IS) / EXTRAORDINARIO(S)
        """,
        metadados={
            'ADVOGADO': [
                'LUIZ CARLOS SILVA - SP168472-A',
                'DENIS ATANAZIO - SP229058-A',
                'MARIA EMILIA GONCALVES DE RUEDA - PE23748-A',
            ],
            'AGRAVANTE': [
                'COMPANHIA EXCELSIOR DE SEGUROS'
            ],
            'AGRAVADO': [
                'EVA MARIA FURLANETTO RUFFO',
                'GUILHERME SAVIO',
                'ISABEL GREGIO DE PAULA',
                'JOAO CARLOS MARQUIORI',
                'JOSE DORIVAL FERRARI',
            ],
        },
    ),
]


if __name__ == '__main__':
    print('Quantidade de Publicações: %d' % publicacoes.__len__())
