/**
 * Hero entrance sequence — requestAnimationFrame chain
 */
(function () {
  var heroElements = document.querySelectorAll('.hero-slide-up, .hero-fade');
  if (!heroElements.length) return;

  heroElements.forEach(function (el) {
    var delay = parseInt(el.getAttribute('data-delay') || '0', 10);
    setTimeout(function () {
      el.classList.add('animate');
    }, delay);
  });
})();
