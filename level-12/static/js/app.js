document.addEventListener('DOMContentLoaded', function() {
    loadSystemMetrics();
    
    setInterval(loadSystemMetrics, 30000);
});

function loadSystemMetrics() {
    fetchMetric('memory', 'memory-data');
    fetchMetric('cpu', 'cpu-data');
    fetchMetric('disk', 'disk-data');
    fetchMetric('network', 'network-data');
    
    updateLastUpdate();
}

function fetchMetric(component, elementId) {
    fetch(`/cgi-bin/system-info.cgi?component=${component}`)
        .then(response => response.json())
        .then(data => {
            const element = document.getElementById(elementId);
            if (data.status === 'ok') {
                element.textContent = data.data.trim();
                element.classList.remove('text-danger');
                element.classList.add('text-success');
            } else {
                element.textContent = 'Error loading data';
                element.classList.remove('text-success');
                element.classList.add('text-danger');
            }
        })
        .catch(error => {
            const element = document.getElementById(elementId);
            element.textContent = 'Connection error';
            element.classList.remove('text-success');
            element.classList.add('text-danger');
        });
}

function updateLastUpdate() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    const dateString = now.toLocaleDateString();
    document.getElementById('last-update').textContent = `${dateString} ${timeString}`;
}
