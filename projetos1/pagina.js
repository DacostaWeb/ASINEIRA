/* =====================================================================
   As peças que as três experiências partilham: o título, o vídeo, a
   ficha técnica e as fotografias. Cada página chama as que quer e
   arruma-as à sua maneira — o que muda entre experiências é a ordem e o
   sítio, não as peças.
   ===================================================================== */

function el(tag, cls, txt) {
  var n = document.createElement(tag);
  if (cls) { n.className = cls; }
  if (txt != null) { n.textContent = txt; }
  return n;
}

/* O título e a linha que o acompanha: a natureza, quando e onde. */
function montaTitulo(caixa, p) {
  var h = el('h1', 'h1');
  h.appendChild(document.createTextNode(p.titulo + ' '));
  h.appendChild(el('small', null, '(' + p.ano + ')'));
  caixa.appendChild(h);

  var meta = el('div', 'meta');
  meta.appendChild(el('span', 'tag', p.natureza));
  meta.appendChild(el('p', null, p.quando + ' · ' + p.onde));
  caixa.appendChild(meta);
}

function montaVideo(caixa, p) {
  var d = el('div', 'video');
  var f = document.createElement('iframe');
  f.src = p.video.src;
  f.title = p.video.titulo;
  f.allow = 'autoplay; fullscreen; picture-in-picture';
  f.allowFullscreen = true;
  d.appendChild(f);
  caixa.appendChild(d);
}

function montaTexto(caixa, p) {
  p.texto.forEach(function (t) { caixa.appendChild(el('p', null, t)); });
}

function montaFicha(caixa, p) {
  var t = el('table', 'fichas');
  var corpo = el('tbody');
  p.ficha.forEach(function (par) {
    var tr = el('tr');
    tr.appendChild(el('th', null, par[0]));
    tr.appendChild(el('td', null, par[1]));
    corpo.appendChild(tr);
  });
  t.appendChild(corpo);
  caixa.appendChild(t);
}

/* As fotografias uma de cada vez, como no sítio da Sara — mas com as setas,
   os pontos e o número à vista, e o clique na própria fotografia a avançar,
   que é o que toda a gente tenta primeiro.

   Cabem nove fotografias de formatos diferentes (a primeira está ao alto e
   as outras deitadas): o palco tem uma medida fixa e a fotografia entra
   inteira lá dentro, sem cortes — por isso a que está ao alto fica mais
   pequena em vez de ficar sem cabeças. */
function montaFotos(caixa, fotos) {
  var n = 0;

  var palco = el('div', 'fotos__palco');
  palco.setAttribute('role', 'group');
  palco.setAttribute('aria-label', 'Fotografias, ' + fotos.length + ' no total');

  var imgs = fotos.map(function (f, i) {
    var img = el('img');
    img.src = f.src;
    img.alt = f.alt;
    if (i > 0) { img.loading = 'lazy'; }
    if (i === 0) { img.className = 'is-on'; }
    palco.appendChild(img);
    return img;
  });
  caixa.appendChild(palco);

  var pe = el('div', 'fotos__pe');
  var conta = el('p', 'fotos__conta');
  pe.appendChild(conta);

  var pontos = el('div', 'fotos__pontos');
  var bolas = fotos.map(function (f, i) {
    var b = el('button');
    b.type = 'button';
    b.setAttribute('aria-label', 'Fotografia ' + (i + 1));
    b.addEventListener('click', function () { vai(i); });
    pontos.appendChild(b);
    return b;
  });
  pe.appendChild(pontos);

  var setas = el('div', 'fotos__setas');
  var atras = el('button', null, '←');
  var frente = el('button', null, '→');
  atras.type = frente.type = 'button';
  atras.setAttribute('aria-label', 'Fotografia anterior');
  frente.setAttribute('aria-label', 'Fotografia seguinte');
  atras.addEventListener('click', function () { vai(n - 1); });
  frente.addEventListener('click', function () { vai(n + 1); });
  setas.appendChild(atras);
  setas.appendChild(frente);
  pe.appendChild(setas);

  caixa.appendChild(pe);

  palco.addEventListener('click', function () { vai(n + 1); });

  function vai(i) {
    n = (i + fotos.length) % fotos.length;   /* dá a volta nas duas pontas */
    imgs.forEach(function (img, k) { img.classList.toggle('is-on', k === n); });
    bolas.forEach(function (b, k) { b.setAttribute('aria-current', String(k === n)); });
    conta.textContent = (n + 1) + ' / ' + fotos.length;
  }

  vai(0);
}

/* O pé: o projeto de antes e o de depois, como no sítio da Sara. */
function montaPe(caixa, p) {
  var a = el('a', null, '← ' + p.antes.titulo);
  a.href = p.antes.href;
  var b = el('a', null, p.depois.titulo + ' →');
  b.href = p.depois.href;
  caixa.appendChild(a);
  caixa.appendChild(b);
}
