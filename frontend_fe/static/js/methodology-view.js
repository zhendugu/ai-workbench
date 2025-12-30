// Interface E: Methodology Perspective Switcher - Read-Only Display

// 自检规则：这个界面是否让人产生"系统在运行"的感觉？
// 答案：NO - 仅改变显示视角，不改变数据，不触发行为

// 自检规则：是否让人感觉"点一下就能完成事情"？
// 答案：NO - 切换仅改变界面分组或标注方式，无执行操作

// 自检规则：是否在任何地方暗示了推荐、执行或智能判断？
// 答案：NO - 仅显示方法论选择，无推荐、无执行、无智能判断

(function() {
    'use strict';

    // 初始化方法论切换器
    function initMethodologySwitcher() {
        const methodologySelect = document.getElementById('methodology-select');
        if (!methodologySelect) return;

        // 从 METHODOLOGY_DECLARATION.md 读取数据（实际实现中需要后端 API 或直接读取文件）
        const methodologies = [
            { id: 'work-order-structure', name: 'Work Order Structure', status: 'active' },
            { id: 'execution-pattern', name: 'Execution Pattern', status: 'active' },
            { id: 'phase-based-organization', name: 'Phase-Based Organization', status: 'active' },
            { id: 'epoch-based-time-fractured-intelligence', name: 'Epoch-Based Time-Fractured Intelligence', status: 'frozen' },
            { id: 'constitutional-compliance-audit', name: 'Constitutional Compliance Audit', status: 'active' }
        ];

        // 填充选项
        methodologies.forEach(methodology => {
            const option = document.createElement('option');
            option.value = methodology.id;
            option.textContent = `${methodology.name} (${methodology.status})`;
            methodologySelect.appendChild(option);
        });

        // 设置切换事件（仅改变显示，不改变数据）
        methodologySelect.addEventListener('change', function() {
            const selectedMethodologyId = this.value;
            applyMethodologyPerspective(selectedMethodologyId);
        });
    }

    // 应用方法论视角（仅改变界面 B/C/D 的分组或标注方式）
    function applyMethodologyPerspective(methodologyId) {
        // 实际实现中，这里应该根据方法论改变界面 B/C/D 的显示方式
        // 但不改变任何数据，不触发任何行为
        console.log('Methodology perspective changed to:', methodologyId);
        // 这里可以更新界面 B/C/D 的显示，但仅改变标注方式
    }

    // 初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMethodologySwitcher);
    } else {
        initMethodologySwitcher();
    }
})();

