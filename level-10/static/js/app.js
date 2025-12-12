async function scanPath() {
    const pathInput = document.getElementById('path-input');
    const scanResult = document.getElementById('scan-result');
    const path = pathInput.value;

    if (!path) {
        alert('Please enter a path to analyze');
        return;
    }

    try {
        const response = await fetch('/api/scan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ path: path })
        });

        const data = await response.json();

        scanResult.classList.remove('hidden');
        scanResult.innerHTML = `
            <div class="space-y-2">
                <div class="flex justify-between items-center">
                    <span class="text-purple-300">Path Length:</span>
                    <span class="text-white font-semibold">${data.length}</span>
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-purple-300">Safe Characters:</span>
                    <span class="text-white font-semibold">${data.safe_characters ? '✓ Yes' : '✗ No'}</span>
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-purple-300">Properly Encoded:</span>
                    <span class="text-white font-semibold">${data.encoded_properly ? '✓ Yes' : '✗ No'}</span>
                </div>
                <div class="flex justify-between items-center">
                    <span class="text-purple-300">Risk Score:</span>
                    <span class="text-white font-semibold ${data.risk_score > 50 ? 'text-red-400' : 'text-green-400'}">${data.risk_score}/100</span>
                </div>
            </div>
        `;

        addLogEntry('Path analysis completed', 'success');
    } catch (error) {
        scanResult.classList.remove('hidden');
        scanResult.innerHTML = `
            <p class="text-red-400">Error analyzing path. Please try again.</p>
        `;
        addLogEntry('Analysis failed', 'error');
    }
}

function addLogEntry(message, type) {
    const activityLog = document.getElementById('activity-log');
    const icon = type === 'success' ? '✓' : '✗';
    const color = type === 'success' ? 'text-green-400' : 'text-red-400';

    const logEntry = document.createElement('div');
    logEntry.className = 'log-entry flex items-start space-x-3 p-3 bg-slate-800/30 rounded-lg';
    logEntry.innerHTML = `
        <span class="${color} text-xs mt-1">${icon}</span>
        <div class="flex-1">
            <p class="text-white text-sm">${message}</p>
            <p class="text-gray-500 text-xs mt-1">Just now</p>
        </div>
    `;

    activityLog.insertBefore(logEntry, activityLog.firstChild);

    if (activityLog.children.length > 5) {
        activityLog.removeChild(activityLog.lastChild);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const pathInput = document.getElementById('path-input');
    if (pathInput) {
        pathInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                scanPath();
            }
        });
    }

    animateCounter('paths-count', 48392);
});

function animateCounter(elementId, target) {
    const element = document.getElementById(elementId);
    if (!element) return;

    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current).toLocaleString();
        }
    }, 20);
}
