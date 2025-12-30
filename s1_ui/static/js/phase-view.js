/**
 * Phase View Module
 * Displays phase overview and details
 */

const PhaseView = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/phases');
            this.renderPhaseList(data.phases);
        } catch (error) {
            S1App.showError('Failed to load phases: ' + error.message);
        }
    },
    
    renderPhaseList(phases) {
        if (!phases || phases.length === 0) {
            S1App.showContent('<p>No phases found.</p>');
            return;
        }
        
        const html = `
            <h2>Phases</h2>
            <div class="phase-list">
                ${phases.map(phase => `
                    <div class="phase-card" onclick="PhaseView.showPhase('${phase.id}')">
                        <h3>Phase ${phase.id}</h3>
                        <p>Status: <span class="phase-status ${phase.status}">${phase.status}</span></p>
                        <p>Work Orders: ${phase.work_order_count || 0}</p>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showPhase(phaseId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/phases/${phaseId}`);
            this.renderPhaseDetails(data);
        } catch (error) {
            S1App.showError('Failed to load phase details: ' + error.message);
        }
    },
    
    renderPhaseDetails(phase) {
        const statusHtml = phase.status_content ? 
            `<div class="markdown-content">${phase.status_content}</div>` : 
            '<p>No status file available.</p>';
        
        const closureHtml = phase.closure_content ? 
            `<div class="markdown-content">${phase.closure_content}</div>` : 
            '<p>No closure summary available.</p>';
        
        const html = `
            <div>
                <button onclick="PhaseView.load()" style="margin-bottom: 20px;">← Back to Phases</button>
                <h2>Phase ${phase.id}</h2>
                <p>Status: <span class="phase-status ${phase.status}">${phase.status}</span></p>
                
                <h3 style="margin-top: 30px;">Status</h3>
                ${statusHtml}
                
                <h3 style="margin-top: 30px;">Closure Summary</h3>
                ${closureHtml}
                
                <h3 style="margin-top: 30px;">Work Orders (${phase.work_orders.length})</h3>
                <ul>
                    ${phase.work_orders.map(wo => `<li>${wo}</li>`).join('')}
                </ul>
            </div>
        `;
        
        S1App.showContent(html);
    }
};

