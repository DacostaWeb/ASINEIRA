/* =====================================================================
   Um projeto, num registo só.

   As três experiências leem todas daqui — é o mesmo princípio da lista
   EVENTOS do index.html: o conteúdo num sítio, e cada vista a arrumá-lo
   à sua maneira. Quando o "Voar" passar a página a sério, este objeto é
   o que o site já tem de saber sobre ele.

   O texto e a ficha técnica são os do sítio da Sara Garcia, palavra por
   palavra. As fotografias são as nove de lá, pela mesma ordem.
   ===================================================================== */

var PROJETO = {
  slug:     'voar-muito-perto-do-sol',
  titulo:   'Voar Muito Perto do Sol',
  ano:      2024,

  /* A natureza é a etiqueta do cartaz do evento — a mesma do site. No sítio
     da Sara este projeto está arrumado em "teaching", e é de facto uma
     oficina; aqui fica "Formação" e o palco fica dito na linha ao lado. */
  natureza: 'Formação',
  onde:     'Fórum da Maia · Mês da Arquitectura da Maia',
  quando:   'Novembro de 2024',

  /* Uma linha só, para a lista de projetos e para a partilha. */
  resumo:   'Uma oficina e uma apresentação pública sobre a liberdade dentro de casa, a partir de um texto de Adolf Loos.',

  video: {
    src: 'https://player.vimeo.com/video/1031886171?badge=0&autopause=0&player_id=0&app_id=58479',
    titulo: 'Voar Muito Perto do Sol — vídeo de Mário M. Fonseca'
  },

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

  /* As descrições são do que se vê em cada fotografia — servem a quem lê a
     página com um leitor de ecrã e a quem fica com a ligação estragada. */
  fotos: [
    { src: 'img/voar1.jpg', alt: 'Um adulto e nove crianças sentados em roda no chão do palco, à frente de uma casa de madeira com uma janela redonda.' },
    { src: 'img/voar2.jpg', alt: 'Três crianças entre colunas de cartão e fios esticados, com formas recortadas de cartolina na mão.' },
    { src: 'img/voar3.jpg', alt: 'A coreógrafa, de vermelho, sentada no chão entre crianças, a recortar uma forma em cartolina.' },
    { src: 'img/voar4.jpg', alt: 'Crianças a atravessar o palco por baixo de fios onde estão pendurados desenhos presos com molas.' },
    { src: 'img/voar5.jpg', alt: 'A apresentação final vista de trás da plateia: uma criança aparece na janela redonda da casa.' },
    { src: 'img/voar6.jpg', alt: 'Vista de cima: crianças e a coreógrafa sentadas no chão, cada uma com uma forma de cartolina na mão.' },
    { src: 'img/voar7.jpg', alt: 'O músico toca guitarra sentado à frente das crianças, ao lado de um espelho oval que as reflete.' },
    { src: 'img/voar8.jpg', alt: 'As crianças sentadas de costas, a olhar para a janela redonda iluminada da casa.' },
    { src: 'img/voar9.jpg', alt: 'Crianças sentadas em cadeiras brancas a olhar para uma figura recortada que a coreógrafa levanta.' }
  ],

  /* Os vizinhos na lista de projetos. Numa página a sério saem da lista; aqui
     ficam escritos para o pé da página ter o que mostrar. */
  antes:   { titulo: 'Projeto X', href: '#' },
  depois:  { titulo: 'Projeto Y', href: '#' }
};
