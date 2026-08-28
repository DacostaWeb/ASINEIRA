/* =====================================================================
   As peças da ficha.

   Cada uma escreve um pedaço da página a partir do registo do projeto e
   da língua em que ele está. As três experiências chamam as mesmas
   peças — o que muda entre elas é onde as põem, e é isso que se está a
   comparar.

   Tudo se repinta quando a língua muda: as fichas não guardam texto
   nenhum no HTML, e por isso trocar de PT para EN é voltar a escrever
   as peças, não andar a substituir palavras dentro delas.
   ===================================================================== */

function el(tag, cls, txt) {
  var n = document.createElement(tag);
  if (cls) { n.className = cls; }
  if (txt != null) { n.textContent = txt; }
  return n;
}

/* Os dois desenhos que a identificação usa. São do feitio dos do site:
   16 de caixa, traço de 1,3, sem preenchimento. */
var ICONES = {
  sitio:  '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 14.2s4.6-4.4 4.6-7.5a4.6 4.6 0 0 0-9.2 0C3.4 9.8 8 14.2 8 14.2z"/><circle cx="8" cy="6.6" r="1.8"/></svg>',
  quando: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="2.4" y="3.6" width="11.2" height="10" rx="1.4"/><path d="M2.4 6.6h11.2M5.6 2.2v2.8M10.4 2.2v2.8"/></svg>'
};

/* Uma secção da coluna do material: o rótulo em versaletes, o filete por
   baixo dele, e o conteúdo. */
function sec(rotulo, id) {
  var s = el('section', 'sec');
  if (id) { s.id = id; }
  var h = el('div', 'sec__h');
  h.appendChild(el('h2', 'lbl', rotulo));
  s.appendChild(h);
  var corpo = el('div');
  s.appendChild(corpo);
  s.corpo = corpo;
  return s;
}


/* ---------- a identificação ---------- */

/* O 'comFicha' diz se a ficha técnica fica aqui, com o resto da
   identificação, ou se desce para a coluna do material. Só a experiência
   do índice a manda para baixo, e por uma razão: com a ficha técnica aqui
   a coluna fica mais alta do que a janela, e o índice — que é o que ela
   veio ganhar — deixa de se ver. */
function montaId(caixa, comFicha) {
  if (comFicha === undefined) { comFicha = true; }
  var t = T();
  caixa.textContent = '';

  var kick = el('div', 'ficha__kick');
  kick.appendChild(el('span', 'evtag', t.natureza));
  kick.appendChild(el('span', 'ficha__ano', String(PROJETO.ano)));
  caixa.appendChild(kick);

  caixa.appendChild(el('h1', 'ficha__h1', PROJETO.titulo));
  caixa.appendChild(el('p', 'ficha__resumo', t.resumo));

  var dets = el('div', 'ficha__dets');
  [['sitio', t.onde + ' · ' + t.contexto], ['quando', t.quando]].forEach(function (par) {
    var d = el('p', 'det');
    d.innerHTML = ICONES[par[0]];
    d.appendChild(el('span', null, par[1]));
    dets.appendChild(d);
  });
  caixa.appendChild(dets);

  /* A ficha técnica vive aqui e não no fim da página: é identificação, e
     numa ficha a identificação fica toda no mesmo sítio. */
  if (comFicha) {
    caixa.appendChild(el('p', 'lbl', t.rotulos.ficha));
    caixa.appendChild(tabelaFicha());
  }
}

/* A tabela dos créditos, sozinha, para quem a quiser noutro sítio. */
function tabelaFicha(largo) {
  var tab = el('table', largo ? 'fichat fichat--largo' : 'fichat');
  var corpo = el('tbody');
  T().ficha.forEach(function (par) {
    var tr = el('tr');
    tr.appendChild(el('th', null, par[0]));
    tr.appendChild(el('td', null, par[1]));
    corpo.appendChild(tr);
  });
  tab.appendChild(corpo);
  return tab;
}

/* A ficha técnica como secção da coluna do material — na coluna larga já
   cabem as duas colunas da tabela, e volta a ser a tabela do site. */
function montaFichaSec(caixa) {
  var s = sec(T().rotulos.ficha, 'ficha');
  s.corpo.appendChild(tabelaFicha(true));
  caixa.appendChild(s);
}


/* ---------- o texto ---------- */

function montaTexto(caixa) {
  var s = sec(T().rotulos.sobre, 'sobre');
  s.corpo.className = 'texto';
  T().texto.forEach(function (p) { s.corpo.appendChild(el('p', null, p)); });
  caixa.appendChild(s);
}


/* ---------- o vídeo ---------- */

function montaVideo(caixa) {
  var s = sec(T().rotulos.video, 'video');
  var d = el('div', 'video');
  var f = document.createElement('iframe');
  f.src = PROJETO.video.src;
  f.title = TF(PROJETO.video.titulo);
  f.allow = 'autoplay; fullscreen; picture-in-picture';
  f.allowFullscreen = true;
  d.appendChild(f);
  s.corpo.appendChild(d);
  caixa.appendChild(s);
}


/* ---------- as fotografias ---------- */

/* A grande em cima e a folha de contacto por baixo. Carregar numa pequena
   troca a grande; carregar na grande avança para a seguinte. */
function montaFotos(caixa) {
  var fotos = PROJETO.fotos;
  var n = 0;

  var s = sec(T().rotulos.fotos, 'fotos');
  var caixaFs = el('div', 'fs');

  var palco = el('div', 'fs__palco');
  var imgs = fotos.map(function (f, i) {
    var img = el('img');
    img.src = f.src;
    img.alt = TF(f);
    if (i > 0) { img.loading = 'lazy'; }
    palco.appendChild(img);
    return img;
  });
  caixaFs.appendChild(palco);

  var pe = el('div', 'fs__pe');
  var conta = el('p', 'fs__conta');
  var desc = el('p', 'fs__desc');
  pe.appendChild(conta);
  pe.appendChild(desc);
  caixaFs.appendChild(pe);

  var folha = el('div', 'fs__folha');
  var botoes = fotos.map(function (f, i) {
    var b = el('button');
    b.type = 'button';
    b.setAttribute('aria-label', (i + 1) + ' ' + T().rotulos.de + ' ' + fotos.length);
    var img = el('img');
    img.src = f.src;
    img.alt = '';
    img.loading = 'lazy';
    b.appendChild(img);
    b.addEventListener('click', function () { vai(i); });
    folha.appendChild(b);
    return b;
  });
  caixaFs.appendChild(folha);

  palco.addEventListener('click', function () { vai(n + 1); });

  function vai(i) {
    n = (i + fotos.length) % fotos.length;   /* dá a volta nas duas pontas */
    imgs.forEach(function (img, k) { img.classList.toggle('is-on', k === n); });
    botoes.forEach(function (b, k) { b.setAttribute('aria-current', String(k === n)); });
    conta.textContent = (n + 1) + ' / ' + fotos.length;
    /* A descrição no pé é a mesma que a fotografia já tem em alt: quem a
       ouve não a ouve duas vezes, porque o palco não é lido como imagem. */
    desc.textContent = TF(fotos[n]);
  }

  vai(0);

  s.corpo.appendChild(caixaFs);
  caixa.appendChild(s);
}


/* ---------- outros projetos ---------- */

function montaOutros(caixa) {
  var s = sec(T().rotulos.outros, 'outros');
  var ul = el('ul', 'prj');

  PROJETO.vizinhos.forEach(function (v) {
    var t = TF(v);
    var li = el('li', 'prj__l');
    var a = el('a', 'prj__a');
    a.href = '#';

    var mini = el('div', 'prj__mini');
    var img = el('img');
    img.src = v.img; img.alt = ''; img.loading = 'lazy';
    mini.appendChild(img);
    a.appendChild(mini);

    a.appendChild(el('p', 'prj__t', t.titulo));
    a.appendChild(el('p', 'prj__q', String(v.ano)));
    a.appendChild(el('span', 'evtag', t.natureza));
    a.appendChild(el('span', 'prj__seta', '→'));

    li.appendChild(a);
    ul.appendChild(li);
  });

  s.corpo.appendChild(ul);
  caixa.appendChild(s);
}
