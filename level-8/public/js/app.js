let currentSession = null;

async function checkSession() {
    try {
        const response = await fetch('/api/session');
        const data = await response.json();

        if (data.authenticated) {
            currentSession = data.user;
            showDashboard();
            loadAnalytics();
            loadLogs();
        } else {
            showLogin();
        }
    } catch (error) {
        showLogin();
    }
}

function showLogin() {
    document.getElementById('loginScreen').classList.remove('hidden');
    document.getElementById('dashboardScreen').classList.add('hidden');
}

function showDashboard() {
    document.getElementById('loginScreen').classList.add('hidden');
    document.getElementById('dashboardScreen').classList.remove('hidden');
    document.getElementById('currentUser').textContent = currentSession;
}

function showAlert(elementId, message, type) {
    const alertEl = document.getElementById(elementId);
    alertEl.className = `alert alert-${type}`;
    alertEl.textContent = message;
    alertEl.classList.remove('hidden');

    setTimeout(() => {
        alertEl.classList.add('hidden');
    }, 5000);
}

document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
        });

        const data = await response.json();

        if (data.success) {
            currentSession = data.user;
            showDashboard();
            loadAnalytics();
            loadLogs();
        } else {
            showAlert('loginAlert', 'Invalid username or password', 'error');
        }
    } catch (error) {
        showAlert('loginAlert', 'Login failed. Please try again.', 'error');
    }
});

document.getElementById('logoutBtn').addEventListener('click', async () => {
    try {
        await fetch('/api/logout', { method: 'POST' });
        currentSession = null;
        showLogin();
        document.getElementById('loginForm').reset();
    } catch (error) {
        console.error('Logout failed:', error);
    }
});

async function loadAnalytics() {
    try {
        const response = await fetch('/api/analytics');
        const data = await response.json();

        if (data.success) {
            document.getElementById('totalQueries').textContent = data.data.total_queries.toLocaleString();
            document.getElementById('activeUsers').textContent = data.data.active_users;
            document.getElementById('avgResponse').textContent = data.data.avg_response_time + 'ms';
            document.getElementById('successRate').textContent = data.data.success_rate + '%';
        }
    } catch (error) {
        console.error('Failed to load analytics:', error);
    }
}

async function loadLogs() {
    try {
        const response = await fetch('/api/logs');
        const data = await response.json();

        if (data.success) {
            const logsContainer = document.getElementById('logsContainer');
            logsContainer.innerHTML = '';

            data.logs.forEach(log => {
                const logEntry = document.createElement('div');
                logEntry.className = `log-entry ${log.level.toLowerCase()}`;

                const timestamp = new Date(log.timestamp * 1000).toLocaleString();
                logEntry.innerHTML = `
                    <span class="log-time">${timestamp}</span>
                    <span class="log-level">[${log.level}]</span>
                    <span>${log.message}</span>
                `;

                logsContainer.appendChild(logEntry);
            });
        }
    } catch (error) {
        console.error('Failed to load logs:', error);
    }
}

document.getElementById('fileUploadArea').addEventListener('click', () => {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            showAlert('uploadAlert', `${data.message} (${data.records} records)`, 'success');
            loadLogs();
        } else {
            showAlert('uploadAlert', data.error || 'Upload failed', 'error');
        }
    } catch (error) {
        showAlert('uploadAlert', 'Upload failed. Please try again.', 'error');
    }

    e.target.value = '';
});

document.getElementById('queryForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const query = document.getElementById('queryInput').value;

    if (!query.trim()) {
        showAlert('queryAlert', 'Please enter a query', 'error');
        return;
    }

    try {
        const response = await fetch('/api/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `query=${encodeURIComponent(query)}`
        });

        const data = await response.json();

        if (data.success) {
            const resultsEl = document.getElementById('queryResults');
            resultsEl.textContent = JSON.stringify(data.results, null, 2);
            resultsEl.classList.remove('hidden');
            showAlert('queryAlert', 'Query executed successfully', 'success');
            loadLogs();
        } else {
            showAlert('queryAlert', data.error || 'Query failed', 'error');
        }
    } catch (error) {
        showAlert('queryAlert', 'Query execution failed', 'error');
    }
});

checkSession();
