document.addEventListener("DOMContentLoaded", function() {

    function updateClock() {
        const now = new Date();
        const h = String(now.getHours()).padStart(2, '0');
        const m = String(now.getMinutes()).padStart(2, '0');
        const s = String(now.getSeconds()).padStart(2, '0');
        const el = document.getElementById('live-clock');
        if (el) el.textContent = h + ':' + m + ':' + s;
    }
    setInterval(updateClock, 1000);
    updateClock();

    const container = document.getElementById('particles');
    if (container) {
        for (let i = 0; i < 40; i++) {
            const dot = document.createElement('span');
            const size = Math.random() * 3 + 1;
            dot.style.width = size + 'px';
            dot.style.height = size + 'px';
            dot.style.left = Math.random() * 100 + '%';
            dot.style.animationDuration = (Math.random() * 25 + 15) + 's';
            dot.style.animationDelay = (Math.random() * 20) + 's';
            dot.style.opacity = Math.random() * 0.3 + 0.02;
            container.appendChild(dot);
        }
    }

    const btnEncode = document.getElementById('btn-encode');
    if (btnEncode) {
        btnEncode.addEventListener('click', function(e) {
            e.preventDefault();
            this.innerHTML = '⚡ Traitement...';
            this.style.transform = 'scale(0.96)';
            setTimeout(() => {
                this.innerHTML = '✅ Image Prête !';
                this.style.background = 'linear-gradient(135deg, #00d4ff, #a855f7)';
                this.style.transform = 'scale(1)';
            }, 2000);
        });
    }

    const btnDecode = document.getElementById('btn-decode');
    if (btnDecode) {
        btnDecode.addEventListener('click', function(e) {
            e.preventDefault();
            this.innerHTML = '🔍 Analyse...';
            this.style.transform = 'scale(0.96)';
            setTimeout(() => {
                this.innerHTML = '📩 Message extrait !';
                this.style.background = 'rgba(255,255,255,0.06)';
                this.style.transform = 'scale(1)';
            }, 2000);
        });
    }

    console.log('🛡️ StegoApp Premium v3.0');
});