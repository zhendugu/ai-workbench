// Interface B: Cell Responsibility Structure View - Read-Only Display
// FE_COGNITIVE_GUIDANCE_ADDENDUM compliance

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅显示 Cell 声明性信息，无动态更新

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 所有链接仅用于导航，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示 Cell 事实，无推荐、无执行、无智能判断

// T-2 验收标准：能够找到 Cell，读懂责任描述与边界，不产生"该 Cell 正在工作"的错觉

(function() {
    'use strict';

    // 加载 Cell 视图
    window.loadCellView = function() {
        const cellList = document.getElementById('cell-list');
        if (!cellList) return;

        // 从后端读取 Cell 定义（实际实现中需要后端 API 或直接读取 JSON 文件）
        // 这里使用示例数据，实际应从 backend/subsystems/cell_composition/cells/*.json 读取
        loadCellsData().then(cells => {
            renderCellView(cells);
        }).catch(err => {
            console.error('Failed to load cells:', err);
            cellList.innerHTML = '<p>无法加载 Cell 数据</p>';
        });
    };

    // 加载 Cells 数据
    async function loadCellsData() {
        // 实际实现中，这里应该从后端 API 或直接读取 JSON 文件
        // 示例：fetch('/api/cells') 或直接读取文件系统
        // 这里返回示例数据
        return [
            {
                cell_id: 'test-cell-1',
                role_ids: ['role-1', 'role-2'],
                input_contract: {
                    input_type: 'string',
                    required: true
                },
                output_format: {
                    output_type: 'dict',
                    schema: {}
                },
                registered_at: '2025-12-26T23:32:19.235122'
            }
        ];
    }

    // 渲染 Cell 视图
    function renderCellView(cells) {
        const cellList = document.getElementById('cell-list');
        if (!cellList) return;

        if (cells.length === 0) {
            cellList.innerHTML = '<p>暂无 Cell 定义</p>';
            return;
        }

        let html = '';

        cells.forEach(cell => {
            html += '<div class="cell-item">';
            // 稳定标识符始终可见 (FE_COGNITIVE_GUIDANCE_ADDENDUM Section 6.3)
            html += `<h2>Cell ID: ${escapeHtml(cell.cell_id)}</h2>`;

            // 责任描述（从 Cell 定义推断）
            html += '<div class="cell-item-section">';
            html += '<h3>责任描述</h3>';
            html += `<p>Cell ID: ${escapeHtml(cell.cell_id)}</p>`;
            html += `<p>注册时间: ${escapeHtml(cell.registered_at)}</p>`;
            html += '</div>';

            // 责任边界说明（从 input_contract 和 output_format 推断）
            html += '<div class="cell-item-section">';
            html += '<h3>责任边界说明</h3>';
            html += '<p><strong>输入契约:</strong></p>';
            html += `<pre>${escapeHtml(JSON.stringify(cell.input_contract, null, 2))}</pre>`;
            html += '<p><strong>输出格式:</strong></p>';
            html += `<pre>${escapeHtml(JSON.stringify(cell.output_format, null, 2))}</pre>`;
            html += '</div>';

            // 存在状态（文字标签）
            html += '<div class="cell-item-section">';
            html += '<h3>存在状态</h3>';
            html += '<p>已定义（静态声明）</p>';
            html += '</div>';

            // 附属 Role 约束信息（折叠区域，纯文字）
            html += '<div class="cell-item-section">';
            html += '<h3>附属 Role 约束</h3>';
            html += '<div class="cell-role-list">';
            if (cell.role_ids && cell.role_ids.length > 0) {
                cell.role_ids.forEach(roleId => {
                    html += `<div class="cell-role-item">`;
                    html += `<p><strong>Role ID:</strong> ${escapeHtml(roleId)}</p>`;
                    html += `<p>（Role 约束信息需要从 Role 定义文件读取）</p>`;
                    html += `</div>`;
                });
            } else {
                html += '<p>无附属 Role</p>';
            }
            html += '</div>';
            html += '</div>';

            // 明确表达的事实
            html += '<div class="cell-item-section">';
            html += '<h3>明确表达的事实</h3>';
            html += '<ul>';
            html += '<li>Cell 是责任声明，不是执行者</li>';
            html += '<li>Role 是约束描述，不是实体</li>';
            html += '<li>关系是声明性的，不是执行路径</li>';
            html += '</ul>';
            html += '</div>';

            html += '</div>';
        });

        cellList.innerHTML = html;
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

