/* =====================================================================
   a Sineira — a casa, em JS
   Escreve o cabeçalho e a faixa do rodapé, e trata do PT—EN. As três
   fichas chamam montaCasa() e ficam com a mesma casa, sem a copiarem
   três vezes.

   O logótipo e o triângulo são os do index.html, tal e qual — o mesmo
   desenho, as mesmas classes, o mesmo salto das letras ao passar o rato.

   Nota: aqui a casa entra por JS para as três fichas não a repetirem. No
   site a sério ela está no HTML, e é onde deve estar: uma página que não
   mostra o logótipo enquanto o JS não corre não é uma página do site.
   ===================================================================== */

var CASA = {};

/* A língua guarda-se na mesma chave do site, para quem vem de lá a
   encontrar como a deixou. */
CASA.lang = 'pt';
try { CASA.lang = localStorage.getItem('sineira-lang') === 'en' ? 'en' : 'pt'; } catch (e) {}

CASA.ouvintes = [];
CASA.aoMudar = function (fn) { CASA.ouvintes.push(fn); fn(CASA.lang); };

CASA.setLang = function (l) {
  CASA.lang = l === 'en' ? 'en' : 'pt';
  document.documentElement.lang = CASA.lang;
  CASA.ouvintes.forEach(function (fn) { fn(CASA.lang); });
  try { localStorage.setItem('sineira-lang', CASA.lang); } catch (e) {}
};

/* A frase da faixa é a do site, nas duas línguas. */
CASA.MARQUEE = {
  pt: 'Adere já e torna-te um "Amigo da Sineira" para espetáculos gratuitos, descontos e conteúdo exclusivo!',
  en: 'Join now and become a "Friend of a Sineira" for discounts and monthly surprises!'
};

CASA.WORDMARK =
    '<svg class="wordmark__svg" viewBox="48 42 194 58" role="img" aria-label="a Sineira" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">' +
    '      <g class="wm__letter wm__a" id="wm-a" transform="translate(61.805172,73.153994) rotate(0)"><path d="M69.823985,81.501434c-.890183,2.191852-2.012935,5.465021-2.104465,6.074494l-6.089234-2.473037c.006775-.527952.366541-1.795292.59178-2.381029-1.359507.954594-3.531095,1.809153-7.602648.155563-5.550884-2.254396-6.410494-6.854411-4.960295-10.425162c2.130009-5.244613,7.324404-5.953472,14.074134-3.212186l3.285291,1.334264.571407-1.406947c.664744-1.636765.729446-3.485605-2.226502-4.686112-2.690844-1.092839-3.744337-.188405-4.714542,1.359611l-6.061185-2.461646c2.007121-3.950634,5.881465-6.233827,12.864932-3.351763c6.150156,2.54363,8.527829,6.315106,6.30228,11.794964l-3.930953,9.678986ZM65.45233,74.446331l-2.596746-1.054624c-3.840831-1.559887-5.741204-.965669-6.642595,1.253779-.67687,1.666623-.224395,3.485186,2.066532,4.415607c4.050743,1.645139,5.691927-.96846,6.927159-4.00991l.24565-.604852Z" transform="translate(-61.805172,-73.153994)"></path></g>' +
    '      <g class="wm__letter wm__s" transform="translate(102.681297,70.45)"><path d="M96.421534,77.298584c.754883,3.323731,3.138672,4.780762,6.969727,4.780762c3.819336,0,5.453125-1.508789,5.453125-3.931641c0-2.693359-1.594727-3.862305-7.254883-5.179687-9.006836-2.114258-11.233398-5.390137-11.233398-9.858399c0-5.768554,4.314453-9.685547,12.149414-9.685547c8.787109,0,12.288086,4.723633,12.761719,9.564453h-7.209961c-.345703-2.036621-1.47168-4.248535-5.738281-4.248535-2.904297,0-4.657227,1.199707-4.657227,3.549317c0,2.301757,1.405273,3.234863,6.75293,4.475097c9.625976,2.268067,11.736328,5.849121,11.736328,10.515137c0,6.042969-4.572266,10.188965-13.321289,10.188965-8.400391,0-12.825196-4.135742-13.618165-10.169922h7.209961Z" transform="translate(-102.681297,-70.446289)"></path></g>' +
    '      <g class="wm__letter wm__i1-dot" transform="translate(122.109634,64.644287)"><rect width="6.87987" height="6.13574" transform="translate(-3.439634,-3.067887)"></rect></g>' +
    '      <g class="wm__letter wm__i1-stem" transform="translate(122.109634,79.004761)"><rect width="6.87987" height="15.99" transform="translate(-3.439634,-7.994961)"></rect></g>' +
    '      <g class="wm__letter wm__n" transform="translate(140.437744,74.288086)"><path d="M129.301519,68.412354c0-2.112305,0-5.000489-.048828-6.835938h6.663086c.138671.641113.228515,2.942871.264648,3.741699.844727-1.560547,2.855469-3.741699,7.208008-3.741699c4.991211,0,8.234375,3.37207,8.234375,9.616211v15.807129h-6.879883v-15.042481c0-2.793457-.930664-4.816894-3.966797-4.816894-2.922852,0-4.595703,1.625-4.595703,6.012695v13.84668h-6.878906v-18.587402Z" transform="translate(-140.437744,-74.288086)"></path></g>' +
    '      <g class="wm__letter wm__e" transform="translate(165.976837,74.576172) rotate(0)"><path d="M161.196567,76.047607c.005859,3.107422,1.5625,6.14502,4.987305,6.14502c2.864258,0,3.682617-1.149902,4.334961-2.65332h6.885742c-.881836,3.041504-3.594727,8.036621-11.401367,8.036621-8.183594,0-11.734375-6.119629-11.734375-12.638672c0-7.794434,4-13.36084,11.980468-13.36084c8.53418,0,11.435547,6.17334,11.435547,12.375977c0,.841308,0,1.38623-.09082,2.095214h-16.397461Zm9.59668-4.225585c-.047852-2.892579-1.203125-5.327149-4.555664-5.327149-3.295899,0-4.622071,2.272949-4.896485,5.327149h9.452149Z" transform="translate(-165.976837,-74.576172)"></path></g>' +
    '      <g class="wm__letter wm__i2-dot" transform="translate(183.770813,56.491943)"><rect width="6.87988" height="6.13574" transform="translate(-3.439813,-3.067843)"></rect></g>' +
    '      <g class="wm__letter wm__i2-stem" transform="translate(183.77094,86.9997) scale(1,1)"><rect width="6.87988" height="24.1423" transform="translate(-3.43994,-24.1423)"></rect></g>' +
    '      <g class="wm__letter wm__r" transform="translate(198.365051,74.640503) rotate(0)"><path d="M190.962709,69.597168c0-2.46875-.005859-4.661621-.047852-6.739746h6.747071c.09082.556641.180664,3.022461.180664,4.362305c1.09668-2.839844,3.746094-4.915528,7.972656-4.938477v6.564453c-4.992188-.128418-7.972656.51001-7.972656,7.321045v10.833008h-6.879883v-17.402588Z" transform="translate(-198.365051,-74.640503)"></path></g>' +
    '      <g class="wm__letter wm__a2" transform="translate(217.027161,74.288059)"><path d="M227.903139,80.291936c0,2.365722.191406,5.8208.335937,6.419921h-6.572265c-.192383-.491699-.335938-1.801269-.347657-2.42871-.90039,1.395996-2.589843,3.004882-6.985351,3.004882-5.991211,0-8.518555-3.938476-8.518555-7.79248c0-5.660645,4.545899-8.271973,11.831055-8.271973h3.545898v-1.907658c0-1.766602-.635742-3.114803-3.826172-3.114803-2.904297,0-3.540039.845272-3.856445,2.644588h-6.541992c.373047-4.415527,3.103515-7.599666,10.658203-7.557185c6.655273.04248,10.277344,2.252986,10.277344,8.167537v10.835881Zm-6.705094-4.891602h-2.802719c-4.145508,0-5.682617,1.265625-5.682617,3.661133c0,1.798828,1.103516,3.313476,3.576172,3.313476c4.37207,0,4.909164-3.039062,4.909164-6.321777v-.652832Z" transform="translate(-217.027161,-74.288059)"></path></g>' +
    '    </svg>';

CASA.TRIANGULO =
    '<svg class="menu-trigger__svg" viewBox="0 0 382 387" xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision">' +
    '      <defs>' +
    '        <clipPath id="triClip" clipPathUnits="userSpaceOnUse">' +
    '          <path d="M95.7804 387L382 110.293L0 0L95.7804 387Z"></path>' +
    '        </clipPath>' +
    '      </defs>' +
    '      <g id="triRot">' +
    '        <path class="menu-trigger__shape" d="M95.7804 387L382 110.293L0 0L95.7804 387Z"></path>' +
    '      </g>' +
    '      <g class="menu-trigger__letters" id="triLetters" clip-path="url(#triClip)">' +
    '        <path d="M237.388 200.34C247.689 213.363 261.205 214.741 278 206.656C294.744 198.596 298.733 188.514 293.636 177.859C287.97 166.014 278.519 164.239 250.934 170.39C207 180.098 190.348 170.391 180.948 150.741C168.813 125.373 179.487 99.0424 213.836 82.5088C252.358 63.9658 277.644 77.3509 289.904 97.6398L258.295 112.855C252.495 104.628 242.906 97.2765 224.201 106.28C211.468 112.409 206.307 121.384 211.25 131.717C216.092 141.839 224.216 142.977 250.269 137.146C297.241 126.807 314.026 138.102 323.842 158.622C336.554 185.197 325.231 213.078 286.876 231.541C250.048 249.268 221.95 240.417 205.779 215.554L237.388 200.34Z"></path>' +
    '        <path d="M127.809 268.327C123.481 279.019 118.021 294.985 117.576 297.957L87.9668 285.895C87.9997 283.319 89.7491 277.138 90.8443 274.28C84.2336 278.937 73.674 283.105 53.8757 275.039C26.8839 264.043 22.704 241.605 29.7557 224.188C40.1131 198.606 65.3714 195.148 98.1927 208.519L114.168 215.028L116.946 208.165C120.179 200.181 120.493 191.163 106.12 185.307C93.0352 179.976 87.9124 184.388 83.1947 191.939L53.7216 179.932C63.4814 160.661 82.3208 149.524 116.279 163.582C146.184 175.99 157.746 194.386 146.924 221.116L127.809 268.327ZM106.552 233.914L93.9249 228.77C75.2484 221.161 66.0077 224.06 61.6246 234.886C58.3332 243.015 60.5334 251.886 71.6733 256.424C91.3705 264.449 99.3509 251.7 105.357 236.865L106.552 233.914Z"></path>' +
    '      </g>' +
    '    </svg>';

/* Escreve a casa à volta do que a página já tem. O 'volta' é para onde
   levam o logótipo e o triângulo. */
function montaCasa(volta) {
  volta = volta || '../index.html';

  var topo = document.createElement('div');
  topo.innerHTML =
    '<a class="wordmark" href="' + volta + '" aria-label="a Sineira">' + CASA.WORDMARK + '</a>' +
    '<div class="lang" role="group" aria-label="PT — EN">' +
      '<button class="lang__btn" id="lang-pt" type="button" aria-pressed="true">PT</button>' +
      '<span class="lang__sep" aria-hidden="true">—</span>' +
      '<button class="lang__btn" id="lang-en" type="button" aria-pressed="false">EN</button>' +
    '</div>' +
    '<header class="site-header">' +
      '<a class="menu-trigger" href="' + volta + '" aria-label="menu">' + CASA.TRIANGULO + '</a>' +
    '</header>';
  while (topo.firstChild) { document.body.insertBefore(topo.firstChild, document.body.firstChild); }

  /* A frase repetida seis vezes: o translate de -50% cai sempre numa cópia
     igual, e por isso o ciclo não tem emenda visível. */
  var faixa = document.createElement('div');
  faixa.className = 'marquee';
  var pista = document.createElement('div');
  pista.className = 'marquee__track';
  var i;
  for (i = 0; i < 6; i++) {
    var s = document.createElement('span');
    s.className = 'marquee__text';
    pista.appendChild(s);
  }
  faixa.appendChild(pista);
  document.body.appendChild(faixa);

  document.getElementById('lang-pt').addEventListener('click', function () { CASA.setLang('pt'); });
  document.getElementById('lang-en').addEventListener('click', function () { CASA.setLang('en'); });

  CASA.aoMudar(function (lang) {
    document.documentElement.lang = lang;
    Array.prototype.forEach.call(pista.children, function (sp) {
      sp.textContent = CASA.MARQUEE[lang];
    });
    document.getElementById('lang-pt').setAttribute('aria-pressed', String(lang === 'pt'));
    document.getElementById('lang-en').setAttribute('aria-pressed', String(lang === 'en'));
  });
}
