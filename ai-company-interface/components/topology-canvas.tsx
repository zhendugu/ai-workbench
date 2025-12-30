"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { AlertCircle } from "lucide-react"

interface TopologyCanvasProps {
  isFrozen: boolean
}

export function TopologyCanvas({ isFrozen }: TopologyCanvasProps) {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Declarative Topology</h2>
          <p className="text-sm text-muted-foreground mt-1">
            Visual representation of structural relationships between cells
          </p>
        </div>
        <Badge variant="outline" className="font-mono text-xs">
          NOT EXECUTABLE
        </Badge>
      </div>

      <Card className="border-dashed">
        <CardContent className="pt-6">
          <div className="flex items-start gap-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <div className="space-y-1 text-xs leading-relaxed">
              <p className="font-medium">Topology Construction Rules:</p>
              <ul className="list-disc list-inside space-y-1 ml-2">
                <li>This is STRUCTURE DECLARATION, not a workflow engine</li>
                <li>Connections represent semantic relationships, not execution order</li>
                <li>No "current node" or "next step" concept exists here</li>
                <li>No execution direction, progress, or path recommendations</li>
                <li>Relationship types: Dependency / Reference / Sequential Declaration</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card className="min-h-[500px]">
        <CardHeader>
          <CardTitle className="text-lg font-mono">Canvas</CardTitle>
          <CardDescription>Place cells as nodes and connect them with relationship lines</CardDescription>
        </CardHeader>
        <CardContent className="h-[500px] flex items-center justify-center text-muted-foreground">
          <div className="text-center space-y-2">
            <div className="text-sm">Canvas implementation placeholder</div>
            <div className="text-xs">Would contain: Node placement, relationship line drawing, type labeling</div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base font-mono">Relationship Legend</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-border" />
            <span className="font-mono text-xs">Dependency</span>
            <span className="text-muted-foreground text-xs">Cell A depends on Cell B existing</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-border border-t-2 border-dashed" />
            <span className="font-mono text-xs">Reference</span>
            <span className="text-muted-foreground text-xs">Cell A references Cell B output</span>
          </div>
          <div className="flex items-center gap-3 text-sm">
            <div className="w-16 h-0.5 bg-muted-foreground" />
            <span className="font-mono text-xs">Sequential</span>
            <span className="text-muted-foreground text-xs">Structural sequence declaration</span>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
