// L3: Topology Layer - Declarative Topology
// Authority: DT_FE_REQ_DRAFT.md Section 2.4
// WO-FE-TOPOLOGY-CANVAS-001: Mode A (Graphical Canvas) implementation

import { useState, useRef, useCallback, useEffect } from 'react'
import type { Cell, Relation, RelationType } from '../../types'

interface TopologyCanvasProps {
  cells: Cell[]
  relations: Relation[]
  onRelationsChange: (relations: Relation[]) => void
  isFrozen: boolean
}

// Node position state (layout only, no semantic meaning)
interface NodePosition {
  x: number
  y: number
}

export function TopologyCanvas({ cells, relations, onRelationsChange, isFrozen }: TopologyCanvasProps) {
  const [viewMode, setViewMode] = useState<'canvas' | 'list'>('canvas')
  const [showCreateDialog, setShowCreateDialog] = useState(false)
  const [editingRelation, setEditingRelation] = useState<Relation | null>(null)
  const [newRelation, setNewRelation] = useState<Partial<Relation>>({
    sourceCellId: '',
    targetCellId: '',
    type: 'dependency',
    description: '',
  })
  
  // Canvas state
  const [nodePositions, setNodePositions] = useState<Record<string, NodePosition>>({})
  const [draggingNodeId, setDraggingNodeId] = useState<string | null>(null)
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 })
  const svgRef = useRef<SVGSVGElement>(null)

  const handleCreateRelation = () => {
    if (!newRelation.sourceCellId || !newRelation.targetCellId || !newRelation.type) return

    const relation: Relation = {
      id: `REL-${Date.now()}`,
      sourceCellId: newRelation.sourceCellId,
      targetCellId: newRelation.targetCellId,
      type: newRelation.type as RelationType,
      description: newRelation.description,
    }

    onRelationsChange([...relations, relation])
    setNewRelation({ sourceCellId: '', targetCellId: '', type: 'dependency', description: '' })
    setShowCreateDialog(false)
  }

  const handleDeleteRelation = (id: string) => {
    if (confirm('Are you sure you want to delete this relation?')) {
      onRelationsChange(relations.filter((r) => r.id !== id))
    }
  }

  // Initialize node positions (geometric layout only)
  useEffect(() => {
    if (cells.length > 0 && Object.keys(nodePositions).length === 0) {
      const positions: Record<string, NodePosition> = {}
      const radius = 200
      const centerX = 400
      const centerY = 300
      
      cells.forEach((cell, index) => {
        const angle = (2 * Math.PI * index) / cells.length
        positions[cell.id] = {
          x: centerX + radius * Math.cos(angle),
          y: centerY + radius * Math.sin(angle),
        }
      })
      
      setNodePositions(positions)
    }
  }, [cells, nodePositions])

  // Handle node drag start
  const handleNodeMouseDown = useCallback((e: React.MouseEvent<SVGElement>, nodeId: string) => {
    if (isFrozen) return
    e.preventDefault()
    const nodePos = nodePositions[nodeId]
    if (!nodePos || !svgRef.current) return
    
    const svgRect = svgRef.current.getBoundingClientRect()
    setDraggingNodeId(nodeId)
    setDragOffset({
      x: e.clientX - svgRect.left - nodePos.x,
      y: e.clientY - svgRect.top - nodePos.y,
    })
  }, [nodePositions, isFrozen])

  // Handle node drag
  const handleNodeMouseMove = useCallback((e: React.MouseEvent<SVGElement>) => {
    if (!draggingNodeId || !svgRef.current) return
    e.preventDefault()
    
    const svgRect = svgRef.current.getBoundingClientRect()
    const newX = e.clientX - svgRect.left - dragOffset.x
    const newY = e.clientY - svgRect.top - dragOffset.y
    
    setNodePositions((prev) => ({
      ...prev,
      [draggingNodeId]: { x: newX, y: newY },
    }))
  }, [draggingNodeId, dragOffset])

  // Handle node drag end
  const handleNodeMouseUp = useCallback(() => {
    setDraggingNodeId(null)
  }, [])

  // Handle node click (open Cell detail - placeholder, would navigate to Cell view)
  const handleNodeClick = useCallback((cellId: string) => {
    // In real implementation, this would navigate to Cell detail view
    // For now, just log
    console.log('Cell clicked:', cellId)
  }, [])

  // Handle edge click (edit relation)
  const handleEdgeClick = useCallback((relation: Relation) => {
    if (isFrozen) return
    setEditingRelation(relation)
    setNewRelation({
      sourceCellId: relation.sourceCellId,
      targetCellId: relation.targetCellId,
      type: relation.type,
      description: relation.description || '',
    })
  }, [isFrozen])

  // Update relation
  const handleUpdateRelation = () => {
    if (!editingRelation || !newRelation.sourceCellId || !newRelation.targetCellId || !newRelation.type) return

    const updated = relations.map((r) =>
      r.id === editingRelation.id
        ? {
            ...r,
            sourceCellId: newRelation.sourceCellId!,
            targetCellId: newRelation.targetCellId!,
            type: newRelation.type as RelationType,
            description: newRelation.description,
          }
        : r
    )

    onRelationsChange(updated)
    setEditingRelation(null)
    setNewRelation({ sourceCellId: '', targetCellId: '', type: 'dependency', description: '' })
  }

  // Get relation type label (noun form)
  const getRelationTypeLabel = (type: RelationType): string => {
    switch (type) {
      case 'dependency':
        return 'Dependency'
      case 'reference':
        return 'Reference'
      case 'input-output':
        return 'Input-Output'
      default:
        return type
    }
  }

  // Get relation line style
  const getRelationLineStyle = (type: RelationType): { stroke: string; strokeDasharray?: string } => {
    switch (type) {
      case 'dependency':
        return { stroke: '#666' }
      case 'reference':
        return { stroke: '#666', strokeDasharray: '5,5' }
      case 'input-output':
        return { stroke: '#333' }
      default:
        return { stroke: '#666' }
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">Declarative Topology</h2>
          <p className="text-sm text-gray-600 mt-1">
            Visual representation of structural relationships between cells
          </p>
        </div>
        <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
          NOT EXECUTABLE
        </span>
      </div>

      {/* Topology Construction Rules - DT_FE_REQ_DRAFT.md Section 2.4 */}
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <div className="text-sm text-gray-700">
          <p className="font-medium mb-2">Topology Construction Rules:</p>
          <ul className="list-disc list-inside space-y-1 text-xs">
            <li>This is STRUCTURE DECLARATION, not a workflow engine</li>
            <li>Connections represent semantic relationships, not execution order</li>
            <li>No "current node" or "next step" concept exists here</li>
            <li>No execution direction, progress, or path recommendations</li>
            <li>Relationship types: Dependency / Reference / Sequential Declaration</li>
          </ul>
        </div>
      </div>

      {/* View Mode Toggle - WO-FE-TOPOLOGY-CANVAS-001 */}
      <div className="bg-white border rounded-lg p-4">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-base font-mono">View Mode</h3>
          <div className="flex gap-2">
            <button
              onClick={() => setViewMode('canvas')}
              className={`px-4 py-2 text-sm border rounded ${
                viewMode === 'canvas' ? 'bg-blue-100 border-blue-600' : 'bg-gray-50'
              }`}
            >
              Topology Canvas
            </button>
            <button
              onClick={() => setViewMode('list')}
              className={`px-4 py-2 text-sm border rounded ${
                viewMode === 'list' ? 'bg-blue-100 border-blue-600' : 'bg-gray-50'
              }`}
            >
              Relation List
            </button>
          </div>
        </div>
      </div>

      {/* Mode A: Topology Canvas - WO-FE-TOPOLOGY-CANVAS-001 */}
      {viewMode === 'canvas' && (
        <div className="bg-white border rounded-lg p-6">
          {/* UI Copy Requirement - WO-FE-TOPOLOGY-CANVAS-001 */}
          <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded">
            <p className="text-sm text-gray-700">
              <strong>This is a declarative topology view.</strong>
              <br />
              Relationships represent structural dependencies, not execution order or runtime flow.
            </p>
          </div>

          {cells.length === 0 ? (
            <div className="h-[500px] flex items-center justify-center text-gray-400 border-2 border-dashed rounded">
              <div className="text-center">
                <p className="text-sm">No cells defined</p>
                <p className="text-xs mt-1">Create cells first to visualize topology</p>
              </div>
            </div>
          ) : (
            <div className="relative">
              <svg
                ref={svgRef}
                width="100%"
                height="600"
                className="border rounded bg-gray-50"
                onMouseMove={handleNodeMouseMove}
                onMouseUp={handleNodeMouseUp}
                onMouseLeave={handleNodeMouseUp}
              >
                {/* Render edges (relations) */}
                {relations.map((relation) => {
                  const sourcePos = nodePositions[relation.sourceCellId]
                  const targetPos = nodePositions[relation.targetCellId]
                  
                  if (!sourcePos || !targetPos) return null

                  const lineStyle = getRelationLineStyle(relation.type)
                  const midX = (sourcePos.x + targetPos.x) / 2
                  const midY = (sourcePos.y + targetPos.y) / 2

                  return (
                    <g key={relation.id}>
                      {/* Edge line - bidirectional, no arrow */}
                      <line
                        x1={sourcePos.x}
                        y1={sourcePos.y}
                        x2={targetPos.x}
                        y2={targetPos.y}
                        stroke={lineStyle.stroke}
                        strokeWidth={2}
                        strokeDasharray={lineStyle.strokeDasharray}
                        style={{ cursor: isFrozen ? 'default' : 'pointer' }}
                        onClick={() => handleEdgeClick(relation)}
                      />
                      {/* Relation type label (noun form) */}
                      <g
                        transform={`translate(${midX}, ${midY})`}
                        style={{ cursor: isFrozen ? 'default' : 'pointer' }}
                        onClick={() => handleEdgeClick(relation)}
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
                          {getRelationTypeLabel(relation.type)}
                        </text>
                      </g>
                    </g>
                  )
                })}

                {/* Render nodes (cells) */}
                {cells.map((cell) => {
                  const pos = nodePositions[cell.id]
                  if (!pos) return null

                  return (
                    <g key={cell.id}>
                      {/* Node circle */}
                      <circle
                        cx={pos.x}
                        cy={pos.y}
                        r="40"
                        fill="white"
                        stroke="#333"
                        strokeWidth="2"
                        style={{
                          cursor: isFrozen ? 'default' : 'move',
                        }}
                        onMouseDown={(e) => handleNodeMouseDown(e, cell.id)}
                        onClick={() => handleNodeClick(cell.id)}
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
                        {cell.name}
                      </text>
                    </g>
                  )
                })}
              </svg>

              {/* Canvas Toolbar - WO-FE-TOPOLOGY-CANVAS-001 */}
              {!isFrozen && (
                <div className="mt-4 flex gap-2">
                  <button
                    onClick={() => setShowCreateDialog(true)}
                    className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm"
                  >
                    Add Relation
                  </button>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Mode B: Relation List - DT_FE_REQ_DRAFT.md Section 2.4 (方式 B) */}
      {viewMode === 'list' && (
        <div className="bg-white border rounded-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-base font-mono">Relations</h3>
          {!isFrozen && (
            <button
              onClick={() => setShowCreateDialog(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm"
            >
              Create Relation
            </button>
          )}
        </div>

        {relations.length === 0 ? (
          <p className="text-sm text-gray-400">No relations defined</p>
        ) : (
          <div className="space-y-2">
            {relations.map((relation) => {
              const sourceCell = cells.find((c) => c.id === relation.sourceCellId)
              const targetCell = cells.find((c) => c.id === relation.targetCellId)
              return (
                <div key={relation.id} className="border rounded p-3 flex items-center justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-mono">{sourceCell?.name || relation.sourceCellId}</span>
                      <span className="text-xs text-gray-500">→</span>
                      <span className="text-sm font-mono">{targetCell?.name || relation.targetCellId}</span>
                      <span className="px-2 py-1 text-xs font-mono border rounded bg-gray-100">
                        {relation.type}
                      </span>
                    </div>
                    {relation.description && (
                      <p className="text-xs text-gray-600 mt-1">{relation.description}</p>
                    )}
                  </div>
                  {!isFrozen && (
                    <button
                      onClick={() => handleDeleteRelation(relation.id)}
                      className="ml-4 px-3 py-1 text-sm text-red-600 border border-red-300 rounded hover:bg-red-50"
                    >
                      Delete
                    </button>
                  )}
                </div>
              )
            })}
          </div>
        )}
        </div>
      )}

      {/* Relationship Legend - DT_FE_REQ_DRAFT.md Section 2.4 */}
      <div className="bg-white border rounded-lg p-6">
        <h3 className="text-base font-mono mb-4">Relationship Legend</h3>
        <div className="space-y-3">
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-400" />
            <span className="font-mono text-xs">Dependency</span>
            <span className="text-gray-600 text-xs">Cell A depends on Cell B existing</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-400 border-t-2 border-dashed" />
            <span className="font-mono text-xs">Reference</span>
            <span className="text-gray-600 text-xs">Cell A references Cell B output</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-gray-600" />
            <span className="font-mono text-xs">Input-Output</span>
            <span className="text-gray-600 text-xs">Cell A output is Cell B input</span>
          </div>
        </div>
      </div>

      {/* Create Relation Dialog */}
      {(showCreateDialog || editingRelation) && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-2xl w-full mx-4">
            <h3 className="text-lg font-mono mb-4">
              {editingRelation ? 'Edit Relation' : 'Create Relation'}
            </h3>

            <div className="space-y-4">
              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">Source Cell</label>
                <select
                  value={newRelation.sourceCellId || ''}
                  onChange={(e) => setNewRelation({ ...newRelation, sourceCellId: e.target.value })}
                  className="w-full px-3 py-2 border rounded"
                >
                  <option value="">Select source cell</option>
                  {cells.map((cell) => (
                    <option key={cell.id} value={cell.id}>
                      {cell.name} ({cell.id})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">Target Cell</label>
                <select
                  value={newRelation.targetCellId || ''}
                  onChange={(e) => setNewRelation({ ...newRelation, targetCellId: e.target.value })}
                  className="w-full px-3 py-2 border rounded"
                >
                  <option value="">Select target cell</option>
                  {cells
                    .filter((cell) => cell.id !== newRelation.sourceCellId)
                    .map((cell) => (
                      <option key={cell.id} value={cell.id}>
                        {cell.name} ({cell.id})
                      </option>
                    ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">Relation Type</label>
                <select
                  value={newRelation.type || 'dependency'}
                  onChange={(e) => setNewRelation({ ...newRelation, type: e.target.value as RelationType })}
                  className="w-full px-3 py-2 border rounded"
                >
                  <option value="dependency">Dependency</option>
                  <option value="reference">Reference</option>
                  <option value="input-output">Input-Output</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-mono text-gray-600 mb-1">Description (Optional)</label>
                <textarea
                  value={newRelation.description || ''}
                  onChange={(e) => setNewRelation({ ...newRelation, description: e.target.value })}
                  placeholder="Relation description"
                  className="w-full px-3 py-2 border rounded text-sm min-h-20"
                />
              </div>
            </div>

            <div className="flex gap-2 mt-6">
              <button
                onClick={() => {
                  setShowCreateDialog(false)
                  setEditingRelation(null)
                  setNewRelation({ sourceCellId: '', targetCellId: '', type: 'dependency', description: '' })
                }}
                className="px-4 py-2 border rounded hover:bg-gray-50"
              >
                Cancel
              </button>
              {editingRelation ? (
                <button
                  onClick={handleUpdateRelation}
                  disabled={!newRelation.sourceCellId || !newRelation.targetCellId}
                  className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                >
                  Update Relation
                </button>
              ) : (
                <button
                  onClick={handleCreateRelation}
                  disabled={!newRelation.sourceCellId || !newRelation.targetCellId}
                  className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed"
                >
                  Create Relation
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

