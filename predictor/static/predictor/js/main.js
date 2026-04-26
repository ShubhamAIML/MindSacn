// Theme
const html = document.documentElement;
const themeBtn = document.getElementById('themeBtn');
const themeIcon = document.getElementById('themeIcon');
const saved = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', saved);
setIcon(saved);
if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    setIcon(next);
  });
}
function setIcon(t) {
  if (themeIcon) themeIcon.className = t === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
}

// Sliders
document.querySelectorAll('.slider').forEach(s => {
  const v = document.getElementById(s.id + 'Val');
  const upd = () => {
    if (v) v.textContent = s.value;
    const pct = ((s.value - s.min) / (s.max - s.min)) * 100;
    s.style.background = `linear-gradient(90deg,var(--accent) ${pct}%,var(--surface2) ${pct}%)`;
  };
  s.addEventListener('input', upd);
  upd();
});

// Progress bar
const form = document.getElementById('form');
const bar = document.getElementById('progressBar');
if (form && bar) {
  const req = form.querySelectorAll('input[required],select[required]');
  const upd = () => { bar.style.width = `${([...req].filter(f => f.value.trim()).length / req.length) * 100}%`; };
  req.forEach(f => { f.addEventListener('input', upd); f.addEventListener('change', upd); });
}

// Submit loader
if (form) {
  form.addEventListener('submit', () => {
    const btn = document.getElementById('submitBtn');
    const sp = document.getElementById('spinner');
    if (btn) { btn.querySelector('span').textContent = 'Analyzing...'; btn.disabled = true; }
    if (sp) sp.classList.remove('hidden');
  });
}

// Ring animation
document.addEventListener('DOMContentLoaded', () => {
  const ring = document.querySelector('.ring-fg');
  if (ring) {
    const target = ring.style.strokeDashoffset;
    ring.style.strokeDashoffset = '314';
    setTimeout(() => { ring.style.strokeDashoffset = target; }, 100);
  }
});
