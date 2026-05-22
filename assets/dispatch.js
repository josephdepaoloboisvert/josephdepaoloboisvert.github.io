function toRoman(n) {
  const vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
  const syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];
  let r = '';
  for (let i = 0; i < vals.length; i++) {
    while (n >= vals[i]) { r += syms[i]; n -= vals[i]; }
  }
  return r;
}

function currentAge() {
  const now = new Date();
  let age = now.getFullYear() - 1997;
  if (now.getMonth() < 8 || (now.getMonth() === 8 && now.getDate() < 10)) age--;
  return age;
}

document.addEventListener('DOMContentLoaded', function () {
  const vol = toRoman(new Date().getFullYear());
  const no  = toRoman(currentAge());
  document.querySelectorAll('[data-vol]').forEach(function (el) {
    el.textContent = 'VOL. ' + vol + ' · NO. ' + no;
  });
});
