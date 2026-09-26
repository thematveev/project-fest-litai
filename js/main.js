/**
 * Main — initialize all modules
 */
(function () {
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var targetId = link.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerHeight = document.getElementById('header').offsetHeight || 72;
        var top = target.getBoundingClientRect().top + window.scrollY - headerHeight;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  // Ticket form modal
  var ticketModal = document.getElementById('ticket-modal');
  var ticketOverlay = document.getElementById('ticket-modal-overlay');
  var ticketClose = document.getElementById('ticket-modal-close');
  var ticketForm = document.getElementById('ticket-form');
  var ticketSuccess = document.getElementById('ticket-form-success');
  var ticketSuccessClose = document.getElementById('ticket-form-success-close');

  // === REPLACE THIS with your Google Apps Script Web App URL ===
  var FORM_SUBMIT_URL = 'https://script.google.com/macros/s/AKfycbzkoz1OEQA6gLdhXXx6ktNJWbNdwLGPwmjsI8S-Pf8AuVDiV5qzLUo7864mjA8IeEJ-/exec';

  function openTicketModal() {
    ticketForm.reset();
    ticketForm.style.display = '';
    ticketSuccess.style.display = 'none';
    ticketModal.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    document.getElementById('ticket-name').focus();
  }

  function closeTicketModal() {
    ticketModal.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.ticket-open-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      openTicketModal();
    });
  });

  ticketClose.addEventListener('click', closeTicketModal);
  ticketOverlay.addEventListener('click', closeTicketModal);
  ticketSuccessClose.addEventListener('click', closeTicketModal);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && ticketModal.classList.contains('is-open')) {
      closeTicketModal();
    }
  });

  ticketForm.addEventListener('submit', function (e) {
    e.preventDefault();

    var name = document.getElementById('ticket-name').value.trim();
    var email = document.getElementById('ticket-email').value.trim();
    var phone = document.getElementById('ticket-phone').value.trim();

    if (!name || !email || !phone) {
      return;
    }

    var submitBtn = ticketForm.querySelector('.ticket-form__submit');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Надсилаємо...';

    var params = new URLSearchParams();
    params.append('name', name);
    params.append('email', email);
    params.append('phone', phone);
    params.append('ticketType', '75');

    fetch(FORM_SUBMIT_URL, {
      method: 'POST',
      body: params
    })
    .then(function () {
      ticketForm.style.display = 'none';
      ticketSuccess.style.display = '';
    })
    .catch(function () {
      alert('Сталася помилка. Спробуйте ще раз або зв\'яжіться з нами напряму.');
    })
    .finally(function () {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Надіслати заявку';
    });
  });
  // Support modal — реквізити
  var supportModal = document.getElementById('support-modal');
  var supportOverlay = document.getElementById('support-modal-overlay');
  var supportClose = document.getElementById('support-modal-close');
  var supportCopyAll = document.getElementById('support-copy-all');

  function openSupportModal() {
    supportModal.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    supportClose.focus();
  }

  function closeSupportModal() {
    supportModal.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.support-open-btn').forEach(function (btn) {
    btn.addEventListener('click', openSupportModal);
  });

  supportClose.addEventListener('click', closeSupportModal);
  supportOverlay.addEventListener('click', closeSupportModal);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && supportModal.classList.contains('is-open')) {
      closeSupportModal();
    }
  });

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }

    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.top = '-1000px';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try {
        ok = document.execCommand('copy');
      } catch (err) {
        ok = false;
      }
      document.body.removeChild(ta);
      ok ? resolve() : reject(new Error('copy failed'));
    });
  }

  function flashCopied(btn) {
    if (!btn.getAttribute('data-label')) {
      btn.setAttribute('data-label', btn.textContent.trim());
    }
    btn.textContent = 'Скопійовано';
    btn.classList.add('is-copied');
    clearTimeout(btn._copyTimer);
    btn._copyTimer = setTimeout(function () {
      btn.textContent = btn.getAttribute('data-label');
      btn.classList.remove('is-copied');
    }, 1800);
  }

  function copyFailed() {
    alert('Не вдалося скопіювати. Виділіть текст реквізитів і скопіюйте вручну.');
  }

  document.querySelectorAll('.requisite__copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      copyText(btn.getAttribute('data-copy') || '')
        .then(function () {
          flashCopied(btn);
        })
        .catch(copyFailed);
    });
  });

  supportCopyAll.addEventListener('click', function () {
    var lines = [];
    document.querySelectorAll('#support-modal .requisite').forEach(function (row) {
      var label = row.querySelector('.requisite__label');
      var value = row.querySelector('.requisite__value');
      lines.push(label.textContent.trim() + ': ' + value.textContent.trim());
    });

    copyText(lines.join('\n'))
      .then(function () {
        flashCopied(supportCopyAll);
      })
      .catch(copyFailed);
  });
})();
