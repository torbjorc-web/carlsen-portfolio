// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.nav-links a');
  const current = window.location.pathname.replace(/\/$/, '');
  navLinks.forEach(link => {
    const href = new URL(link.href).pathname.replace(/\/$/, '');
    if (href === current) link.classList.add('active');
  });

  const revealItems = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  revealItems.forEach(item => observer.observe(item));

  const backToTop = document.querySelector('[data-back-to-top]');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      backToTop.style.display = window.scrollY > 400 ? 'inline-flex' : 'none';
    });
    backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }
});
