document.addEventListener('DOMContentLoaded', function () {
    const urlForm = document.getElementById('urlForm');
    const pathForm = document.getElementById('pathForm');
    const loadLogsBtn = document.getElementById('loadLogs');
    const loadStatsBtn = document.getElementById('loadStats');

    urlForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const url = document.getElementById('urlInput').value;
        const resultDiv = document.getElementById('urlResult');

        resultDiv.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';

        try {
            const response = await fetch('/api/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url })
            });

            const data = await response.json();
            displayUrlResult(data, resultDiv);
        } catch (error) {
            resultDiv.innerHTML = '<div class="alert alert-danger">Error processing request</div>';
        }
    });

    pathForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const path = document.getElementById('pathInput').value;
        const resultDiv = document.getElementById('pathResult');

        resultDiv.innerHTML = '<div class="spinner-border text-success" role="status"><span class="visually-hidden">Loading...</span></div>';

        try {
            const response = await fetch(`/parse/${encodeURIComponent(path)}`);
            const data = await response.json();

            if (data.status === 'success') {
                resultDiv.innerHTML = `
                    <div class="alert alert-success">
                        <h6><i class="bi bi-check-circle"></i> Path Parsed Successfully</h6>
                        <div class="result-box mt-3">
                            <strong>Result:</strong>
                            <pre class="mb-0 mt-2">${escapeHtml(JSON.stringify(data.result, null, 2))}</pre>
                        </div>
                    </div>
                `;
            } else {
                resultDiv.innerHTML = `<div class="alert alert-warning">${data.error || 'Invalid path format'}</div>`;
            }
        } catch (error) {
            resultDiv.innerHTML = '<div class="alert alert-danger">Error processing path</div>';
        }
    });

    loadLogsBtn.addEventListener('click', async function () {
        const logsContainer = document.getElementById('logsContainer');
        logsContainer.innerHTML = '<div class="spinner-border text-dark" role="status"><span class="visually-hidden">Loading...</span></div>';

        try {
            const response = await fetch('/api/logs');
            const data = await response.json();
            displayLogs(data.logs, logsContainer);
        } catch (error) {
            logsContainer.innerHTML = '<div class="alert alert-danger">Error loading logs</div>';
        }
    });

    loadStatsBtn.addEventListener('click', async function () {
        const statsContainer = document.getElementById('statsContainer');
        statsContainer.innerHTML = '<div class="spinner-border text-info" role="status"><span class="visually-hidden">Loading...</span></div>';

        try {
            const response = await fetch('/api/stats');
            const data = await response.json();
            displayStats(data, statsContainer);
        } catch (error) {
            statsContainer.innerHTML = '<div class="alert alert-danger">Error loading statistics</div>';
        }
    });

    function displayUrlResult(data, container) {
        const checks = data.checks;
        const isSafe = data.safe;

        let html = `
            <div class="alert alert-${isSafe ? 'success' : 'warning'}">
                <h6><i class="bi bi-${isSafe ? 'shield-check' : 'exclamation-triangle'}"></i> Security Analysis Complete</h6>
                <div class="result-box mt-3">
                    <div class="check-item">
                        <span>Length Check:</span>
                        <span class="badge bg-${checks.length ? 'success' : 'danger'}">${checks.length ? 'PASS' : 'FAIL'}</span>
                    </div>
                    <div class="check-item">
                        <span>Protocol Check:</span>
                        <span class="badge bg-${checks.protocol ? 'success' : 'danger'}">${checks.protocol ? 'PASS' : 'FAIL'}</span>
                    </div>
                    <div class="check-item">
                        <span>Special Characters:</span>
                        <span class="badge bg-${checks.special_chars ? 'success' : 'danger'}">${checks.special_chars ? 'PASS' : 'FAIL'}</span>
                    </div>
                    <div class="check-item">
                        <span>Encoding Check:</span>
                        <span class="badge bg-${checks.encoding ? 'success' : 'danger'}">${checks.encoding ? 'PASS' : 'FAIL'}</span>
                    </div>
                </div>
                <div class="mt-3">
                    <strong>Overall Status:</strong> 
                    <span class="badge bg-${isSafe ? 'success' : 'warning'} fs-6">${isSafe ? 'SAFE' : 'POTENTIALLY UNSAFE'}</span>
                </div>
            </div>
        `;

        container.innerHTML = html;
    }

    function displayLogs(logs, container) {
        let html = '';
        logs.forEach(log => {
            const levelClass = log.level === 'WARN' ? 'warn' : (log.level === 'ERROR' ? 'error' : '');
            html += `
                <div class="log-entry ${levelClass}">
                    <span class="text-muted">[${log.timestamp}]</span>
                    <span class="badge bg-${log.level === 'INFO' ? 'primary' : 'warning'}">${log.level}</span>
                    ${log.message}
                </div>
            `;
        });
        container.innerHTML = html;
    }

    function displayStats(stats, container) {
        const html = `
            <div class="row g-3">
                <div class="col-md-6">
                    <div class="stat-item">
                        <div class="stat-label">Total Requests</div>
                        <div class="stat-value">${stats.total_requests.toLocaleString()}</div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="stat-item">
                        <div class="stat-label">Blocked Requests</div>
                        <div class="stat-value">${stats.blocked_requests.toLocaleString()}</div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="stat-item">
                        <div class="stat-label">Success Rate</div>
                        <div class="stat-value">${stats.success_rate}%</div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="stat-item">
                        <div class="stat-label">System Uptime</div>
                        <div class="stat-value">${stats.uptime}</div>
                    </div>
                </div>
            </div>
        `;
        container.innerHTML = html;
    }

    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
});
