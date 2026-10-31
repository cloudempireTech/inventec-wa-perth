// Inventec WA Pty Ltd - Precision Engineering Engine
document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-menu-drawer');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.toggle('open');
      const isOpen = mobileDrawer.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // 2. Dynamic Typewriter Headline
  const typewriterEl = document.querySelector('.typewriter-text');
  if (typewriterEl) {
    const phrases = [
      '5-Axis Precision CNC Milling',
      'Heavy Drivetrain & Lathe Turning',
      'Wire & Die Sinker EDM',
      'Pilbara Mining Component Overhauls',
      'Certified Structural Metal Fabrication'
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function typeLoop() {
      const currentPhrase = phrases[phraseIdx];
      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx - 1);
        charIdx--;
        typingSpeed = 50;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIdx + 1);
        charIdx++;
        typingSpeed = 110;
      }

      if (!isDeleting && charIdx === currentPhrase.length) {
        typingSpeed = 2200;
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % phrases.length;
        typingSpeed = 500;
      }

      setTimeout(typeLoop, typingSpeed);
    }
    typeLoop();
  }

  // 3. Animated Number Counters
  const counterEls = document.querySelectorAll('.stat-number');
  if (counterEls.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target'), 10);
          const prefix = el.getAttribute('data-prefix') || '';
          const suffix = el.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1800;

          const timer = setInterval(() => {
            count += Math.ceil(target / 45);
            if (count >= target) {
              el.textContent = `${prefix}${target.toLocaleString()}${suffix}`;
              clearInterval(timer);
            } else {
              el.textContent = `${prefix}${count.toLocaleString()}${suffix}`;
            }
          }, 35);

          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    counterEls.forEach(el => observer.observe(el));
  }

  // 4. Interactive Precision RFQ Feasibility Widget
  const rfqBtn = document.getElementById('btnCalculateRFQ');
  if (rfqBtn) {
    rfqBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const checkboxes = document.querySelectorAll('input[name="process_req"]:checked');
      const material = document.getElementById('rfqMaterial') ? document.getElementById('rfqMaterial').value : '';
      const tolerance = document.getElementById('rfqTolerance') ? document.getElementById('rfqTolerance').value : '';
      const resultTitle = document.getElementById('rfqResultTitle');
      const resultDesc = document.getElementById('rfqResultDesc');
      const resultUrgency = document.getElementById('rfqResultUrgency');

      if (checkboxes.length === 0) {
        resultTitle.textContent = "General Engineering Consultation";
        resultDesc.textContent = "Send your 2D/3D CAD models (STEP, IGES, DXF) to our Maddington engineering office for detailed toolpathing and material quotation.";
        resultUrgency.innerHTML = "<strong>Lead Time:</strong> Rapid engineering review within 4 business hours.";
        return;
      }

      let processes = Array.from(checkboxes).map(cb => cb.value);

      if (processes.includes('edm') || tolerance.includes('0.005')) {
        resultTitle.textContent = "High-Precision EDM & Micron Grinding Setup";
        resultDesc.textContent = `For ${material} requiring ${tolerance} tolerance, we route to our Wire EDM or CNC cylindrical grinding suite with comprehensive CMM coordinate inspection certificate.`;
        resultUrgency.innerHTML = "<strong>Feasibility: Confirmed In-House.</strong> 100% CMM dimensional report supplied with delivery.";
      } else if (processes.includes('welding') || processes.includes('boring')) {
        resultTitle.textContent = "Heavy Fabrication & Boring Integration";
        resultDesc.textContent = `Components requiring certified MIG/TIG structural welding paired with horizontal line boring. Ultrasonic weld NDT testing and stress relief available.`;
        resultUrgency.innerHTML = "<strong>Capability: Heavy Bay Equipped.</strong> Overhead gantry cranes support multi-tonne assemblies.";
      } else if (processes.includes('breakdown')) {
        resultTitle.textContent = "Urgent 24/7 Mining & Breakdown Dispatch";
        resultDesc.textContent = `Immediate priority workshop queuing. We coordinate overnight transport from Pilbara or Goldfields mine sites for rapid reverse engineering and emergency machining.`;
        resultUrgency.innerHTML = "<strong>Status: Priority Breakdown Response.</strong> Call 1300 344 136 for immediate mobilization.";
      } else {
        resultTitle.textContent = "Multi-Axis CNC Milling & Turning Production";
        resultDesc.textContent = `Production run scheduled across our Mazak and Okuma VMC / CNC lathe centres with optimized cycle times in ${material}.`;
        resultUrgency.innerHTML = "<strong>Standard Turnaround:</strong> 5 - 10 working days, or expedite on request.";
      }
    });
  }
});
