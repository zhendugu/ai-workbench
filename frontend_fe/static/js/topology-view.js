// Interface C: Declarative Topology View - Read-Only Display

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示声明性拓扑结构，无动画、无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 所有节点仅用于显示，无点击触发行为

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示拓扑事实，无推荐、无执行、无智能判断

(function() {
    'use strict';

    // 加载拓扑视图
    window.loadTopologyView = function() {
        const topologyGraph = document.getElementById('topology-graph');
        if (!topologyGraph) return;

        // 从 WORKFLOW_DECLARATION.md 读取数据（实际实现中需要后端 API 或直接读取文件）
        // 这里使用示例数据，实际应从声明文件读取
        const topologyData = {
            nodes: [
                { node_id: 'catalyst_hub', node_type: 'catalyst_hub', description: 'Workflow stabilizer and correction system' },
                { node_id: 'cell_composition', node_type: 'cell', description: 'Minimum independent delivery unit' },
                { node_id: 'role_management', node_type: 'role', description: 'AI behavior constraint unit' },
                { node_id: 'task_force', node_type: 'task_force', description: 'Temporary work group' }
            ],
            edges: [
                { from: 'catalyst_hub', to: 'cell_composition', relationship_type: 'routes_to', description: 'Catalyst Hub routes requirements to Cells' },
                { from: 'cell_composition', to: 'role_management', relationship_type: 'composed_of', description: 'Cell is composed of Roles' },
                { from: 'catalyst_hub', to: 'task_force', relationship_type: 'triggers', description: 'Catalyst Hub triggers Task Force creation' },
                { from: 'task_force', to: 'cell_composition', relationship_type: 'extracts_from', description: 'Task Force extracts capabilities from Cells' }
            ]
        };

        renderTopologyView(topologyData);
    };

    // 渲染拓扑视图
    function renderTopologyView(data) {
        const topologyGraph = document.getElementById('topology-graph');
        if (!topologyGraph) return;

        let html = '';

        // 明确表达的事实
        html += '<div style="margin-bottom: 2rem;">';
        html += '<h3>明确表达的事实</h3>';
        html += '<ul>';
        html += '<li>这是结构声明，不是执行流程</li>';
        html += '<li>节点关系是语义性的，不是时序性的</li>';
        html += '</ul>';
        html += '</div>';

        // 节点列表（仅 Cell）
        html += '<div style="margin-bottom: 2rem;">';
        html += '<h3>声明性节点（仅 Cell）</h3>';
        data.nodes.forEach(node => {
            if (node.node_type === 'cell') {
                html += '<div class="topology-node">';
                html += `<p><strong>${escapeHtml(node.node_id)}</strong></p>`;
                html += `<p>${escapeHtml(node.description)}</p>`;
                html += '</div>';
            }
        });
        html += '</div>';

        // 关系类型标注（文字：依赖/参考）
        html += '<div>';
        html += '<h3>声明性关系类型</h3>';
        data.edges.forEach(edge => {
            html += '<div class="topology-relationship">';
            html += `<p><strong>${escapeHtml(edge.from)}</strong> → <strong>${escapeHtml(edge.to)}</strong></p>`;
            html += `<p>关系类型: ${escapeHtml(edge.relationship_type)}</p>`;
            html += `<p>${escapeHtml(edge.description)}</p>`;
            html += '</div>';
        });
        html += '</div>';

        topologyGraph.innerHTML = html;
    }

    // HTML 转义
    function escapeHtml(text) {
        if (typeof text !== 'string') {
            text = String(text);
        }
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
})();

