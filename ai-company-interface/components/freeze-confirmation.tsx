"use client"

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { AlertCircle } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"

interface FreezeConfirmationProps {
  onConfirm: () => void
  onCancel: () => void
}

export function FreezeConfirmation({ onConfirm, onCancel }: FreezeConfirmationProps) {
  return (
    <Dialog open onOpenChange={(open) => !open && onCancel()}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle className="font-mono text-xl">Freeze Design Confirmation</DialogTitle>
          <DialogDescription>
            This action will convert your design-time draft into a frozen, read-only structure
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-4 py-4">
          <Card className="border-destructive/50 bg-destructive/5">
            <CardContent className="pt-6">
              <div className="flex items-start gap-2">
                <AlertCircle className="h-5 w-5 text-destructive flex-shrink-0 mt-0.5" />
                <div className="space-y-2 text-sm">
                  <p className="font-semibold text-foreground">Consequences of Freezing:</p>
                  <ul className="list-disc list-inside space-y-1 text-muted-foreground ml-2">
                    <li>All current structure becomes READ-ONLY</li>
                    <li>No further edits, additions, or deletions allowed</li>
                    <li>A stable ID will be generated for Run-Time reference</li>
                    <li>This frozen structure becomes available to Run-Time and Audit interfaces</li>
                    <li>You will need to create a new draft to make further changes</li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="space-y-3">
                <p className="text-sm font-medium">What will be frozen:</p>
                <div className="space-y-2 text-sm text-muted-foreground">
                  <div className="flex justify-between py-2 border-b">
                    <span>Company Metadata</span>
                    <span className="font-mono">1 draft</span>
                  </div>
                  <div className="flex justify-between py-2 border-b">
                    <span>Defined Cells</span>
                    <span className="font-mono">0 cells</span>
                  </div>
                  <div className="flex justify-between py-2 border-b">
                    <span>Topology Relationships</span>
                    <span className="font-mono">0 relationships</span>
                  </div>
                  <div className="flex justify-between py-2">
                    <span>Selected Methodology</span>
                    <span className="font-mono">None</span>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="border-dashed">
            <CardContent className="pt-6">
              <p className="text-sm text-muted-foreground leading-relaxed">
                Please confirm that you understand this is an irreversible action. Once frozen, this design becomes a
                permanent reference structure for the Run-Time system. No AI assistance or automatic optimization will
                occur.
              </p>
            </CardContent>
          </Card>
        </div>

        <DialogFooter className="gap-2">
          <Button variant="outline" onClick={onCancel}>
            Cancel (Keep Editing)
          </Button>
          <Button variant="default" onClick={onConfirm} className="bg-primary">
            Confirm Freeze Design
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
