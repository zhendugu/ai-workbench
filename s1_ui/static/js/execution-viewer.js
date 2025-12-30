/**
 * Execution Viewer Module
 * Displays execution history
 */

const ExecutionViewer = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/executions');
            this.renderExecutionList(data.executions);
        } catch (error) {
            S1App.showError('Failed to load executions: ' + error.message);
        }
    },
    
    renderExecutionList(executions) {
        if (!executions || executions.length === 0) {
            S1App.showContent('<p>No executions found.</p>');
            return;
        }
        
        const html = `
            <h2>Executions</h2>
            <div class="execution-list">
                ${executions.map(exec => `
                    <div class="execution-item" onclick="ExecutionViewer.showExecution('${exec.id}')">
                        <h4>${exec.id}</h4>
                        <p>Phase: ${exec.phase || 'N/A'}</p>
                        <p>Status: <span class="wo-status ${exec.status}">${exec.status}</span></p>
                        <div class="execution-stats">
                            <span>Expected: ${exec.expected_runs || 'N/A'}</span>
                            <span>Completed: ${exec.completed_runs || 'N/A'}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showExecution(execId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/executions/${execId}`);
            this.renderExecutionDetails(data);
        } catch (error) {
            S1App.showError('Failed to load execution details: ' + error.message);
        }
    },
    
    renderExecutionDetails(exec) {
        const statusHtml = exec.status_content ? 
            `<div class="markdown-content">${exec.status_content}</div>` : 
            '<p>No status file available.</p>';
        
        const html = `
            <div>
                <button onclick="ExecutionViewer.load()" style="margin-bottom: 20px;">← Back to Executions</button>
                <h2>${exec.id}</h2>
                <p>Phase: ${exec.phase || 'N/A'}</p>
                <p>Status: <span class="wo-status ${exec.status}">${exec.status}</span></p>
                <div class="execution-stats">
                    <span>Expected Runs: ${exec.expected_runs || 'N/A'}</span>
                    <span>Completed Runs: ${exec.completed_runs || 'N/A'}</span>
                </div>
                
                <h3 style="margin-top: 30px;">Status</h3>
                ${statusHtml}
            </div>
        `;
        
        S1App.showContent(html);
    }
};

