"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"
import { Separator } from "@/components/ui/separator"
import { Plus, Trash2, AlertCircle } from "lucide-react"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

interface Cell {
  id: string
  responsibility: string
  boundary: string
  roleConstraints: string
  state: "defined" | "frozen" | "historical"
}

interface CellManagerProps {
  isFrozen: boolean
}

export function CellManager({ isFrozen }: CellManagerProps) {
  const [cells, setCells] = useState<Cell[]>([])
  const [showCreateDialog, setShowCreateDialog] = useState(false)
  const [editingCell, setEditingCell] = useState<Cell | null>(null)
  const [newCell, setNewCell] = useState<Partial<Cell>>({
    responsibility: "",
    boundary: "",
    roleConstraints: "",
    state: "defined",
  })

  const handleCreateCell = () => {
    if (newCell.responsibility && newCell.boundary) {
      const cell: Cell = {
        id: `cell-${Date.now()}`,
        responsibility: newCell.responsibility,
        boundary: newCell.boundary,
        roleConstraints: newCell.roleConstraints || "",
        state: "defined",
      }
      setCells([...cells, cell])
      setNewCell({ responsibility: "", boundary: "", roleConstraints: "", state: "defined" })
      setShowCreateDialog(false)
    }
  }

  const handleDeleteCell = (id: string) => {
    setCells(cells.filter((cell) => cell.id !== id))
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Cell Management</h2>
          <p className="text-sm text-muted-foreground mt-1">Define minimum responsibility units and their boundaries</p>
        </div>
        {!isFrozen && (
          <Button onClick={() => setShowCreateDialog(true)} className="gap-2">
            <Plus className="h-4 w-4" />
            New Cell
          </Button>
        )}
      </div>

      <Card className="border-dashed">
        <CardContent className="pt-6">
          <div className="flex items-start gap-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <div className="space-y-1 text-xs leading-relaxed">
              <p className="font-medium">Cell Design Constraints (DESIGN-TIME ONLY):</p>
              <ul className="list-disc list-inside space-y-1 ml-2">
                <li>Cell is a responsibility declaration, NOT an executor</li>
                <li>Cell does NOT bind to AI, humans, or agents</li>
                <li>Cell does NOT contain execution logic</li>
                <li>Cell does NOT imply "who does the work"</li>
                <li>Role constraints define allowed/prohibited behaviors only</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>

      {cells.length === 0 ? (
        <Card>
          <CardContent className="py-12 text-center text-muted-foreground">
            <Box className="h-12 w-12 mx-auto mb-4 opacity-20" />
            <p>No cells defined yet</p>
            <p className="text-xs mt-1">Create your first responsibility unit to begin</p>
          </CardContent>
        </Card>
      ) : (
        <div className="grid gap-4">
          {cells.map((cell) => (
            <Card key={cell.id}>
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <CardTitle className="text-base font-mono">{cell.id}</CardTitle>
                      <Badge variant="outline" className="text-xs font-mono">
                        {cell.state}
                      </Badge>
                    </div>
                    <CardDescription className="text-xs font-mono">Responsibility Declaration</CardDescription>
                  </div>
                  {!isFrozen && (
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => handleDeleteCell(cell.id)}
                      className="text-destructive hover:text-destructive"
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  )}
                </div>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-2">
                  <Label className="text-xs font-mono text-muted-foreground">Responsibility Description</Label>
                  <p className="text-sm leading-relaxed">{cell.responsibility}</p>
                </div>

                <Separator />

                <div className="space-y-2">
                  <Label className="text-xs font-mono text-muted-foreground">Responsibility Boundary</Label>
                  <p className="text-sm leading-relaxed">{cell.boundary}</p>
                </div>

                {cell.roleConstraints && (
                  <>
                    <Separator />
                    <div className="space-y-2">
                      <Label className="text-xs font-mono text-muted-foreground">Attached Role Constraints</Label>
                      <p className="text-sm leading-relaxed text-muted-foreground">{cell.roleConstraints}</p>
                    </div>
                  </>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      )}

      <Dialog open={showCreateDialog} onOpenChange={setShowCreateDialog}>
        <DialogContent className="max-w-2xl">
          <DialogHeader>
            <DialogTitle className="font-mono">Create New Cell</DialogTitle>
            <DialogDescription>Define a minimum responsibility unit with explicit boundaries</DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label htmlFor="responsibility" className="font-mono text-xs">
                Responsibility Description (Required)
              </Label>
              <Textarea
                id="responsibility"
                value={newCell.responsibility}
                onChange={(e) => setNewCell({ ...newCell, responsibility: e.target.value })}
                placeholder="What is this cell responsible for?"
                className="min-h-24 font-mono text-sm"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="boundary" className="font-mono text-xs">
                Responsibility Boundary (Required)
              </Label>
              <Textarea
                id="boundary"
                value={newCell.boundary}
                onChange={(e) => setNewCell({ ...newCell, boundary: e.target.value })}
                placeholder="What are the explicit boundaries of this responsibility?"
                className="min-h-24 font-mono text-sm"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="role-constraints" className="font-mono text-xs">
                Attached Role Constraints (Optional)
              </Label>
              <Textarea
                id="role-constraints"
                value={newCell.roleConstraints}
                onChange={(e) => setNewCell({ ...newCell, roleConstraints: e.target.value })}
                placeholder="Define allowed/prohibited behaviors..."
                className="min-h-20 font-mono text-sm"
              />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setShowCreateDialog(false)}>
              Cancel
            </Button>
            <Button onClick={handleCreateCell} disabled={!newCell.responsibility || !newCell.boundary}>
              Create Cell
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}

function Box({ className }: { className?: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className={className}
    >
      <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
      <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
      <line x1="12" y1="22.08" x2="12" y2="12" />
    </svg>
  )
}
