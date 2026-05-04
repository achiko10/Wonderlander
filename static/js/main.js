// Navbar scroll effect
const navbar = document.getElementById('navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  });
}

// Mobile hamburger
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
}

// Fade-in on scroll
const fadeEls = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.1 });
fadeEls.forEach(el => observer.observe(el));

// Accordion
function toggleAccordion(btn) {
  const content = btn.nextElementSibling;
  const isOpen = content.classList.contains('open');
  document.querySelectorAll('.accordion-content.open').forEach(c => c.classList.remove('open'));
  document.querySelectorAll('.accordion-btn.open').forEach(b => b.classList.remove('open'));
  if (!isOpen) { content.classList.add('open'); btn.classList.add('open'); }
}

// Auto-hide toasts
document.querySelectorAll('.toast').forEach(t => {
  setTimeout(() => { t.style.opacity = '0'; setTimeout(() => t.remove(), 300); }, 4000);
});
