// static/js/edit_listing.js

document.addEventListener('DOMContentLoaded', () => {
  // === [ 0. FALLBACK IMAGE HANDLER FOR MOCKUP THUMBS ] ===
  document.querySelectorAll('.mockup-thumb-img').forEach(img => {
    img.addEventListener('error', function handleError() {
      if (this.dataset.fallback && this.src !== this.dataset.fallback) {
        this.src = this.dataset.fallback;
      }
      this.onerror = null; // Prevent loop
    });
  });

  // === [ 1. MODAL CAROUSEL LOGIC ] ===
  const carousel = document.getElementById('mockup-carousel');
  const carouselImg = document.getElementById('carousel-img');
  const images = Array.from(document.querySelectorAll('.mockup-img-link, .main-thumb-link'));
  let currentIndex = 0;

  function showImage(index) {
    if (index >= 0 && index < images.length) {
      currentIndex = index;
      carouselImg.src = images[currentIndex].dataset.img;
      carousel.classList.add('active');
    }
  }

  function hideCarousel() {
    carousel.classList.remove('active');
  }

  images.forEach((link, index) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      showImage(index);
    });
  });

  if (carousel) {
    carousel.querySelector('#carousel-close').addEventListener('click', hideCarousel);
    carousel.querySelector('#carousel-prev').addEventListener('click', () => showImage((currentIndex - 1 + images.length) % images.length));
    carousel.querySelector('#carousel-next').addEventListener('click', () => showImage((currentIndex + 1) % images.length));
    
    carousel.addEventListener('click', (e) => {
        if (e.target === carousel) {
            hideCarousel();
        }
    });

    document.addEventListener('keydown', (e) => {
      if (carousel.classList.contains('active')) {
        if (e.key === 'ArrowLeft') showImage((currentIndex - 1 + images.length) % images.length);
        if (e.key === 'ArrowRight') showImage((currentIndex + 1) % images.length);
        if (e.key === 'Escape') hideCarousel();
      }
    });
  }

  // === [ 2. ASYNC MOCKUP SWAP LOGIC - Delegated & hardened ] ===
  const mockupGrid = document.querySelector('.mockup-preview-grid');
  if (mockupGrid) {
    mockupGrid.addEventListener('click', (event) => {
      const btn = event.target.closest('.swap-btn');
      if (!btn) return;
      event.preventDefault();
      handleSwapClick(btn).catch(err => console.error('Swap handler error:', err));
    });
  }

  async function handleSwapClick(button) {
    const mockupCard = button.closest('.mockup-card');
    if (!mockupCard) return;

    // Prevent concurrent swaps on the same card
    if (mockupCard.classList.contains('swapping')) return;

    const slotIndex = parseInt(button.dataset.index, 10);
    const controlsContainer = button.closest('.swap-controls');
    if (!controlsContainer) return;
    const select = controlsContainer.querySelector('select[name="new_category"]');
    if (!select) return;

    const newCategory = select.value;
    const liveNode = mockupCard.querySelector('.swap-live');
    const statusNode = controlsContainer.querySelector('.swap-status');
    const mockupImg = document.getElementById(`mockup-img-${slotIndex}`);
    const mockupLink = document.getElementById(`mockup-link-${slotIndex}`);

    // Defensive check for config
    if (!window.EDIT_INFO || !window.EDIT_INFO.seoFolder) {
      if (statusNode) { statusNode.textContent = 'Page configuration error.'; statusNode.style.display = 'block'; }
      return;
    }

    // If selecting same as current category, no-op with hint
    const currentCategory = select.querySelector('option[selected]') ? select.querySelector('option[selected]').value : null;
    if (currentCategory && currentCategory === newCategory) {
      if (statusNode) {
        statusNode.textContent = 'Category unchanged.'; statusNode.style.display = 'block';
        setTimeout(() => { statusNode.style.display = 'none'; }, 1500);
      }
      return;
    }

    // Setup state
    mockupCard.classList.add('swapping');
    mockupCard.setAttribute('aria-busy', 'true');
    select.disabled = true;
    button.disabled = true;
    const swapLabel = button.querySelector('.swap-label');
    if (swapLabel) swapLabel.style.visibility = 'hidden';
    const spinner = button.querySelector('.swap-spinner');
    if (spinner) spinner.style.display = 'block';
    if (liveNode) liveNode.textContent = `Generating new mockup in ${newCategory}…`;

    // Prepare payload and headers (CSRF if present)
    const payload = {
      seo_folder: window.EDIT_INFO.seoFolder,
      slot_index: slotIndex,
      new_category: newCategory,
      aspect: window.EDIT_INFO.aspect,
      current_mockup_src: mockupImg ? (mockupImg.src.split('/').pop().split('?')[0]) : ''
    };

    const headers = { 'Content-Type': 'application/json' };
    const csrf = document.querySelector('meta[name="csrf-token"]');
    if (csrf) headers['X-CSRF-Token'] = csrf.getAttribute('content');

    // AbortController + timeout + retry policy
    let attempts = 0;
    const maxAttempts = 3;
    const baseTimeout = 45000; // 45s
    let responseData = null;

    while (attempts < maxAttempts) {
      attempts += 1;
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), baseTimeout * Math.pow(2, attempts - 1));

      try {
        const resp = await fetch('/edit/swap-mockup-api', {
          method: 'POST',
          headers,
          body: JSON.stringify(payload),
          signal: controller.signal,
        });

        clearTimeout(timeoutId);

        // Retry on transient server errors
        if ([502, 503, 504].includes(resp.status) && attempts < maxAttempts) {
          await delay(500 * Math.pow(2, attempts));
          continue;
        }

        responseData = await resp.json().catch(() => ({}));
        if (!resp.ok || !responseData.success) {
          throw new Error(responseData.error || `Server returned ${resp.status}`);
        }

        // Success path
        break;
      } catch (err) {
        clearTimeout(timeoutId);
        // If aborted due to timeout, present a user-friendly message but allow retry
        if (err.name === 'AbortError') {
          if (attempts < maxAttempts) {
            if (liveNode) liveNode.textContent = 'Still generating… retrying';
            await delay(800 * attempts);
            continue;
          }
          // final failure
          showInlineError(statusNode, 'Request timed out. Please try again.');
        } else {
          if (attempts < maxAttempts && /Server returned 5../.test(err.message)) {
            await delay(400 * attempts);
            continue;
          }
          showInlineError(statusNode, err.message || 'Swap failed');
        }
        // break loop on non-retriable errors
        responseData = null;
        break;
      }
    }

    // If responseData is null => failure; cleanup state
    if (!responseData) {
      cleanupSwapState();
      return;
    }

    // Update images and links, then poll for image readiness
    try {
      const ts = Date.now();
      if (mockupImg && responseData.new_thumb_url) {
        mockupImg.dataset.fallback = `${responseData.new_mockup_url}?t=${ts}`;
        mockupImg.src = `${responseData.new_thumb_url}?t=${ts}`;
      }
      if (mockupLink && responseData.new_mockup_url) {
        mockupLink.dataset.img = `${responseData.new_mockup_url}?t=${ts}`;
        mockupLink.href = `${responseData.new_mockup_url}?t=${ts}`;
      }

      if (liveNode) liveNode.textContent = 'Mockup updated.';
      if (statusNode) { statusNode.textContent = 'Updated'; statusNode.style.display = 'block'; setTimeout(() => statusNode.style.display='none', 1500); }

      // If image fails 404 briefly, poll to see when it becomes available
      if (mockupImg) await pollImageReady(mockupImg, 1000, 10000);

    } catch (err) {
      console.error('Apply update failed:', err);
      showInlineError(statusNode, 'Could not apply new mockup image.');
    } finally {
      cleanupSwapState();
    }

    function cleanupSwapState() {
      mockupCard.classList.remove('swapping');
      mockupCard.removeAttribute('aria-busy');
      select.disabled = false;
      button.disabled = false;
      if (swapLabel) swapLabel.style.visibility = '';
      if (spinner) spinner.style.display = 'none';
      if (liveNode) setTimeout(() => { liveNode.textContent = ''; }, 500);
    }

    function showInlineError(node, text) {
      if (node) {
        node.textContent = text;
        node.style.display = 'block';
      } else {
        console.warn('Swap error:', text);
      }
      setTimeout(() => { if (node) node.style.display = 'none'; }, 5000);
    }

    function delay(ms) { return new Promise(res => setTimeout(res, ms)); }

    async function pollImageReady(imgEl, interval = 1000, timeout = 10000) {
      const start = Date.now();
      return new Promise((resolve) => {
        if (!imgEl) return resolve(false);
        const originalOnError = imgEl.onerror;
        let done = false;

        const check = () => {
          // If image naturalWidth > 1 it's loaded
          if (imgEl.naturalWidth && imgEl.naturalWidth > 1) {
            done = true;
            imgEl.onerror = originalOnError;
            return resolve(true);
          }
          if (Date.now() - start >= timeout) {
            done = true;
            imgEl.onerror = originalOnError;
            return resolve(false);
          }
          setTimeout(check, interval);
        };

        // Ensure onerror fallback remains available
        imgEl.onerror = function() { /* leave fallback handler as-is */ };
        // Start checks
        check();
      });
    }
  }

  // === [ 3. ASYNC UPDATE IMAGE URLS ] ===
  const updateLinksBtn = document.getElementById('update-links-btn');
  if (updateLinksBtn) {
    updateLinksBtn.addEventListener('click', async () => {
      const originalText = updateLinksBtn.textContent;
      updateLinksBtn.textContent = 'Updating...';
      updateLinksBtn.disabled = true;

      try {
        const url = `/update-links/${window.EDIT_INFO.aspect}/${window.EDIT_INFO.seoFolder}.jpg`;
        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Accept': 'application/json' }
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.message || 'Server error');
        
        const joined = data.images.join('\n');
        document.getElementById('images-input').value = joined;
        const publicBox = document.getElementById('public-image-urls');
        if (publicBox) publicBox.value = joined;
      } catch (error) {
        alert(`Error updating image links: ${error.message}`);
      } finally {
        updateLinksBtn.textContent = originalText;
        updateLinksBtn.disabled = false;
      }
    });
  }
  
  // === [ 4. ASYNC GENERIC TEXT REWORDING ] ===
  const rewordContainer = document.getElementById('generic-text-reworder');
  if (rewordContainer) {
    const descriptionTextarea = document.getElementById('description-input');
    const spinner = document.getElementById('reword-spinner');
    const genericTextInput = document.getElementById('generic-text-input');
    const buttons = rewordContainer.querySelectorAll('button');

    rewordContainer.addEventListener('click', async (event) => {
      if (!event.target.matches('#reword-openai-btn, #reword-gemini-btn')) {
        return;
      }
      const button = event.target;
      const provider = button.dataset.provider;
      const genericText = genericTextInput.value;
      const currentDescription = descriptionTextarea.value;
      
      buttons.forEach(b => b.disabled = true);
      spinner.style.display = 'block';

      try {
          const response = await fetch('/api/reword-generic-text', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                  provider: provider,
                  artwork_description: currentDescription,
                  generic_text: genericText
              })
          });

          const data = await response.json();
          if (!response.ok) throw new Error(data.error || 'Failed to reword text.');
          
          genericTextInput.value = data.reworded_text;

      } catch (error) {
          console.error('Reword failed:', error);
          alert(`Error: ${error.message}`);
      } finally {
          buttons.forEach(b => b.disabled = false);
          spinner.style.display = 'none';
      }
    });
  }

  // === [ 5. RE-ANALYZE MODAL TRIGGER ] ===
  const analyzeForm = document.querySelector('.analyze-form');
  if (analyzeForm) {
    analyzeForm.addEventListener('submit', () => {
      // Open the modal from analysis-modal.js when the form is submitted
      if (window.AnalysisModal) {
        window.AnalysisModal.open();
      }
    });
  }
});