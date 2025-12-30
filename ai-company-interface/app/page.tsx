"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { AlertCircle, FileText, Box, Layers, Settings, Eye } from "lucide-react"
import { CompanyMetadata } from "@/components/company-metadata"
import { CellManager } from "@/components/cell-manager"
import { TopologyCanvas } from "@/components/topology-canvas"
import { MethodologySelector } from "@/components/methodology-selector"
import { TemplateLibrary } from "@/components/template-library"
import { FreezeConfirmation } from "@/components/freeze-confirmation"

export default function DesignTimePage() {
  const [activeTab, setActiveTab] = useState("company")
  const [isFrozen, setIsFrozen] = useState(false)
  const [showFreezeDialog, setShowFreezeDialog] = useState(false)

  return (
    <div className="min-h-screen bg-background">
      {/* Global Design-Time Indicator */}
      <div className="sticky top-0 z-50 border-b bg-card/95 backdrop-blur supports-[backdrop-filter]:bg-card/60">
        <div className="container mx-auto px-4 py-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2">
                <Box className="h-5 w-5 text-primary" />
                <span className="text-lg font-mono font-semibold">AI Virtual Company</span>
              </div>
              <Badge variant="outline" className="font-mono text-xs">
                DESIGN-TIME
              </Badge>
            </div>
            <div className="flex items-center gap-2">
              <div className="text-sm text-muted-foreground font-mono">{isFrozen ? "FROZEN (READ-ONLY)" : "DRAFT"}</div>
              {!isFrozen && (
                <Button variant="default" size="sm" onClick={() => setShowFreezeDialog(true)} className="font-mono">
                  Freeze Design
                </Button>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Information Banner */}
      <div className="border-b bg-muted/30">
        <div className="container mx-auto px-4 py-3">
          <div className="flex items-start gap-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4 mt-0.5 flex-shrink-0" />
            <div className="space-y-1">
              <p className="font-medium">You are in DESIGN-TIME mode</p>
              <p className="text-xs leading-relaxed">
                All content here is structural declaration. No execution, automation, or AI behavior occurs in this
                interface. This is for constructing company structures from zero, not running them.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 py-8">
        <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
          <TabsList className="grid w-full grid-cols-5 lg:w-auto lg:inline-grid font-mono">
            <TabsTrigger value="company" className="gap-2">
              <FileText className="h-4 w-4" />
              Company
            </TabsTrigger>
            <TabsTrigger value="cells" className="gap-2">
              <Box className="h-4 w-4" />
              Cells
            </TabsTrigger>
            <TabsTrigger value="topology" className="gap-2">
              <Layers className="h-4 w-4" />
              Topology
            </TabsTrigger>
            <TabsTrigger value="methodology" className="gap-2">
              <Settings className="h-4 w-4" />
              Methodology
            </TabsTrigger>
            <TabsTrigger value="templates" className="gap-2">
              <Eye className="h-4 w-4" />
              Templates
            </TabsTrigger>
          </TabsList>

          <TabsContent value="company" className="space-y-6">
            <CompanyMetadata isFrozen={isFrozen} />
          </TabsContent>

          <TabsContent value="cells" className="space-y-6">
            <CellManager isFrozen={isFrozen} />
          </TabsContent>

          <TabsContent value="topology" className="space-y-6">
            <TopologyCanvas isFrozen={isFrozen} />
          </TabsContent>

          <TabsContent value="methodology" className="space-y-6">
            <MethodologySelector isFrozen={isFrozen} />
          </TabsContent>

          <TabsContent value="templates" className="space-y-6">
            <TemplateLibrary isFrozen={isFrozen} />
          </TabsContent>
        </Tabs>
      </div>

      {showFreezeDialog && (
        <FreezeConfirmation
          onConfirm={() => {
            setIsFrozen(true)
            setShowFreezeDialog(false)
          }}
          onCancel={() => setShowFreezeDialog(false)}
        />
      )}
    </div>
  )
}
