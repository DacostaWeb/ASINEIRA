# -*- coding: utf-8 -*-
"""Gera as três experiências do dossier a partir de um só conteúdo.
O conteúdo é o que a cliente escreveu em "mudancas cliente.png" — nada foi
inventado. Onde ela ainda não escreveu, fica marcado como por escrever."""
import io, os

REPO = r"C:\Users\Eduardo\Documents\design\sineira\ASINEIRA"
DOSSIER = os.path.join(REPO, "dossier")

# --------------------------------------------------------------------------
# CONTEÚDO (da cliente)
# --------------------------------------------------------------------------

INTRO = {
    "num": "01", "kicker": "Introdução", "titulo": "a Sineira",
    "sub": "Associação &amp; Espaço Cultural",
    "paras": [
        "Criada em 2025, a Sineira — Associação Cultural pretende colaborar com as demais "
        "estruturas existentes a nível nacional e internacional, para dar resposta às "
        "necessidades e interesses da comunidade artística local e a todo o público interessado "
        "em usufruir das actividades culturais e sociais por si promovidas.",
        "Surge como um colectivo, mas também como espaço físico, em Vila do Conde. "
        "Requalificando o complexo arquitectónico da antiga Igreja de Retorta, pretende-se aí "
        "criar um ponto de encontro <em>intergeracional</em>, de conexão com as <em>artes</em> "
        "e com a <em>natureza</em>.",
    ],
}

MISSAO = {
    "num": "02", "kicker": "Missão", "titulo": "Missão e objetivos",
    "itens": [
        "Fomentar a <em>criação e divulgação</em> de projetos artísticos, através de residências artísticas e performances;",
        "Reforçar a <em>colaboração</em> entre artistas e entre estes e a comunidade local;",
        "Promover a <em>valorização</em> do património cultural e natural de Vila do Conde;",
        "Apoiar a <em>literacia</em> artística, promovendo atividades de <em>mediação e formação</em>, tais como workshops, cursos intensivos e aulas regulares;",
        "Dinamizar um <em>festival</em> anual de dança e música.",
    ],
}

IDADES = {
    "kicker": "Para quem", "titulo": "Programas para todas as idades",
    "texto": "A Sineira proporciona atividades para público geral e especializado, "
             "dedicando-se a todas as faixas etárias, através de diferentes propostas.",
    "pills": ["Infância", "Jovens", "Adultos", "Séniores"],
}

ACTIVIDADES = {
    "num": "03", "kicker": "Actividades", "titulo": "Actividades",
    "disciplinas": "Dança · Música · Teatro · Arquitectura · Artes plásticas · Artes visuais · Fotografia",
    "colunas": [
        ("Artistas", ["Aulas regulares", "Workshops", "Cursos intensivos",
                      "Residências artísticas", "Espetáculos"]),
        ("Comunidade", ["Aulas regulares", "Workshops", "Campo de férias",
                        "Sessões de cinema", "Produtos locais", "Experiências na natureza"]),
    ],
}

ESPACO = {
    "num": "04", "kicker": "O espaço", "titulo": "Retorta — Vila do Conde",
    "texto": "Área aproximada: 18.000 m². Um complexo a requalificar — igreja, casa, mata e "
             "clareira — para formação, criação e apresentação.",
    "itens": ["Estúdio / palco", "Igreja: espaço multiusos",
              "Alojamento: programa de residências artísticas", "Restauração",
              "Estacionamento", "Floresta: percursos de lazer e pedagógicos",
              "Clareira: espaço para festival"],
    "foto": ("vista-aerea.jpg", "Implantação aérea do complexo da antiga Igreja de Retorta",
             "Implantação · 18.000 m²"),
}

ACESSOS = {
    "num": "05", "kicker": "Acessos", "titulo": "Acessos",
    "tabela": [
        ("Metro Santa Clara / Vila do Conde", "bicicleta 5 min", "a pé 15 min"),
        ("Centro histórico de Vila do Conde", "bicicleta 10 min", "a pé 30 min"),
        ("Praias de Vila do Conde", "bicicleta 20 min", "a pé 60 min"),
        ("Metro Trindade / Porto", "metro 40 min", "60 min"),
        ("Aeroporto Francisco Sá Carneiro", "carro 20 min", "50 min"),
    ],
    "texto": "Retorta fica entre o rio, a floresta e a cidade. Metro, centro histórico, "
             "praias e aeroporto estão a minutos.",
    "foto": ("vila-do-conde.jpg", "Vila do Conde, o rio Ave e o Atlântico",
             "Vila do Conde · o rio Ave e o Atlântico"),
}

REQUALIFICACAO = {
    "num": "06", "kicker": "Requalificação", "titulo": "Plano de requalificação",
    "itens": [
        "Levantamento topográfico e arquitectónico",
        "Projecto de arquitectura e especialidades",
        "Construção: redes de esgotos, água, electricidade e telecomunicações",
        "Sistema de aquecimento / arrefecimento",
        "Construção de acessos e estacionamento",
        "Execução de janelas",
        "Recuperação da porta principal da igreja",
        "Recuperação dos altares da igreja",
        "Execução de pavimentos",
        "Tratamento de paredes",
        "Criação de instalações sanitárias",
        "Recuperação do telhado da casa do padre",
        "Abertura de vão (proscénio) e demolição de laje",
        "Pinturas · iluminação interior e exterior",
        "Projecto de paisagismo e arranjos exteriores",
    ],
    "fotos": [
        ("scene-estudio.jpg", "Proposta: estúdio de dança com plateia", "Proposta · estúdio de dança com plateia"),
        ("scene-aerea.jpg", "Proposta: vista aérea nocturna do complexo", "Proposta · vista aérea nocturna"),
    ],
}

FASEAMENTO = {
    "num": "07", "kicker": "Faseamento", "titulo": "Faseamento da intervenção",
    "itens": [
        "<strong>Fase 1</strong> — igreja, jardim e estacionamento",
        "<strong>Fase 2</strong> — antiga casa do padre",
        "<strong>Fase 3</strong> — antiga catequese",
        "<strong>Fase 4</strong> — equipamento de restauração, eventos e melhoria do estacionamento",
        "<strong>Fase 5</strong> — área de expansão futura (limites a verificar)",
    ],
    "foto": ("faseamento.jpg", "Planta de faseamento da intervenção na antiga Igreja de Retorta",
             "Planta de faseamento"),
}

MECENATO = {
    "num": "08", "kicker": "Mecenato", "titulo": "Plano de apoio e mecenato",
    "texto": "A requalificação da antiga Igreja de Retorta e o programa artístico da Sineira "
             "pedem companhia. Pessoas, empresas e instituições podem apoiar o projecto — e "
             "fazer parte da comunidade que está a nascer.",
    "itens": [
        "Acesso gratuito a todos os eventos",
        "Desconto na frequência de aulas regulares, workshops e cursos intensivos",
        "Criação de dinâmica socio-cultural e económica em Vila do Conde",
        "Publicidade através de cartazes e demais materiais de comunicação",
        "Benefícios fiscais (Lei do Mecenato Cultural)",
    ],
    "legal": "a Sineira — Associação Cultural · NIF 518858359. Apoios enquadráveis no Estatuto "
             "dos Benefícios Fiscais (mecenato cultural).",
    "niveis": [
        ("01", "Pessoas", "Amigo",
         "Entra na comunidade. Eventos, descontos e um lugar no que está a nascer em Retorta.", False),
        ("02", "Empresas e instituições", "Patrocínio",
         "Texto por escrever pela associação.", True),
        ("03", "Instituições e associações", "Parceiro",
         "Associação nomeada à dinâmica cultural de Vila do Conde — cartazes, site, eventos e território.", False),
    ],
}

TERRITORIO = {
    "num": "09", "kicker": "Território", "titulo": "Parcerias e apoios",
    "grupos": [
        ("Parcerias (à data)", ["Curtas de Vila do Conde", "Centro Ciência Viva"]),
        ("Apoios (à data)", ["Junta de Freguesia de Retorta e Tougues",
                             "Câmara Municipal de Vila do Conde"]),
    ],
    "proximidade_titulo": "Pontos de interesse na proximidade",
    "proximidade": ["Centro Ciência Viva", "Pólo de investigação", "ESMAD",
                    "Centro gimnodesportivo", "Campo Rio Ave Futebol", "Escola Sanches",
                    "Escola Saul Dias", "Clube Fluvial Vilacondense",
                    "Rede ciclovia (futuramente)", "Praia fluvial (futuramente)"],
}

INTERVENCAO = {
    "num": "10", "kicker": "Intervenção", "titulo": "Intervenção",
    "texto": "O trabalho já começou. A nave ganhou pavimento novo; os altares e o arco dourado "
             "aguardam recuperação.",
    "fotos": [
        ("nave-2025.jpg", "Nave da igreja antes do pavimento", "Antes · nave"),
        ("nave-2026.jpg", "Nave com pavimento novo, em obra", "Durante · pavimento novo"),
        ("arco.jpg", "Interior em obra, visto através do arco", "Interior · arco e pavimento em execução"),
        ("altares.jpg", "Pormenor dos altares a recuperar", "Altares — recuperação prevista no plano"),
    ],
}

CONTACTOS = {
    "num": "11", "kicker": "Contactos", "titulo": "Mais informações",
    "links": [("asineira.pt", "https://asineira.pt"), ("Instagram", "https://instagram.com")],
    "legal": "a Sineira — Associação Cultural · NIF 518858359",
    "moradas": ["Sede: Av. General Humberto Delgado 103 – 3.º I, 4480-905 Vila do Conde",
                "Igreja: Rua da Igreja, Retorta, 4480-353 Vila do Conde"],
    "email": "ola@asineira.pt",
}

CONVITE = {
    "kicker": "Convite", "titulo": "Vem ver o sítio. Vem apoiar o que falta.",
    "texto": "Este dossier é um convite: à visita, ao mecenato, à parceria. A antiga Igreja de "
             "Retorta está a tornar-se casa para as artes — e precisa de quem queira fazer parte.",
}

MAILTO = "mailto:ola@asineira.pt?subject=Apoiar%20a%20Sineira"

# --------------------------------------------------------------------------
# PEÇAS COMUNS
# --------------------------------------------------------------------------

def li(itens, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return "<ul%s>\n%s\n</ul>" % (c, "\n".join("  <li>%s</li>" % i for i in itens))

def figura(f, cls="shot"):
    src, alt, cap = f
    return ('<figure class="%s">\n'
            '  <img src="../assets/%s" alt="%s" loading="lazy">\n'
            '  <figcaption>%s</figcaption>\n'
            '</figure>' % (cls, src, alt, cap))

def tabela(linhas):
    corpo = "\n".join(
        "    <tr><td>%s</td><td>%s</td><td>%s</td></tr>" % l for l in linhas)
    return ('<table class="acessos">\n'
            '  <thead><tr><th>Destino</th><th>Modo A</th><th>Modo B</th></tr></thead>\n'
            '  <tbody>\n%s\n  </tbody>\n</table>' % corpo)

MARCA = '''<svg class="svg-defs" aria-hidden="true">
  <symbol id="mark-sineira" viewBox="0 0 382 387">
    <path fill="var(--blue)" d="M95.7804 387L382 110.293L0 0L95.7804 387Z"></path>
    <path fill="var(--cream)" d="M237.388 200.34C247.689 213.363 261.205 214.741 278 206.656C294.744 198.596 298.733 188.514 293.636 177.859C287.97 166.014 278.519 164.239 250.934 170.39C207 180.098 190.348 170.391 180.948 150.741C168.813 125.373 179.487 99.0424 213.836 82.5088C252.358 63.9658 277.644 77.3509 289.904 97.6398L258.295 112.855C252.495 104.628 242.906 97.2765 224.201 106.28C211.468 112.409 206.307 121.384 211.25 131.717C216.092 141.839 224.216 142.977 250.269 137.146C297.241 126.807 314.026 138.102 323.842 158.622C336.554 185.197 325.231 213.078 286.876 231.541C250.048 249.268 221.95 240.417 205.779 215.554L237.388 200.34Z"></path>
    <path fill="var(--cream)" d="M127.809 268.327C123.481 279.019 118.021 294.985 117.576 297.957L87.9668 285.895C87.9997 283.319 89.7491 277.138 90.8443 274.28C84.2336 278.937 73.674 283.105 53.8757 275.039C26.8839 264.043 22.704 241.605 29.7557 224.188C40.1131 198.606 65.3714 195.148 98.1927 208.519L114.168 215.028L116.946 208.165C120.179 200.181 120.493 191.163 106.12 185.307C93.0352 179.976 87.9124 184.388 83.1947 191.939L53.7216 179.932C63.4814 160.661 82.3208 149.524 116.279 163.582C146.184 175.99 157.746 194.386 146.924 221.116L127.809 268.327ZM106.552 233.914L93.9249 228.77C75.2484 221.161 66.0077 224.06 61.6246 234.886C58.3332 243.015 60.5334 251.886 71.6733 256.424C91.3705 264.449 99.3509 251.7 105.357 236.865L106.552 233.914Z"></path>
  </symbol>
</svg>'''

def cabecalho(nome):
    return '''<header class="topo">
  <a class="topo__marca" href="/">
    <svg viewBox="0 0 382 387" aria-hidden="true"><use href="#mark-sineira"></use></svg>
    <span>a Sineira</span>
  </a>
  <p class="topo__titulo">Dossier de apresentação</p>
  <a class="topo__versao" href="../">%s</a>
</header>''' % nome

def pagina(slug, nome, css, corpo):
    return '''<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>a Sineira — Dossier · %s</title>
<meta name="description" content="Dossier de apresentação e mecenato da a Sineira — requalificação da antiga Igreja de Retorta, Vila do Conde.">
<link rel="icon" href="../../favicon.ico" type="image/x-icon">
<link rel="stylesheet" href="../base.css">
<style>
%s
</style>
</head>
<body class="exp exp--%s">

%s

%s

</body>
</html>
''' % (nome, css, slug, MARCA, corpo)

# --------------------------------------------------------------------------
# BASE — a linguagem a que chegámos no site
# --------------------------------------------------------------------------

BASE_CSS = '''/* ==========================================================================
   a Sineira — dossier · base partilhada pelas três experiências
   A paleta, a tipografia e a margem são as do site.
   ========================================================================== */

:root {
  --blue:  #003C78;
  --cream: #F2E7A9;
  --gold:       #D8B44A;
  --gold-light: #F0DFA0;
  --gold-deep:  #A8842B;

  --font: Helvetica, Arial, sans-serif;
  --gutter: 30px;
  --medida: 62ch;          /* medida de leitura */
}

@media (max-width: 760px) { :root { --gutter: 18px; } }

*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; }
html, body { margin: 0; overflow-x: clip; }

/* Nenhuma barra de scroll à vista, como no site. */
* { scrollbar-width: none; }
*::-webkit-scrollbar { display: none; }

body {
  background: var(--cream);
  color: var(--blue);
  font-family: var(--font);
  text-wrap: pretty;
  font-size: 16px;
  line-height: 1.55;
}

h1, h2, h3, h4, p, ul, ol, figure, table, blockquote { margin: 0; }
ul { list-style: none; padding: 0; }
img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
a:hover { text-decoration: underline; }
em { font-style: italic; font-weight: 700; }

.svg-defs { display: none; }

/* --- cabeçalho comum --- */

.topo {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 18px;
  height: 62px;
  padding: 0 var(--gutter);
  background: var(--cream);
  border-bottom: 1.5px solid var(--blue);
}
.topo__marca { display: flex; align-items: center; gap: 9px; flex-shrink: 0; }
.topo__marca:hover { text-decoration: none; }
.topo__marca svg { width: 20px; height: auto; }
.topo__marca span { font-weight: 700; font-size: 15px; letter-spacing: -.01em; }
.topo__titulo {
  font-size: 10px; font-weight: 700; letter-spacing: .16em;
  text-transform: uppercase; opacity: .6;
}
.topo__versao {
  margin-left: auto; flex-shrink: 0;
  font-size: 10px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase;
  border: 1.5px solid currentColor; border-radius: 99px; padding: 4px 11px;
}

/* --- peças de texto --- */

.kicker {
  font-size: 10px; font-weight: 700; letter-spacing: .18em;
  text-transform: uppercase; opacity: .65;
}

.lista li { position: relative; padding-left: 1.1em; margin-bottom: .35em; }
.lista li::before { content: "›"; position: absolute; left: 0; font-weight: 700; }

.pills { display: flex; flex-wrap: wrap; gap: 9px; }
.pills li {
  border: 1.5px solid currentColor; border-radius: 99px; padding: 6px 15px;
  font-size: 12px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
}

.botao {
  display: inline-block; margin-top: 26px;
  justify-self: start; align-self: start; width: fit-content;
  border: 1.5px solid currentColor; padding: 12px 22px;
  font-size: 12px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
}
.botao:hover { background: currentColor; text-decoration: none; }
.botao:hover span { color: var(--cream); }
.invertido .botao:hover span { color: var(--blue); }

.legal { font-size: 12px; opacity: .75; margin-top: 20px; max-width: 60ch; }

/* Onde a associação ainda não escreveu o texto. */
.por-escrever {
  border: 1.5px dashed currentColor; padding: 10px 14px;
  font-size: 13px; font-style: italic; opacity: .7;
}

/* --- fotografias --- */

.shot img { width: 100%; height: auto; }
.shot figcaption {
  margin-top: 7px;
  font-size: 9px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
  opacity: .8;
}

/* --- tabela de acessos --- */

.acessos { width: 100%; border-collapse: collapse; font-size: 14px; }
.acessos th, .acessos td {
  padding: 9px 12px 9px 0; text-align: left;
  border-bottom: 1px solid color-mix(in srgb, currentColor 25%, transparent);
}
.acessos th {
  border-bottom-color: color-mix(in srgb, currentColor 55%, transparent);
  font-size: 9px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase;
}
.acessos td:not(:first-child) { white-space: nowrap; }

/* --- bandas invertidas --- */

.invertido { background: var(--blue); color: var(--cream); }

/* --- cartão de amigo, como no site --- */

.cartao-amigo {
  width: min(100%, 300px); aspect-ratio: 1.586; margin-top: 22px; padding: 16px;
  display: flex; flex-direction: column; justify-content: space-between;
  border-radius: 12px; color: var(--blue);
  background: linear-gradient(135deg, var(--gold-deep) 0%, var(--gold) 38%, var(--gold-light) 62%, var(--gold-deep) 100%);
}
.cartao-amigo svg { width: 26px; height: auto; }
.cartao-amigo b { font-size: 17px; font-weight: 700; text-transform: lowercase; letter-spacing: -.025em; }
.cartao-amigo small { font-size: 9px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }


/* --- o espaço identificado sobre a planta --------------------------------
   A cliente tinha uma imagem com cada parte do complexo nomeada por setas.
   Aqui a ideia mantém-se, mas com pontos numerados e legenda ao lado: não se
   sobrepõem uns aos outros e lê-se em qualquer tamanho de ecrã. */

.mapa { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 26px; align-items: start; }
.mapa__figura { position: relative; line-height: 0; border: 1.5px solid currentColor; }
.mapa__figura img { width: 100%; height: auto; }
.mapa__ponto {
  position: absolute; transform: translate(-50%, -50%);
  width: 26px; height: 26px; border-radius: 50%;
  display: grid; place-items: center;
  background: var(--cream); color: var(--blue); border: 1.5px solid var(--blue);
  font-size: 12px; font-weight: 700; line-height: 1;
}
.mapa__legenda { counter-reset: parte; }
.mapa__legenda li {
  position: relative; padding-left: 34px; margin-bottom: 9px;
  font-size: 15px; line-height: 1.35;
}
.mapa__legenda li::before {
  counter-increment: parte; content: counter(parte);
  position: absolute; left: 0; top: -1px;
  width: 24px; height: 24px; border-radius: 50%;
  display: grid; place-items: center;
  border: 1.5px solid currentColor; font-size: 11px; font-weight: 700;
}
.mapa__nota { font-size: 12px; opacity: .75; margin-top: 12px; }

/* A igreja está na parte de cima da fotografia de capa: sem isto, um recorte
   largo e baixo mostra só a calçada. */
.capa img, .abertura img { object-position: 50% 32%; }

@media print {
  .topo { position: static; }
  .exp * { animation: none !important; transition: none !important; }
}
'''


# Posicoes de cada parte sobre a planta, em percentagem da imagem. Vieram da
# imagem "o espaco.png" da cliente e sao aproximadas — faceis de acertar.
PARTES = [(79, 43), (77, 50), (62, 50), (57, 42), (70, 34), (40, 60), (66, 84)]

def mapa_espaco(nota=True):
    src, alt, cap = ESPACO["foto"]
    pontos = "".join(
        '<span class="mapa__ponto" style="left:' + str(x) + '%; top:' + str(y) + '%">'
        + str(i + 1) + '</span>'
        for i, (x, y) in enumerate(PARTES))
    legenda = "\n".join('    <li>' + t + '</li>' for t in ESPACO["itens"])
    extra = ('<p class="mapa__nota">' + cap + '</p>') if nota else ''
    return ('<div class="mapa">\n'
            '  <figure class="mapa__figura"><img src="../assets/' + src + '" alt="' + alt
            + '" loading="lazy">' + pontos + '</figure>\n'
            '  <div><ul class="mapa__legenda">\n' + legenda + '\n  </ul>' + extra + '</div>\n'
            '</div>')

def cabeca(s, tag="h2"):
    """kicker numerado + título"""
    k = s.get("kicker", "")
    n = s.get("num")
    kick = (n + " · " + k) if n else k
    return ('<p class="kicker">' + kick + '</p>\n<' + tag + ' class="titulo">'
            + s["titulo"] + '</' + tag + '>')

def bloco_niveis(cls_cartao=True):
    out = []
    for num, quem, nome, texto, vazio in MECENATO["niveis"]:
        corpo = ('<p class="por-escrever">' + texto + '</p>') if vazio else ('<p>' + texto + '</p>')
        extra = ''
        if nome == "Amigo" and cls_cartao:
            extra = ('\n    <div class="cartao-amigo">'
                     '<svg viewBox="0 0 382 387" aria-hidden="true"><use href="#mark-sineira"></use></svg>'
                     '<div><b>Amigo da Sineira</b><br><small>Cartão de amigo</small></div></div>')
        out.append('  <article class="nivel">\n'
                   '    <p class="kicker">' + num + ' · ' + quem + '</p>\n'
                   '    <h3>' + nome + '</h3>\n    ' + corpo + extra + '\n  </article>')
    return '<div class="niveis">\n' + "\n".join(out) + '\n</div>'

def bloco_actividades():
    cols = []
    for nome, itens in ACTIVIDADES["colunas"]:
        cols.append('  <div>\n    <p class="kicker">' + nome + '</p>\n    '
                    + li(itens, "lista") + '\n  </div>')
    return '<div class="duas">\n' + "\n".join(cols) + '\n</div>'

def bloco_territorio():
    gs = []
    for nome, itens in TERRITORIO["grupos"]:
        gs.append('  <div>\n    <p class="kicker">' + nome + '</p>\n    '
                  + li(itens, "lista") + '\n  </div>')
    gs.append('  <div>\n    <p class="kicker">' + TERRITORIO["proximidade_titulo"]
              + '</p>\n    ' + li(TERRITORIO["proximidade"], "lista") + '\n  </div>')
    return '<div class="tres">\n' + "\n".join(gs) + '\n</div>'

# --------------------------------------------------------------------------
# A — DOCUMENTO
# --------------------------------------------------------------------------

CSS_A = '''
/* Documento: uma coluna larga, secções numeradas, bandas alternadas.
   O mais próximo de um dossier impresso — feito para ler de fio a pavio
   e para imprimir. */

/* Uma coluna centrada na página, mas com o texto encostado à esquerda dentro
   dela — não usar margin-inline:auto nos filhos, que centraria cada bloco. */
.faixa {
  display: grid;
  grid-template-columns: minmax(0, 1100px);
  justify-content: center;
  padding: clamp(48px, 7vw, 96px) var(--gutter);
}
.faixa + .faixa { border-top: 1.5px solid color-mix(in srgb, currentColor 30%, transparent); }
.faixa.invertido + .faixa, .faixa + .faixa.invertido { border-top: none; }

.capa { position: relative; }
.capa img { width: 100%; height: clamp(320px, 62vh, 620px); object-fit: cover; }
.capa__marca {
  position: absolute; right: var(--gutter); bottom: 28px;
  font-size: clamp(38px, 9vw, 104px); font-weight: 700; letter-spacing: -.03em;
  line-height: .8; color: var(--blue);
}

.titulo {
  margin-top: 6px;
  font-size: clamp(30px, 4.6vw, 56px); font-weight: 700; line-height: .95;
  letter-spacing: -.03em; text-transform: uppercase;
}
.faixa p + p, .faixa .titulo + p, .faixa p + ul, .faixa p + .duas,
.faixa p + .tres, .faixa .titulo + ul, .faixa .titulo + .duas,
.faixa .titulo + .tres, .faixa .titulo + table { margin-top: 22px; }
.faixa p, .faixa .lista { max-width: var(--medida); }
.sub { font-size: 18px; margin-top: 14px; }

.duas { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 34px; }
.tres { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 34px; }

.disciplinas {
  font-size: clamp(15px, 1.7vw, 21px); font-weight: 700;
  letter-spacing: .02em; text-transform: uppercase; line-height: 1.35;
}

.galeria { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 22px; margin-top: 30px; }
.faixa .larga { max-width: none; }

.niveis { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 30px; margin-top: 34px; }
.nivel h3 { font-size: 26px; font-weight: 700; text-transform: uppercase; letter-spacing: -.02em; margin: 4px 0 10px; }

.fecho .titulo { font-size: clamp(30px, 5.4vw, 66px); }
'''

def render_a():
    p = []
    p.append(cabecalho("A · Documento"))
    p.append('<div class="capa"><img src="../assets/hero.jpg" alt="Antiga Igreja de Retorta e casa do padre, Vila do Conde">'
             '<p class="capa__marca">a Sineira</p></div>')

    p.append('<section class="faixa" id="intro">' + cabeca(INTRO, "h1")
             + '<p class="sub">' + INTRO["sub"] + '</p>'
             + "".join('<p>' + t + '</p>' for t in INTRO["paras"])
             + '<a class="botao" href="#mecenato"><span>Apoiar o projecto</span></a></section>')

    p.append('<section class="faixa" id="missao">' + cabeca(MISSAO) + li(MISSAO["itens"], "lista") + '</section>')

    p.append('<section class="faixa invertido" id="idades">' + cabeca(IDADES)
             + '<p>' + IDADES["texto"] + '</p>' + li(IDADES["pills"], "pills") + '</section>')

    p.append('<section class="faixa" id="actividades">' + cabeca(ACTIVIDADES)
             + '<p class="disciplinas">' + ACTIVIDADES["disciplinas"] + '</p>'
             + bloco_actividades() + '</section>')

    p.append('<section class="faixa" id="espaco">' + cabeca(ESPACO)
             + '<p>' + ESPACO["texto"] + '</p>'
             + '<div class="larga">' + mapa_espaco() + '</div></section>')

    p.append('<section class="faixa" id="acessos">' + cabeca(ACESSOS)
             + tabela(ACESSOS["tabela"]) + '<p>' + ACESSOS["texto"] + '</p>'
             + '<div class="larga galeria">' + figura(ACESSOS["foto"]) + '</div></section>')

    p.append('<section class="faixa" id="requalificacao">' + cabeca(REQUALIFICACAO)
             + li(REQUALIFICACAO["itens"], "lista")
             + '<div class="larga galeria">' + "".join(figura(f) for f in REQUALIFICACAO["fotos"]) + '</div></section>')

    p.append('<section class="faixa" id="faseamento">' + cabeca(FASEAMENTO)
             + li(FASEAMENTO["itens"], "lista")
             + '<div class="larga galeria">' + figura(FASEAMENTO["foto"]) + '</div></section>')

    p.append('<section class="faixa invertido" id="mecenato">' + cabeca(MECENATO)
             + '<p>' + MECENATO["texto"] + '</p>' + li(MECENATO["itens"], "lista")
             + '<p class="legal">' + MECENATO["legal"] + '</p>'
             + '<a class="botao" href="' + MAILTO + '"><span>Quero apoiar</span></a>'
             + bloco_niveis() + '</section>')

    p.append('<section class="faixa" id="territorio">' + cabeca(TERRITORIO) + bloco_territorio() + '</section>')

    p.append('<section class="faixa" id="intervencao">' + cabeca(INTERVENCAO)
             + '<p>' + INTERVENCAO["texto"] + '</p>'
             + '<div class="larga galeria">' + "".join(figura(f) for f in INTERVENCAO["fotos"]) + '</div></section>')

    p.append('<section class="faixa" id="contactos">' + cabeca(CONTACTOS)
             + li(['<a href="' + u + '">' + n + '</a>' for n, u in CONTACTOS["links"]], "lista")
             + '<p class="legal">' + CONTACTOS["legal"] + '<br>'
             + "<br>".join(CONTACTOS["moradas"]) + '</p>'
             + '<a class="botao" href="mailto:' + CONTACTOS["email"] + '"><span>Escrever-nos</span></a></section>')

    p.append('<section class="faixa invertido fecho">' + cabeca(CONVITE)
             + '<p>' + CONVITE["texto"] + '</p>'
             + '<a class="botao" href="#mecenato"><span>Plano de mecenato</span></a></section>')

    return pagina("a", "A · Documento", CSS_A, "\n\n".join(p))

# --------------------------------------------------------------------------
# B — MOSAICO (a linguagem do site aplicada ao dossier)
# --------------------------------------------------------------------------

CSS_B = '''
/* Mosaico: a grelha de cartões do site, com as fotografias intercaladas.
   Cada secção é um mosaico; os que pedem mais espaço ocupam duas colunas.
   Lê-se por blocos, não de fio a pavio. */

.mosaico {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(max(100% / 3, min(100%, 340px)), 1fr));
  align-items: stretch;
}

.bloco {
  display: flex; flex-direction: column;
  padding: clamp(24px, 2.6vw, 38px) var(--gutter);
  background: var(--cream); color: var(--blue);
}
.bloco--azul { background: var(--blue); color: var(--cream); }
.bloco--largo { grid-column: span 2; }
@media (max-width: 720px) { .bloco--largo { grid-column: auto; } }

.bloco .titulo {
  margin-top: 6px; margin-bottom: 16px;
  font-size: clamp(24px, 2.4vw, 34px); font-weight: 700; line-height: .95;
  letter-spacing: -.03em; text-transform: uppercase;
}
.bloco p + p, .bloco p + ul, .bloco ul + p { margin-top: 14px; }
.bloco p, .bloco li { font-size: 15px; }
.bloco .lista { margin-top: 14px; }

.foto { display: grid; background: var(--blue); min-height: 260px; }
.foto img { width: 100%; height: 100%; object-fit: cover; }
.foto--largo { grid-column: span 2; }
@media (max-width: 720px) { .foto--largo { grid-column: auto; } }

.duas { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 180px), 1fr)); gap: 24px; margin-top: 14px; }
.tres { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr)); gap: 24px; margin-top: 14px; }

.disciplinas { font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: .02em; line-height: 1.4; }

.niveis { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 24px; margin-top: 18px; }
.nivel h3 { font-size: 21px; font-weight: 700; text-transform: uppercase; letter-spacing: -.02em; margin: 4px 0 8px; }

.bloco .botao { margin-top: auto; align-self: flex-start; }
.bloco .legal { margin-top: 16px; }
.acessos { font-size: 13px; }
.acessos th, .acessos td { padding: 7px 10px 7px 0; }

.capa {
  grid-column: 1 / -1; position: relative; display: grid;
  min-height: clamp(300px, 56vh, 560px); background: var(--blue);
}
.capa img { width: 100%; height: 100%; object-fit: cover; }
.capa__marca {
  position: absolute; right: var(--gutter); bottom: 24px;
  font-size: clamp(34px, 8vw, 92px); font-weight: 700; letter-spacing: -.03em;
  line-height: .8; color: var(--blue);
}
.fecho { grid-column: 1 / -1; }
.fecho .titulo { font-size: clamp(26px, 4vw, 52px); }
'''

def bloco(s, azul=False, largo=False, corpo="", tag="h2"):
    cls = "bloco" + (" bloco--azul" if azul else "") + (" bloco--largo" if largo else "")
    inv = ' invertido' if azul else ''
    return ('<section class="' + cls + inv + '">' + cabeca(s, tag) + corpo + '</section>')

def foto_celula(f, largo=False):
    src, alt, cap = f
    cls = "foto" + (" foto--largo" if largo else "")
    return ('<figure class="' + cls + '"><img src="../assets/' + src + '" alt="' + alt + '" loading="lazy"></figure>')

def render_b():
    p = [cabecalho("B · Mosaico"), '<main class="mosaico">']

    p.append('<div class="capa"><img src="../assets/hero.jpg" alt="Antiga Igreja de Retorta e casa do padre, Vila do Conde">'
             '<p class="capa__marca">a Sineira</p></div>')

    p.append(bloco(INTRO, azul=False, largo=True, tag="h1",
                   corpo='<p><strong>' + INTRO["sub"] + '</strong></p>'
                         + "".join('<p>' + t + '</p>' for t in INTRO["paras"])
                         + '<a class="botao" href="#mecenato"><span>Apoiar o projecto</span></a>'))
    p.append(foto_celula(ESPACO["foto"]))

    p.append(bloco(MISSAO, azul=True, corpo=li(MISSAO["itens"], "lista")))
    p.append(bloco(IDADES, azul=False,
                   corpo='<p>' + IDADES["texto"] + '</p>' + li(IDADES["pills"], "pills")))
    p.append(foto_celula(REQUALIFICACAO["fotos"][0]))

    p.append(bloco(ACTIVIDADES, azul=True, largo=True,
                   corpo='<p class="disciplinas">' + ACTIVIDADES["disciplinas"] + '</p>' + bloco_actividades()))

    p.append(bloco(ESPACO, azul=False, largo=True,
                   corpo='<p>' + ESPACO["texto"] + '</p>' + mapa_espaco()))
    p.append(foto_celula(REQUALIFICACAO["fotos"][1]))

    p.append(bloco(ACESSOS, azul=True, largo=True,
                   corpo=tabela(ACESSOS["tabela"]) + '<p>' + ACESSOS["texto"] + '</p>'))
    p.append(foto_celula(ACESSOS["foto"]))

    p.append(bloco(REQUALIFICACAO, azul=False, largo=True, corpo=li(REQUALIFICACAO["itens"], "lista")))
    p.append(bloco(FASEAMENTO, azul=True, corpo=li(FASEAMENTO["itens"], "lista")))
    p.append(foto_celula(FASEAMENTO["foto"]))

    p.append(bloco(MECENATO, azul=True, largo=True,
                   corpo='<p>' + MECENATO["texto"] + '</p>' + li(MECENATO["itens"], "lista")
                         + bloco_niveis() + '<p class="legal">' + MECENATO["legal"] + '</p>'
                         + '<a class="botao" href="' + MAILTO + '"><span>Quero apoiar</span></a>'))

    p.append(bloco(TERRITORIO, azul=False, largo=True, corpo=bloco_territorio()))

    p.append(bloco(INTERVENCAO, azul=False, corpo='<p>' + INTERVENCAO["texto"] + '</p>'))
    for f in INTERVENCAO["fotos"]:
        p.append(foto_celula(f))

    p.append(bloco(CONTACTOS, azul=True, largo=True,
                   corpo=li(['<a href="' + u + '">' + n + '</a>' for n, u in CONTACTOS["links"]], "lista")
                         + '<p class="legal">' + CONTACTOS["legal"] + '<br>'
                         + "<br>".join(CONTACTOS["moradas"]) + '</p>'
                         + '<a class="botao" href="mailto:' + CONTACTOS["email"] + '"><span>Escrever-nos</span></a>'))

    p.append('<section class="bloco bloco--azul invertido fecho">' + cabeca(CONVITE)
             + '<p>' + CONVITE["texto"] + '</p>'
             + '<a class="botao" href="#mecenato"><span>Plano de mecenato</span></a></section>')

    p.append('</main>')
    return pagina("b", "B · Mosaico", CSS_B, "\n\n".join(p))

# --------------------------------------------------------------------------
# C — ESPACO (o sitio primeiro)
# --------------------------------------------------------------------------

CSS_C = '''
/* Espaço: capítulos de ecrã inteiro, cada um encostado ao seguinte. O lugar
   manda — as plantas, as propostas e as fotografias de obra ocupam metade do
   ecrã e o texto encosta-se a elas. É a leitura que a cliente pediu para pôr
   à frente. */

.capitulo {
  min-height: 100svh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: stretch;
  border-top: 1.5px solid color-mix(in srgb, var(--blue) 30%, transparent);
}
.capitulo:first-of-type { border-top: none; }
@media (max-width: 860px) { .capitulo { grid-template-columns: 1fr; min-height: 0; } }

.capitulo__texto {
  display: flex; flex-direction: column; justify-content: center;
  padding: clamp(40px, 6vh, 90px) var(--gutter);
}
.capitulo--invertido .capitulo__texto { background: var(--blue); color: var(--cream); }
.capitulo--espelhado .capitulo__texto { order: 2; }
@media (max-width: 860px) { .capitulo--espelhado .capitulo__texto { order: 0; } }

.capitulo__imagem { display: grid; background: var(--blue); position: relative; min-height: 42svh; }
.capitulo__imagem img { width: 100%; height: 100%; object-fit: cover; }
.capitulo__imagem figcaption {
  position: absolute; left: 0; right: 0; bottom: 0;
  padding: 10px var(--gutter); background: var(--cream); color: var(--blue);
  font-size: 9px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
}
/* As plantas não devem ser cortadas — mostram-se inteiras sobre creme. */
.capitulo__imagem--planta { background: var(--cream); padding: 26px var(--gutter) 46px; }
.capitulo__imagem--planta img { object-fit: contain; }

.titulo {
  margin-top: 8px;
  font-size: clamp(28px, 3.6vw, 52px); font-weight: 700; line-height: .95;
  letter-spacing: -.03em; text-transform: uppercase;
}
.capitulo p, .capitulo .lista, .capitulo table { max-width: 52ch; }
.capitulo .titulo + p, .capitulo .titulo + ul, .capitulo .titulo + table,
.capitulo p + p, .capitulo p + ul, .capitulo p + .duas, .capitulo p + .tres,
.capitulo ul + p, .capitulo .titulo + .duas, .capitulo .titulo + .tres { margin-top: 20px; }
.sub { font-size: 17px; margin-top: 12px; }

.abertura { position: relative; min-height: 100svh; display: grid; }
.abertura img { width: 100%; height: 100%; object-fit: cover; }
.abertura__marca {
  position: absolute; left: var(--gutter); bottom: clamp(30px, 8vh, 80px);
  font-size: clamp(44px, 11vw, 150px); font-weight: 700; letter-spacing: -.035em;
  line-height: .78; color: var(--blue);
}
.abertura__legenda {
  position: absolute; left: var(--gutter); top: 84px;
  font-size: 11px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase;
  color: var(--blue);
}

.duas { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr)); gap: 26px; }
.tres { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 160px), 1fr)); gap: 24px; }
.disciplinas { font-size: clamp(14px, 1.4vw, 18px); font-weight: 700; text-transform: uppercase; letter-spacing: .02em; }
.niveis { display: grid; gap: 20px; margin-top: 22px; }
.nivel h3 { font-size: 22px; font-weight: 700; text-transform: uppercase; letter-spacing: -.02em; margin: 3px 0 8px; }

.tira { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); }
.tira figure { position: relative; display: grid; background: var(--blue); min-height: 40svh; }
.tira img { width: 100%; height: 100%; object-fit: cover; }
.tira figcaption {
  position: absolute; left: 0; right: 0; bottom: 0; padding: 9px 14px;
  background: var(--cream); color: var(--blue);
  font-size: 9px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase;
}

.fecho { padding: clamp(60px, 12vh, 130px) var(--gutter); }
.fecho .titulo { font-size: clamp(30px, 6vw, 82px); max-width: 18ch; }
.fecho p { max-width: 56ch; margin-top: 22px; }
.fecho .lista, .fecho .niveis { margin-top: 22px; }
.fecho--espaco .mapa { margin-top: 30px; }
.fecho--espaco .mapa__figura { border-width: 1.5px; }
'''


def capitulo(s, foto, corpo, invertido=False, espelhado=False, planta=False, tag="h2"):
    cls = "capitulo"
    if invertido:
        cls += " capitulo--invertido invertido"
    if espelhado:
        cls += " capitulo--espelhado"
    src, alt, cap = foto
    icls = "capitulo__imagem" + (" capitulo__imagem--planta" if planta else "")
    return ('<section class="' + cls + '">\n'
            '  <div class="capitulo__texto">' + cabeca(s, tag) + corpo + '</div>\n'
            '  <figure class="' + icls + '"><img src="../assets/' + src + '" alt="' + alt
            + '" loading="lazy"><figcaption>' + cap + '</figcaption></figure>\n'
            '</section>')


def render_c():
    p = [cabecalho("C · Espaço")]

    p.append('<section class="abertura"><img src="../assets/hero.jpg" alt="Antiga Igreja de Retorta e casa do padre, Vila do Conde">'
             '<p class="abertura__legenda">Dossier de apresentação e mecenato</p>'
             '<p class="abertura__marca">a Sineira</p></section>')

    # o espaço vem primeiro, e a toda a largura
    p.append('<section class="fecho fecho--espaco" id="espaco">' + cabeca(ESPACO, "h1")
             + '<p>' + ESPACO["texto"] + '</p>' + mapa_espaco() + '</section>')

    p.append(capitulo(INTRO, INTERVENCAO["fotos"][2], espelhado=True, invertido=True,
                      corpo='<p class="sub">' + INTRO["sub"] + '</p>'
                            + "".join('<p>' + t + '</p>' for t in INTRO["paras"])
                            + '<a class="botao" href="#mecenato"><span>Apoiar o projecto</span></a>'))

    p.append(capitulo(REQUALIFICACAO, REQUALIFICACAO["fotos"][0],
                      li(REQUALIFICACAO["itens"], "lista")))

    p.append(capitulo(FASEAMENTO, FASEAMENTO["foto"], li(FASEAMENTO["itens"], "lista"),
                      espelhado=True, planta=True))

    p.append(capitulo(ACESSOS, ACESSOS["foto"], invertido=True,
                      corpo=tabela(ACESSOS["tabela"]) + '<p>' + ACESSOS["texto"] + '</p>'))

    p.append(capitulo(MISSAO, REQUALIFICACAO["fotos"][1], li(MISSAO["itens"], "lista"), espelhado=True))

    p.append(capitulo(ACTIVIDADES, INTERVENCAO["fotos"][3], invertido=True,
                      corpo='<p class="disciplinas">' + ACTIVIDADES["disciplinas"] + '</p>'
                            + bloco_actividades()))

    p.append('<section class="capitulo"><div class="capitulo__texto">' + cabeca(IDADES)
             + '<p>' + IDADES["texto"] + '</p>' + li(IDADES["pills"], "pills")
             + '</div><div class="capitulo__texto invertido">' + cabeca(TERRITORIO)
             + bloco_territorio() + '</div></section>')

    p.append('<section class="fecho"><p class="kicker">' + INTERVENCAO["num"] + ' · '
             + INTERVENCAO["kicker"] + '</p><h2 class="titulo">' + INTERVENCAO["titulo"]
             + '</h2><p>' + INTERVENCAO["texto"] + '</p></section>')
    p.append('<div class="tira">' + "".join(
        '<figure><img src="../assets/' + f[0] + '" alt="' + f[1] + '" loading="lazy">'
        '<figcaption>' + f[2] + '</figcaption></figure>' for f in INTERVENCAO["fotos"]) + '</div>')

    p.append('<section class="fecho invertido" id="mecenato">' + cabeca(MECENATO)
             + '<p>' + MECENATO["texto"] + '</p>' + li(MECENATO["itens"], "lista")
             + bloco_niveis() + '<p class="legal">' + MECENATO["legal"] + '</p>'
             + '<a class="botao" href="' + MAILTO + '"><span>Quero apoiar</span></a></section>')

    p.append('<section class="fecho">' + cabeca(CONTACTOS)
             + li(['<a href="' + u + '">' + n + '</a>' for n, u in CONTACTOS["links"]], "lista")
             + '<p class="legal">' + CONTACTOS["legal"] + '<br>'
             + "<br>".join(CONTACTOS["moradas"]) + '</p>'
             + '<a class="botao" href="mailto:' + CONTACTOS["email"] + '"><span>Escrever-nos</span></a></section>')

    p.append('<section class="fecho invertido">' + cabeca(CONVITE)
             + '<p>' + CONVITE["texto"] + '</p>'
             + '<a class="botao" href="#mecenato"><span>Plano de mecenato</span></a></section>')

    return pagina("c", "C · Espaço", CSS_C, "\n\n".join(p))


# --------------------------------------------------------------------------
# ÍNDICE das experiências
# --------------------------------------------------------------------------

CSS_INDICE = '''
/* Três opções, três colunas no máximo — senão sobra uma coluna vazia. */
.escolha { display: grid; grid-template-columns: repeat(auto-fit, minmax(max(100% / 3, min(100%, 300px)), 1fr)); }
.escolha__intro { grid-column: 1 / -1; padding: clamp(46px, 8vh, 110px) var(--gutter) clamp(30px, 5vh, 60px); }
.escolha__intro h1 {
  font-size: clamp(32px, 5.4vw, 70px); font-weight: 700; line-height: .95;
  letter-spacing: -.03em; text-transform: uppercase; margin-top: 8px;
}
.escolha__intro p { max-width: 58ch; margin-top: 20px; }
.opcao {
  display: flex; flex-direction: column; min-height: 46vh;
  padding: clamp(26px, 3vw, 40px) var(--gutter);
  border-top: 1.5px solid color-mix(in srgb, var(--blue) 30%, transparent);
}
.opcao:hover { text-decoration: none; }
.opcao--azul { background: var(--blue); color: var(--cream); }
.opcao h2 {
  margin-top: 6px; font-size: clamp(26px, 3vw, 40px); font-weight: 700;
  line-height: .95; letter-spacing: -.03em; text-transform: uppercase;
}
.opcao p { margin-top: 14px; font-size: 15px; }
.opcao .seta { margin-top: auto; padding-top: 24px; font-size: 26px; }
.nota { grid-column: 1 / -1; padding: clamp(34px, 5vh, 70px) var(--gutter); border-top: 1.5px solid color-mix(in srgb, var(--blue) 30%, transparent); }
.nota p { max-width: 62ch; font-size: 14px; }
.nota p + p { margin-top: 12px; }
'''

OPCOES = [
    ("a", "A · Documento",
     "Uma coluna larga, secções numeradas e bandas alternadas. O mais próximo de um "
     "dossier impresso: lê-se de fio a pavio e imprime-se bem.", False),
    ("b", "B · Mosaico",
     "A grelha de cartões do site aplicada ao dossier, com as fotografias intercaladas. "
     "Lê-se por blocos, em vez de seguido.", True),
    ("c", "C · Espaço",
     "Capítulos de ecrã inteiro, com o lugar a mandar: o espaço abre o dossier e as "
     "plantas e propostas ocupam metade do ecrã.", False),
]


def render_indice():
    cartoes = []
    for slug, nome, desc, azul in OPCOES:
        cls = "opcao" + (" opcao--azul invertido" if azul else "")
        cartoes.append('<a class="' + cls + '" href="' + slug + '/">'
                       '<p class="kicker">Experiência</p><h2>' + nome + '</h2>'
                       '<p>' + desc + '</p><p class="seta">&rarr;</p></a>')
    corpo = ('<main class="escolha">\n'
             '<div class="escolha__intro"><p class="kicker">a Sineira &middot; dossier</p>'
             '<h1>Três experiências</h1>'
             '<p>O mesmo conteúdo, três desenhos. Todos usam a linguagem a que chegámos no '
             'site: creme e azul, a mesma tipografia e a mesma margem do logótipo.</p></div>\n'
             + "\n".join(cartoes) + '\n'
             '<div class="nota"><p><strong>Conteúdo:</strong> o que a associação escreveu na '
             'última revisão. O texto do nível <em>Patrocínio</em> ainda não existe e aparece '
             'marcado como por escrever, em vez de preenchido com texto inventado.</p>'
             '<p><strong>Por fazer:</strong> versão em inglês, assim que houver uma direcção '
             'escolhida.</p></div>\n'
             '</main>')
    return pagina_indice(corpo)


def pagina_indice(corpo):
    return ('<!DOCTYPE html>\n<html lang="pt">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>a Sineira — Dossier</title>\n'
            '<meta name="description" content="Dossier de apresentação e mecenato da a Sineira — três experiências de desenho.">\n'
            '<link rel="icon" href="../favicon.ico" type="image/x-icon">\n'
            '<link rel="stylesheet" href="base.css">\n'
            '<style>\n' + CSS_INDICE + '\n</style>\n</head>\n<body>\n\n'
            + MARCA.replace('class="svg-defs"', 'class="svg-defs"') + '\n\n'
            + '<header class="topo"><a class="topo__marca" href="/">'
            '<svg viewBox="0 0 382 387" aria-hidden="true"><use href="#mark-sineira"></use></svg>'
            '<span>a Sineira</span></a>'
            '<p class="topo__titulo">Dossier de apresentação</p></header>\n\n'
            + corpo + '\n\n</body>\n</html>\n')


# --------------------------------------------------------------------------

def main():
    for sub in ("a", "b", "c"):
        os.makedirs(os.path.join(DOSSIER, sub), exist_ok=True)
    escrever(os.path.join(DOSSIER, "base.css"), BASE_CSS)
    escrever(os.path.join(DOSSIER, "a", "index.html"), render_a())
    escrever(os.path.join(DOSSIER, "b", "index.html"), render_b())
    escrever(os.path.join(DOSSIER, "c", "index.html"), render_c())
    escrever(os.path.join(DOSSIER, "index.html"), render_indice())


def escrever(caminho, texto):
    with io.open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("escrito:", os.path.relpath(caminho, REPO), len(texto), "bytes")


if __name__ == "__main__":
    main()
