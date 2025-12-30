/**
 * Work Order List Module
 * Displays work order registry
 */

const WorkOrderList = {
    async load() {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall('/work-orders');
            this.renderWorkOrderList(data.work_orders);
        } catch (error) {
            S1App.showError('Failed to load work orders: ' + error.message);
        }
    },
    
    renderWorkOrderList(workOrders) {
        if (!workOrders || workOrders.length === 0) {
            S1App.showContent('<p>No work orders found.</p>');
            return;
        }
        
        const html = `
            <h2>Work Orders</h2>
            <div class="work-order-list">
                <div class="work-order-item" style="font-weight: bold; background: #f8f9fa;">
                    <div>ID</div>
                    <div>Phase</div>
                    <div>Status</div>
                    <div>Decision</div>
                </div>
                ${workOrders.map(wo => `
                    <div class="work-order-item" onclick="WorkOrderList.showWorkOrder('${wo.id}')">
                        <div>${wo.id}</div>
                        <div>${wo.phase || 'N/A'}</div>
                        <div><span class="wo-status ${wo.status}">${wo.status}</span></div>
                        <div>${wo.decision_file_path ? '✓' : '✗'}</div>
                    </div>
                `).join('')}
            </div>
        `;
        
        S1App.showContent(html);
    },
    
    async showWorkOrder(woId) {
        S1App.showLoading();
        
        try {
            const data = await S1App.apiCall(`/work-orders/${woId}`);
            this.renderWorkOrderDetails(data);
        } catch (error) {
            S1App.showError('Failed to load work order details: ' + error.message);
        }
    },
    
    renderWorkOrderDetails(wo) {
        const decisionHtml = wo.decision_content ? 
            `<div class="markdown-content">${wo.decision_content}</div>` : 
            '<p>No decision file available.</p>';
        
        const html = `
            <div>
                <button onclick="WorkOrderList.load()" style="margin-bottom: 20px;">← Back to Work Orders</button>
                <h2>${wo.id}</h2>
                <p>Phase: ${wo.phase || 'N/A'}</p>
                <p>Status: <span class="wo-status ${wo.status}">${wo.status}</span></p>
                
                <h3 style="margin-top: 30px;">Decision</h3>
                ${decisionHtml}
            </div>
        `;
        
        S1App.showContent(html);
    }
};

