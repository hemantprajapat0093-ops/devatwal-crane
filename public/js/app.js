// Devatwal Crane Service - Core Logic & Direct Communication

document.addEventListener('DOMContentLoaded', () => {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  if (typeof init3DCrane === 'function') {
    init3DCrane();
  }

  setupContactTriggers();
  setupBookingForm();
  setupGalleryLightbox();
  setupCraneSelectionSync();
  setupMobileMenu();
  setupEmailDispatcherModal();
});

const OWNER_CONFIG = {
  phone1: '9414333328',
  phone2: '9950233073',
  email: 'satyapaldevatwal@gmail.com',
  location: 'RIICO Industrial Area, Ghiloth, Neemrana, Alwar, Rajasthan - 301705',
};

const INQUIRY_TEMPLATE = {
  subject: 'Inquiry for Crane Service - Devatwal Crane Service (301705)',
  body: `Dear Satyapal Prajapat ji (Devatwal Crane Service),

I am writing to inquire about crane hiring and heavy lifting services for our project.

PROJECT REQUIREMENTS:
- Project Location: [e.g. RIICO Industrial Area Ghiloth / Neemrana (Pincode: 301705)]
- Nature of Work: [e.g. Building Construction / Heavy Machinery Shift / Precast Slab / Erection]
- Preferred Crane Variety: [ACE 12XW Window AC / ACE 14XW High-Reach / Indus Heavy Titan]
- Estimated Load Tonnage: [e.g. 5 to 15+ Tons]
- Required Date & Shift: [Immediate / Scheduled Date]
- Client Name & Company: 
- Contact Mobile Number: 

Kindly provide rate quotation and crane availability.

Best regards,
[Your Name / Organization]`,
};

// 1. DIRECT CONTACT TRIGGERS (CALL, DIRECT EMAIL DISPATCH, WHATSAPP)
function setupContactTriggers() {
  // Direct Phone Call
  document.querySelectorAll('.btn-call-primary').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.location.href = `tel:${OWNER_CONFIG.phone1}`;
    });
  });

  document.querySelectorAll('.btn-call-secondary').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.location.href = `tel:${OWNER_CONFIG.phone2}`;
    });
  });

  // Direct Email Launcher - Triggers Email Dispatcher Modal & Direct Options
  document.querySelectorAll('.btn-send-email').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openEmailDispatcherModal(true);
    });
  });

  // Direct WhatsApp
  document.querySelectorAll('.btn-open-whatsapp').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      triggerWhatsAppInquiry();
    });
  });
}

// 2. SMART EMAIL DISPATCHER MODAL & MULTI-PROVIDER SUPPORT
function setupEmailDispatcherModal() {
  const modal = document.getElementById('email-dispatcher-modal');
  const closeBtn = document.getElementById('close-email-modal');
  const copyBtn = document.getElementById('btn-copy-email-text');
  const quickForm = document.getElementById('quick-inmodal-email-form');

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => {
      modal.classList.remove('modal-active');
      document.body.style.overflow = '';
    });
  }

  // Close when clicking outside content
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('modal-active');
        document.body.style.overflow = '';
      }
    });
  }

  // Copy full inquiry text & email address
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const fullText = `TO: ${OWNER_CONFIG.email}\nSUBJECT: ${INQUIRY_TEMPLATE.subject}\n\n${INQUIRY_TEMPLATE.body}`;
      navigator.clipboard.writeText(fullText).then(() => {
        showToast('✓ Email address & inquiry copied to clipboard!');
        copyBtn.innerHTML = `<span class="text-emerald-400 font-bold">✓ Copied Successfully!</span>`;
        setTimeout(() => {
          copyBtn.innerHTML = `<i data-lucide="copy" class="w-4 h-4 text-sky-400"></i><span>Copy Inquiry Message & Email Address to Clipboard</span>`;
          if (typeof lucide !== 'undefined') lucide.createIcons();
        }, 3000);
      }).catch(() => {
        showToast(`Email: ${OWNER_CONFIG.email}`);
      });
    });
  }

  // Quick In-Modal Message Send
  if (quickForm) {
    quickForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const sendBtn = document.getElementById('btn-send-modal-msg');
      const origText = sendBtn ? sendBtn.innerHTML : 'Send Message';
      if (sendBtn) {
        sendBtn.disabled = true;
        sendBtn.textContent = 'Transmitting Message...';
      }

      const payload = {
        name: document.getElementById('modal-name')?.value.trim() || 'Website Visitor',
        phone: document.getElementById('modal-phone')?.value.trim() || 'N/A',
        message: document.getElementById('modal-message')?.value.trim() || 'General Inquiry',
        subject: 'Quick Inquiry from Devatwal Crane Service Website',
      };

      try {
        const res = await fetch('/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        const json = await res.json();
        if (json.success) {
          showToast('✓ Message sent successfully to Satyapal ji!');
          quickForm.reset();
          setTimeout(() => {
            modal.classList.remove('modal-active');
            document.body.style.overflow = '';
          }, 1500);
        } else {
          showToast(json.message || 'Error sending message');
        }
      } catch (err) {
        showToast('Message recorded! Call +91 9414333328');
      } finally {
        if (sendBtn) {
          sendBtn.disabled = false;
          sendBtn.innerHTML = origText;
        }
      }
    });
  }
}

function openEmailDispatcherModal(autoLaunchGmail = false) {
  const modal = document.getElementById('email-dispatcher-modal');
  if (!modal) return;

  const encSubject = encodeURIComponent(INQUIRY_TEMPLATE.subject);
  const encBody = encodeURIComponent(INQUIRY_TEMPLATE.body);

  // 1. Gmail Web URL
  const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=${OWNER_CONFIG.email}&su=${encSubject}&body=${encBody}`;
  const gmailBtn = document.getElementById('btn-launch-gmail');
  if (gmailBtn) gmailBtn.href = gmailUrl;

  // 2. Default System Mailto URL
  const mailtoUrl = `mailto:${OWNER_CONFIG.email}?subject=${encSubject}&body=${encBody}`;
  const mailtoBtn = document.getElementById('btn-launch-mailto');
  if (mailtoBtn) mailtoBtn.href = mailtoUrl;

  // 3. Outlook.com Web URL
  const outlookUrl = `https://outlook.live.com/mail/0/deeplink/compose?to=${OWNER_CONFIG.email}&subject=${encSubject}&body=${encBody}`;
  const outlookBtn = document.getElementById('btn-launch-outlook');
  if (outlookBtn) outlookBtn.href = outlookUrl;

  // 4. Yahoo Mail Web URL
  const yahooUrl = `https://compose.mail.yahoo.com/?to=${OWNER_CONFIG.email}&subj=${encSubject}&body=${encBody}`;
  const yahooBtn = document.getElementById('btn-launch-yahoo');
  if (yahooBtn) yahooBtn.href = yahooUrl;

  // Show Modal
  modal.classList.add('modal-active');
  document.body.style.overflow = 'hidden';

  // If user requested direct action, also open Gmail in a new tab immediately
  if (autoLaunchGmail) {
    try {
      window.open(gmailUrl, '_blank');
    } catch (e) {
      console.log('Popup blocked, modal is active for user choice.');
    }
  }

  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
}

function showToast(message) {
  const existing = document.querySelector('.toast-notice');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'toast-notice';
  toast.innerHTML = `<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i><span>${message}</span>`;
  document.body.appendChild(toast);
  if (typeof lucide !== 'undefined') lucide.createIcons();

  setTimeout(() => {
    toast.style.transition = 'opacity 0.3s ease';
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function triggerWhatsAppInquiry() {
  const text = encodeURIComponent(
    `Hello Satyapal ji, I need a crane for lifting work in RIICO Ghiloth / Neemrana (Pincode: 301705). Please provide availability and rates.`
  );
  window.open(`https://wa.me/91${OWNER_CONFIG.phone1}?text=${text}`, '_blank');
}

// 3. BOOKING FORM LOGIC
function setupBookingForm() {
  const form = document.getElementById('crane-booking-form');
  if (!form) return;

  const craneCards = document.querySelectorAll('.crane-option-card');
  const hiddenCraneInput = document.getElementById('selected-crane-type');

  craneCards.forEach((card) => {
    card.addEventListener('click', () => {
      craneCards.forEach((c) => c.classList.remove('selected'));
      card.classList.add('selected');
      const val = card.getAttribute('data-crane-val');
      if (hiddenCraneInput) hiddenCraneInput.value = val;

      const preset = card.getAttribute('data-preset');
      if (window.setCranePreset && preset) {
        window.setCranePreset(preset);
      }
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('btn-submit-booking');
    const originalText = submitBtn ? submitBtn.innerHTML : 'Confirm Booking';

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<span class="inline-block animate-spin mr-2">⚙️</span> Transmitting Booking Request...`;
    }

    const formData = {
      name: document.getElementById('bk-name').value.trim(),
      phone: document.getElementById('bk-phone').value.trim(),
      email: document.getElementById('bk-email')?.value.trim() || '',
      craneType: hiddenCraneInput?.value || 'ACE 12XW Hydra (Window AC Cabin)',
      workType: document.getElementById('bk-work-type').value,
      date: document.getElementById('bk-date').value,
      timeSlot: document.getElementById('bk-time-slot').value,
      location: document.getElementById('bk-location').value.trim(),
      pincode: document.getElementById('bk-pincode')?.value.trim() || '301705',
      loadWeight: document.getElementById('bk-load-weight').value,
      notes: document.getElementById('bk-notes')?.value.trim() || '',
    };

    try {
      const response = await fetch('/api/bookings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (result.success) {
        showBookingSuccessModal(result);
        form.reset();
        if (typeof confetti === 'function') {
          confetti({
            particleCount: 80,
            spread: 70,
            origin: { y: 0.6 },
            colors: ['#38bdf8', '#2563eb', '#6366f1', '#ffffff'],
          });
        }
      } else {
        alert(result.message || 'Error creating booking. Please call directly: +91 9414333328');
      }
    } catch (err) {
      console.error('Submission error:', err);
      const fallbackId = 'DCS-' + Date.now().toString().slice(-6);
      showBookingSuccessModal({
        bookingId: fallbackId,
        whatsappUrl: `https://wa.me/919414333328?text=${encodeURIComponent(
          `Hello Satyapal ji, I placed booking ${fallbackId} for ${formData.workType} at ${formData.location}. Phone: ${formData.phone}`
        )}`,
        mailtoUrl: `mailto:${OWNER_CONFIG.email}?subject=Booking ${fallbackId}&body=Hello Satyapal ji, Booking request for ${formData.workType} at ${formData.location}. Phone: ${formData.phone}`,
        booking: formData,
      });
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }
    }
  });
}

function showBookingSuccessModal(data) {
  const modal = document.getElementById('booking-success-modal');
  if (!modal) return;

  const idElem = document.getElementById('success-booking-id');
  const detailsElem = document.getElementById('success-booking-details');
  const waBtn = document.getElementById('success-btn-whatsapp');
  const callBtn = document.getElementById('success-btn-call');

  if (idElem) idElem.textContent = data.bookingId;
  if (detailsElem && data.booking) {
    detailsElem.innerHTML = `
      <div class="space-y-1 text-xs text-slate-300 bg-slate-950 p-3.5 rounded-xl border border-slate-800">
        <div><strong class="text-sky-400">Client Name:</strong> ${data.booking.name} (${data.booking.phone})</div>
        <div><strong class="text-sky-400">Crane Variety:</strong> ${data.booking.craneType}</div>
        <div><strong class="text-sky-400">Service Category:</strong> ${data.booking.workType}</div>
        <div><strong class="text-sky-400">Schedule:</strong> ${data.booking.date} | ${data.booking.timeSlot}</div>
        <div><strong class="text-sky-400">Site Location:</strong> ${data.booking.location} (PIN: ${data.booking.pincode})</div>
      </div>
    `;
  }

  if (waBtn && data.whatsappUrl) {
    waBtn.href = data.whatsappUrl;
  }
  if (callBtn) {
    callBtn.href = `tel:${OWNER_CONFIG.phone1}`;
  }

  modal.classList.add('modal-active');
  document.body.style.overflow = 'hidden';

  const closeBtn = document.getElementById('close-success-modal');
  if (closeBtn) {
    closeBtn.onclick = () => {
      modal.classList.remove('modal-active');
      document.body.style.overflow = '';
    };
  }
}

// 4. CRANE CARD DIRECT SELECTION & SMOOTH SCROLL
function setupCraneSelectionSync() {
  document.querySelectorAll('.btn-choose-crane').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const craneVal = btn.getAttribute('data-crane');
      const hiddenCraneInput = document.getElementById('selected-crane-type');
      if (hiddenCraneInput) hiddenCraneInput.value = craneVal;

      document.querySelectorAll('.crane-option-card').forEach((card) => {
        if (card.getAttribute('data-crane-val') === craneVal) {
          card.classList.add('selected');
        } else {
          card.classList.remove('selected');
        }
      });

      const bookingSection = document.getElementById('booking-section');
      if (bookingSection) {
        bookingSection.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
}

// 5. GALLERY LIGHTBOX
function setupGalleryLightbox() {
  const lightboxModal = document.getElementById('gallery-lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const closeLightbox = document.getElementById('close-lightbox-modal');

  document.querySelectorAll('.gallery-item').forEach((item) => {
    item.addEventListener('click', () => {
      const fullImg = item.getAttribute('data-full-img');
      const caption = item.getAttribute('data-caption') || 'Devatwal Crane Service';

      if (lightboxModal && lightboxImg) {
        lightboxImg.src = fullImg;
        if (lightboxCaption) lightboxCaption.textContent = caption;
        lightboxModal.classList.add('modal-active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (closeLightbox && lightboxModal) {
    closeLightbox.addEventListener('click', () => {
      lightboxModal.classList.remove('modal-active');
      document.body.style.overflow = '';
    });
  }

  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) {
        lightboxModal.classList.remove('modal-active');
        document.body.style.overflow = '';
      }
    });
  }
}

// 6. MOBILE MENU
function setupMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-menu-drawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', () => {
      drawer.classList.toggle('hidden');
    });

    drawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        drawer.classList.add('hidden');
      });
    });
  }
}
