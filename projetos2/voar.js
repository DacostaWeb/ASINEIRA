/* =====================================================================
   Um projeto, num registo só — agora nas duas línguas.

   No primeiro estudo o registo era só português. Aqui traz o pt e o en
   dentro de cada campo, exactamente como os eventos do index.html: o
   resto do site tem o português no HTML e o inglês no dicionário, mas
   um projeto não tem onde o guardar, que é o JS quem escreve a página.

   O título não se traduz. É a decisão que o site já tomou na lista
   EVENTOS, onde o "Voar Muito Perto do Sol" se chama assim nas duas
   línguas: é o nome da peça, não uma descrição dela.

   O texto português é o do sítio da Sara Garcia, palavra por palavra.
   O inglês é tradução dele.
   ===================================================================== */

var PROJETO = {
  slug: 'voar-muito-perto-do-sol',
  ano:  2024,

  /* Igual nas duas línguas. */
  titulo: 'Voar Muito Perto do Sol',

  /* A natureza é a etiqueta do site, e usa as palavras do dicionário dele:
     Formação / Training. No sítio da Sara este projeto está arrumado em
     "teaching", e o texto descreve uma oficina com apresentação final. */
  pt: {
    natureza: 'Formação',
    onde:     'Fórum da Maia',
    contexto: 'Mês da Arquitectura da Maia',
    quando:   'Novembro de 2024',
    resumo:   'Uma oficina e uma apresentação pública sobre a liberdade dentro de casa, a partir de um texto de Adolf Loos.',
    texto: [
      '“Voar Muito Perto do Sol” é um trabalho de cruzamento disciplinar entre as artes visuais, o teatro, a dança e a música.',
      'Surge no âmbito do Mês da Arquitectura da Maia (MAM) 2024, a convite dos seus curadores, Nuno Sousa e Ana Resende, como desafio de idealizar e realizar uma oficina que inclui uma apresentação final pública em torno dos conceitos de arquitectura e liberdade, respondendo ao tema da exposição “O que é um espaço de liberdade?”.',
      'Focado no sub-tema da liberdade no espaço doméstico (a casa), e partindo de um texto de 1900 do reconhecido arquitecto Adolf Loos “The Poor Little Rich Man”, desenhou-se e construiu-se uma cenografia, que se utiliza como estrutura base para todas as ações a desenvolver pelos participantes.',
      'É uma parceria entre a coreógrafa e bailarina Sara Garcia e o arquitecto Hugo Barros (atelierdacosta), com participação do músico jazzista Xavier Nunes.'
    ],
    ficha: [
      ['Criação',      'Hugo Barros e Sara Garcia'],
      ['Participação', 'Xavier Nunes'],
      ['Apoios',       'Mês da Arquitectura da Maia 2024, Fercayo / CCR, Ventos e Tempestades — Associação Cultural'],
      ['Vídeo',        'Mário M. Fonseca']
    ],
    rotulos: {
      video:  'Vídeo',
      fotos:  'Fotografias',
      ficha:  'Ficha técnica',
      sobre:  'Sobre o projeto',
      outros: 'Outros projetos',
      de:     'de'
    }
  },

  en: {
    natureza: 'Training',
    onde:     'Fórum da Maia',
    contexto: 'Maia Architecture Month',
    quando:   'November 2024',
    resumo:   'A workshop and a public showing about freedom inside the house, departing from a text by Adolf Loos.',
    texto: [
      '“Voar Muito Perto do Sol” is a cross-disciplinary work between the visual arts, theatre, dance and music.',
      'It came out of Mês da Arquitectura da Maia (MAM) 2024, at the invitation of its curators, Nuno Sousa and Ana Resende, as a challenge to conceive and run a workshop with a final public showing around the ideas of architecture and freedom, answering the theme of the exhibition “What is a space of freedom?”.',
      'Focused on freedom within the domestic space — the house — and departing from a 1900 text by the architect Adolf Loos, “The Poor Little Rich Man”, a stage set was designed and built, and used as the base structure for everything the participants do.',
      'It is a partnership between the choreographer and dancer Sara Garcia and the architect Hugo Barros (atelierdacosta), with the participation of jazz musician Xavier Nunes.'
    ],
    ficha: [
      ['Creation',      'Hugo Barros and Sara Garcia'],
      ['Participation', 'Xavier Nunes'],
      ['Support',       'Mês da Arquitectura da Maia 2024, Fercayo / CCR, Ventos e Tempestades — Associação Cultural'],
      ['Video',         'Mário M. Fonseca']
    ],
    rotulos: {
      video:  'Video',
      fotos:  'Photographs',
      ficha:  'Credits',
      sobre:  'About the project',
      outros: 'Other projects',
      de:     'of'
    }
  },

  /* O vídeo é vertical: 240 por 426, confirmado no Vimeo. É por isso que
     nunca aparece à largura da coluna em nenhuma das três fichas. */
  video: {
    src: 'https://player.vimeo.com/video/1031886171?badge=0&autopause=0&player_id=0&app_id=58479',
    titulo: { pt: 'Voar Muito Perto do Sol — vídeo de Mário M. Fonseca',
              en: 'Voar Muito Perto do Sol — video by Mário M. Fonseca' }
  },

  /* A descrição de cada fotografia serve quem lê a página com um leitor de
     ecrã e quem fica com a ligação estragada — e por isso também traduz. */
  fotos: [
    { src: 'img/voar1.jpg',
      pt: 'Um adulto e nove crianças sentados em roda no chão do palco, à frente de uma casa de madeira com uma janela redonda.',
      en: 'An adult and nine children sitting in a circle on the stage floor, in front of a wooden house with a round window.' },
    { src: 'img/voar2.jpg',
      pt: 'Três crianças entre colunas de cartão e fios esticados, com formas recortadas de cartolina na mão.',
      en: 'Three children among cardboard columns and taut strings, holding cut-out card shapes.' },
    { src: 'img/voar3.jpg',
      pt: 'A coreógrafa, de vermelho, sentada no chão entre crianças, a recortar uma forma em cartolina.',
      en: 'The choreographer, in red, sitting on the floor among children, cutting out a card shape.' },
    { src: 'img/voar4.jpg',
      pt: 'Crianças a atravessar o palco por baixo de fios onde estão pendurados desenhos presos com molas.',
      en: 'Children crossing the stage beneath strings hung with drawings pegged in place.' },
    { src: 'img/voar5.jpg',
      pt: 'A apresentação final vista de trás da plateia: uma criança aparece na janela redonda da casa.',
      en: 'The final showing seen from behind the audience: a child appears in the round window of the house.' },
    { src: 'img/voar6.jpg',
      pt: 'Vista de cima: crianças e a coreógrafa sentadas no chão, cada uma com uma forma de cartolina na mão.',
      en: 'Seen from above: children and the choreographer sitting on the floor, each holding a card shape.' },
    { src: 'img/voar7.jpg',
      pt: 'O músico toca guitarra sentado à frente das crianças, ao lado de um espelho oval que as reflete.',
      en: 'The musician plays guitar sitting in front of the children, beside an oval mirror that reflects them.' },
    { src: 'img/voar8.jpg',
      pt: 'As crianças sentadas de costas, a olhar para a janela redonda iluminada da casa.',
      en: 'The children sitting with their backs to us, looking at the lit round window of the house.' },
    { src: 'img/voar9.jpg',
      pt: 'Crianças sentadas em cadeiras brancas a olhar para uma figura recortada que a coreógrafa levanta.',
      en: 'Children sitting on white chairs, watching a cut-out figure the choreographer holds up.' }
  ],

  /* Os vizinhos na lista de projetos. Numa página a sério saem da lista de
     todos os projetos; aqui ficam escritos para o pé ter o que mostrar, e
     com a miniatura, que é o que a lista do site lhes dá. */
  vizinhos: [
    { img: 'img/voar6.jpg', ano: 2025,
      pt: { titulo: 'Projeto X', natureza: 'Apresentação' },
      en: { titulo: 'Projeto X', natureza: 'Presentation' } },
    { img: 'img/voar3.jpg', ano: 2025,
      pt: { titulo: 'Projeto Y', natureza: 'Criação' },
      en: { titulo: 'Projeto Y', natureza: 'Creation' } }
  ]
};

/* Os atalhos que as fichas usam para não andarem a perguntar a língua. */
function T()   { return PROJETO[CASA.lang]; }
function TF(f) { return f[CASA.lang]; }
