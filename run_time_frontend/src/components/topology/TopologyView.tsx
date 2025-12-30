// L3: Topology View (Read-Only)
// Authority: RT_FE_REQ_FROZEN.md Section 3.4

import { useState, useRef, useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import type { CellViewModel, RelationshipViewModel } from '../../types/viewModels'

interface TopologyViewProps {
  cells: CellViewModel[]
  relations: RelationshipViewModel[]
}

// Node position state (layout only, no semantic meaning)
interface NodePosition {
  x: number
  y: number
}

export function TopologyView({ cells, relations }: TopologyViewProps) {
  const [viewMode, setViewMode] = useState<'canvas' | 'list'>('canvas')
  const [selectedRelationId, setSelectedRelationId] = useState<string | null>(null)
  const [nodePositions, setNodePositions] = useState<Record<string, NodePosition>>({})
  const svgRef = useRef<SVGSVGElement>(null)

  // Initialize node positions (geometric layout only) - RT_FE_REQ_FROZEN.md Section 3.4
  // Layout is frozen at freeze time, not draggable
  useEffect(() => {
    if (cells.length > 0 && Object.keys(nodePositions).length === 0) {
      const positions: Record<string, NodePosition> = {}
      const radius = 200
      const centerX = 400
      const centerY = 300
      
      cells.forEach((cell, index) => {
        const angle = (2 * Math.PI * index) / cells.length
        positions[cell.cellIdentifier] = {
          x: centerX + radius * Math.cos(angle),
          y: centerY + radius * Math.sin(angle),
        }
      })
      
      setNodePositions(positions)
    }
  }, [cells, nodePositions])

  const { t } = useTranslation()

  // Get relation type label (noun form) - RT_FE_REQ_FROZEN.md Section 3.4
  const getRelationTypeLabel = (type: RelationshipViewModel['relationshipType']): string => {
    switch (type) {
      case 'dependency':
        return t('topology.dependency')
      case 'reference':
        return t('topology.reference')
      case 'input_output':
        return t('topology.inputOutput')
      default:
        return type
    }
  }

  // Get relation line style (neutral, bidirectional) - RT_FE_REQ_FROZEN.md Section 3.4
  const getRelationLineStyle = (type: RelationshipViewModel['relationshipType']): { stroke: string; strokeDasharray?: string } => {
    switch (type) {
      case 'dependency':
        return { stroke: '#666' }
      case 'reference':
        return { stroke: '#666', strokeDasharray: '5,5' }
      case 'input_output':
        return { stroke: '#333' }
      default:
        return { stroke: '#666' }
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">{t('topology.title')}</h2>
          <p className="text-sm text-gray-600 mt-1">
            {t('topology.description')}
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded read-only-indicator">
          {t('topology.readOnly')}
        </span>
      </div>

      {/* Anti-Misinterpretation Guardrail - RT_FE_REQ_FROZEN.md Section 6.2 */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-gray-700">
          {t('topology.frozenDeclarativeTopology')}
        </p>
      </div>

      {/* View Mode Toggle - RT_FE_REQ_FROZEN.md Section 3.4 */}
      <div className="bg-white border rounded-lg p-4">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-base font-mono">{t('topology.viewMode')}</h3>
          <div className="flex gap-2">
            <button
              onClick={() => setViewMode('canvas')}
              className={`px-4 py-2 text-sm border rounded ${
                viewMode === 'canvas' ? 'bg-gray-100 border-gray-600' : 'bg-gray-50'
              }`}
            >
              {t('topology.canvas')}
            </button>
            <button
              onClick={() => setViewMode('list')}
              className={`px-4 py-2 text-sm border rounded ${
                viewMode === 'list' ? 'bg-gray-100 border-gray-600' : 'bg-gray-50'
              }`}
            >
              {t('topology.list')}
            </button>
          </div>
        </div>
      </div>

      {/* Mode A: Topology Canvas (Read-Only) - RT_FE_REQ_FROZEN.md Section 3.4 */}
      {viewMode === 'canvas' && (
        <div className="bg-white border rounded-lg p-6">
          {/* UI Copy Requirement - RT_FE_REQ_FROZEN.md Section 3.4 */}
          <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded">
            <p className="text-sm text-gray-700">
              <strong>{t('topology.declarativeTopologyView')}</strong>
              <br />
              {t('topology.relationshipsStructuralDependencies')}
            </p>
          </div>

          {cells.length === 0 ? (
            <div className="h-[500px] flex items-center justify-center text-gray-400 border-2 border-dashed rounded">
              <div className="text-center">
                <p className="text-sm">{t('topology.noCellsDefined')}</p>
                <p className="text-xs mt-1">{t('topology.noTopologyToVisualize')}</p>
              </div>
            </div>
          ) : (
            <div className="relative">
              <svg
                ref={svgRef}
                width="100%"
                height="600"
                className="border rounded bg-gray-50"
              >
                {/* Render edges (relations) - No arrows, bidirectional - RT_FE_REQ_FROZEN.md Section 3.4 */}
                {relations.map((relation) => {
                  const sourcePos = nodePositions[relation.sourceCellIdentifier]
                  const targetPos = nodePositions[relation.targetCellIdentifier]
                  
                  if (!sourcePos || !targetPos) return null

                  const lineStyle = getRelationLineStyle(relation.relationshipType)
                  const midX = (sourcePos.x + targetPos.x) / 2
                  const midY = (sourcePos.y + targetPos.y) / 2

                  return (
                    <g key={relation.relationshipIdentifier}>
                      {/* Edge line - bidirectional, no arrow - RT_FE_REQ_FROZEN.md Section 3.4 */}
                      <line
                        x1={sourcePos.x}
                        y1={sourcePos.y}
                        x2={targetPos.x}
                        y2={targetPos.y}
                        stroke={lineStyle.stroke}
                        strokeWidth={2}
                        strokeDasharray={lineStyle.strokeDasharray}
                        className="cursor-pointer"
                        onClick={() => setSelectedRelationId(relation.relationshipIdentifier)}
                      />
                      {/* Relation type label (noun form) */}
                      <g
                        transform={`translate(${midX}, ${midY})`}
                        className="cursor-pointer"
                        onClick={() => setSelectedRelationId(relation.relationshipIdentifier)}
                      >
                        <rect
                          x="-40"
                          y="-8"
                          width="80"
                          height="16"
                          fill="white"
                          stroke={lineStyle.stroke}
                          strokeWidth="1"
                          rx="2"
                        />
                        <text
                          textAnchor="middle"
                          dominantBaseline="middle"
                          className="text-xs font-mono fill-gray-700"
                        >
                          {getRelationTypeLabel(relation.relationshipType)}
                        </text>
                      </g>
                    </g>
                  )
                })}

                {/* Render nodes (cells) - Read-only - RT_FE_REQ_FROZEN.md Section 3.4 */}
                {cells.map((cell) => {
                  const pos = nodePositions[cell.cellIdentifier]
                  if (!pos) return null

                  return (
                    <g key={cell.cellIdentifier}>
                      {/* Node circle - No drag, read-only */}
                      <circle
                        cx={pos.x}
                        cy={pos.y}
                        r="40"
                        fill="white"
                        stroke="#333"
                        strokeWidth="2"
                        className="cursor-pointer"
                        onClick={() => {
                          // Navigate to cell detail (read-only)
                          // In real implementation, this would navigate to Structure View with cell selected
                          // Placeholder: cell detail navigation (read-only)
                        }}
                      />
                      {/* Cell name text */}
                      <text
                        x={pos.x}
                        y={pos.y}
                        textAnchor="middle"
                        dominantBaseline="middle"
                        className="text-xs font-mono fill-gray-800 pointer-events-none"
                        style={{ userSelect: 'none' }}
                      >
                        {cell.cellName}
                      </text>
                    </g>
                  )
                })}
              </svg>
            </div>
          )}
        </div>
      )}

      {/* Mode B: Relation List (Read-Only) - RT_FE_REQ_FROZEN.md Section 3.4 */}
      {viewMode === 'list' && (
        <div className="bg-white border rounded-lg p-6">
          <h3 className="text-base font-mono mb-4">{t('topology.relations')}</h3>

          {relations.length === 0 ? (
            <p className="text-sm text-gray-400">{t('topology.noRelationsDefined')}</p>
          ) : (
            <div className="space-y-2">
              {relations.map((relation) => {
                const sourceCell = cells.find((c) => c.cellIdentifier === relation.sourceCellIdentifier)
                const targetCell = cells.find((c) => c.cellIdentifier === relation.targetCellIdentifier)
                return (
                  <div
                    key={relation.relationshipIdentifier}
                    onClick={() => setSelectedRelationId(relation.relationshipIdentifier)}
                    className={`border rounded p-3 cursor-pointer ${
                      selectedRelationId === relation.relationshipIdentifier ? 'border-gray-600 bg-gray-50' : 'border-gray-200'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-mono">{sourceCell?.cellName || relation.sourceCellIdentifier}</span>
                      <span className="text-xs text-gray-500">—</span>
                      <span className="text-sm font-mono">{targetCell?.cellName || relation.targetCellIdentifier}</span>
                      <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
                        {getRelationTypeLabel(relation.relationshipType)}
                      </span>
                    </div>
                    {relation.relationshipDescription && (
                      <p className="text-xs text-gray-600 mt-1">{relation.relationshipDescription}</p>
                    )}
                  </div>
                )
              })}
            </div>
          )}
        </div>
      )}

      {/* Relationship Legend - RT_FE_REQ_FROZEN.md Section 3.4 */}
      <div className="bg-white border rounded-lg p-6">
        <h3 className="text-base font-mono mb-4">{t('topology.relationshipLegend')}</h3>
        <div className="space-y-3">
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-400" />
            <span className="font-mono text-xs">{t('topology.dependency')}</span>
            <span className="text-gray-600 text-xs">{t('topology.dependencyDescription')}</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-400 border-t-2 border-dashed" />
            <span className="font-mono text-xs">{t('topology.reference')}</span>
            <span className="text-gray-600 text-xs">{t('topology.referenceDescription')}</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-600" />
            <span className="font-mono text-xs">{t('topology.inputOutput')}</span>
            <span className="text-gray-600 text-xs">{t('topology.inputOutputDescription')}</span>
          </div>
        </div>
      </div>
    </div>
  )
}
