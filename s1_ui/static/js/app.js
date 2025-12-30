/**
 * S1 Operator Control Surface - Main App Router
 * 
 * READ-ONLY INTERFACE ONLY.
 * No execution, no modification, no recommendations.
 */

const API_BASE = '/api';

let currentView = 'phases';

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    setupNavigation();
    loadView('phases');
});

function setupNavigation() {
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const view = btn.dataset.view;
            loadView(view);
            
            // Update active state
            navButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
}

function loadView(viewName) {
    currentView = viewName;
    const content = document.getElementById('content');
    const loading = document.getElementById('loading');
    
    content.classList.add('hidden');
    loading.classList.remove('hidden');
    
    switch(viewName) {
        case 'phases':
            PhaseView.load();
            break;
        case 'work-orders':
            WorkOrderList.load();
            break;
        case 'executions':
            ExecutionViewer.load();
            break;
        case 'evidence':
            EvidenceBrowser.load();
            break;
        case 'decisions':
            DecisionViewer.load();
            break;
        case 'traceability':
            TraceabilityView.load();
            break;
        default:
            showError('Unknown view: ' + viewName);
    }
}

function showError(message) {
    const content = document.getElementById('content');
    const loading = document.getElementById('loading');
    
    loading.classList.add('hidden');
    content.classList.remove('hidden');
    content.innerHTML = `<div class="error">Error: ${message}</div>`;
}

function showLoading() {
    const content = document.getElementById('content');
    const loading = document.getElementById('loading');
    
    content.classList.add('hidden');
    loading.classList.remove('hidden');
}

function showContent(html) {
    const content = document.getElementById('content');
    const loading = document.getElementById('loading');
    
    loading.classList.add('hidden');
    content.classList.remove('hidden');
    content.innerHTML = html;
}

async function apiCall(endpoint) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`);
        if (!response.ok) {
            throw new Error(`API error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

// Export for use by view modules
window.S1App = {
    loadView,
    showError,
    showLoading,
    showContent,
    apiCall
};

