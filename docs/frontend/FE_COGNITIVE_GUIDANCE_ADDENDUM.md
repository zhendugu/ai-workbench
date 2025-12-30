FILE: FE_COGNITIVE_GUIDANCE_ADDENDUM.md
TITLE: Frontend Cognitive Guidance Addendum (Implementation Addendum)
VERSION: FE-ADDENDUM-2
STATUS: DRAFT (PENDING HUMAN CONFIRMATION)
SCOPE: Human-facing Read-Only Cognitive Interface
AUTHORITY: FE-REQ-FROZEN-1 + GCD_v2 + frozen design docs
NON-GOALS: UI visuals, page layout, code, backend changes, capability expansion

============================================================
0. PURPOSE
============================================================

This addendum exists because the current frontend, while compliant (read-only, non-executable),
is not cognitively usable for the human operator.

Goal:
- Convert "confusing / unusable" into testable cognitive requirements.
- Preserve all frozen prohibitions.
- Provide a deterministic reading path that matches how a human thinks and verifies.

This addendum introduces:
- Cognitive path requirements (how a human should traverse information).
- Sense-making requirements (what must be obvious within 30 seconds).
- Minimum affordances that increase comprehension WITHOUT increasing capability.

============================================================
1. DEFINITIONS (COGNITIVE, NOT TECHNICAL)
============================================================

"Read-only cognitive interface" means:
- The human is navigating knowledge, not triggering actions.
- The interface must feel like a map + evidence index, not a control console.

"Cognitive affordance" means:
- A UI feature that reduces confusion without implying execution or recommendation.
Examples: labels, context headers, explicit "You are viewing" text, bounded summaries, breadcrumb.

"Layer" means:
- A mental stratum that answers one question category:
  L1 Identity, L2 Structure, L3 History, L4 Judgment, L5 Evidence.

"Operator question" means:
- A question the human must be able to answer by reading the UI, not by guessing.

============================================================
2. NON-NEGOTIABLE CONSTRAINTS (RE-ASSERTED)
============================================================

The frontend MUST NOT:
- Execute, trigger, run, approve, apply, create, modify, delete.
- Call AI APIs, spawn agents, perform autonomous tasks.
- Recommend, score, predict, rank by intelligence, highlight "next step".
- Suggest progress, health, risk, success probability, or "system is working".
- Use color coding (red/yellow/green), progress bars, urgency cues, countdowns.
- Provide default decisions or preselected choices.

The frontend MAY:
- Provide navigation, filtering, searching, sorting (non-intelligent only).
- Provide reading order guides and context labels.
- Provide explicit "NOT RUNNING" disclaimers as text.

============================================================
3. TOP-LEVEL COGNITIVE CONTRACT (30-SECOND TEST)
============================================================

Within 30 seconds after opening the interface, the human MUST be able to answer:

Q-30-1: What am I looking at (Company identity)?
Q-30-2: Which layer am I in right now (Structure, History, Judgment, Evidence)?
Q-30-3: Is the system executing anything automatically? (must be clearly "NO")
Q-30-4: Where can I find: (a) responsibilities (Cell), (b) decisions, (c) evidence.

Failure condition:
- If the human describes the interface as "random text", "no idea where to start",
  "feels like a dashboard", or "no operational meaning", then the interface fails.

============================================================
4. REQUIRED INFORMATION LAYERS (MUST BE SEPARATED)
============================================================

The interface MUST separate content into the following layers and NEVER mix them silently:

L1: Company Context (Identity Layer)
- Company stable id, name, short description
- Current phase label (read-only)
- Frozen design refs
- Global disclaimer: "Read-only cognitive view; no execution; no recommendations"

L2: Structure Layer
- Cell list / network view (responsibility units)
- Role as cell-attached constraints only
- Workflow declaration as structure reference only (no implied sequence)

L3: History Layer
- Work Orders (documents)
- Execution archives (runs)
- Decisions (documents)
- Phase closure docs

L4: Judgment Layer
- Human decision points index
- Each judgment point page links to its evidence set and decision records
- No default selection, no "recommended answer"

L5: Evidence Layer
- Evidence packs and referenced artifacts
- Hash manifests and traceability links
- Evidence is presented as "source material", not "score"

Mandatory rule:
- Each screen MUST declare which layer it belongs to in plain text.
Example header: "YOU ARE VIEWING: STRUCTURE LAYER (READ-ONLY)"

============================================================
5. COGNITIVE PATHS (READING FLOWS, NOT EXECUTION FLOWS)
============================================================

The interface MUST provide at least these 3 reading paths as explicit navigation presets.
These are not actions; they are curated reading orders.

PATH A: "Understand the Company"
- Start: Company Context
- Then: Structure summary (cells count, roles count, task forces count)
- Then: Methodology declarations (read-only)
- Then: What is NOT claimed (disclaimers)

PATH B: "Inspect a Responsibility"
- Start: Cell index
- Select one Cell
- View: responsibility + boundary + attached Role constraints
- View: linked artifacts (work orders, decisions, evidence) that reference the cell
- View: traceability entries for those artifacts

PATH C: "Verify a Decision"
- Start: Decisions index
- Select a decision document
- View: decision text + metadata
- View: evidence references
- Jump: evidence artifacts
- Jump: traceability index entries for that decision

Hard rule:
- These paths MUST NOT be presented as "workflow" or "next steps".
They are only "reading guides".

============================================================
6. MINIMUM AFFORDANCES FOR COMPREHENSION (REQUIRED)
============================================================

6.1 "Where am I" markers
- Breadcrumb or location header, always visible:
  Company > Layer > Entity Type > Entity ID
- Must be plain text, no "progress" implication.

6.2 "What does this mean" micro-glossary
- For each layer, a short 2-4 lines explanation:
  "Structure Layer shows responsibility declarations (Cells). Nothing is running."
- Must not be educational essay; must be short.

6.3 Stable identifiers always visible
- Every entity view MUST show stable id prominently.
- This is to support audit and cross-referencing.

6.4 Cross-links must be explicit and typed
- Any link must indicate its relation type:
  "Referenced by Work Order", "Evidence for Decision", "Declared in Workflow"
- No "related items" recommendations.

6.5 Non-intelligent search and filters
Allowed:
- Search by id substring, filename substring
- Filter by entity type, date range, phase label
- Sort by name, time, id (deterministic)
Forbidden:
- "smart search", "suggested results", "auto tags"

============================================================
7. MAPPING REQUIREMENTS (FACT OBJECTS TO UI SECTIONS)
============================================================

The frontend MUST map these declarative objects into first-class reading anchors:

- COMPANY_DECLARATION.md => L1 Company Context primary source
- METHODOLOGY_DECLARATION.md => L1/L2 Methodology tab (read-only)
- WORKFLOW_DECLARATION.md => L2 Workflow reference view
- FE_FACT_ENTITY_MAP.md => L1 "What exists" index
- FE_FACT_HUMAN_DECISION_POINTS.md => L4 Judgment index
- FE_FACT_AUDIT_VISIBILITY.md => L5 Evidence entry guide
- TRACEABILITY_INDEX_R0.md => L5 Traceability navigator
- FE_SEMANTIC_CONTRACT.md + SEMANTIC_OBJECT_INDEX.md => L1 "Contract" and "Index"

Hard rule:
- If a file is missing, UI must display "MISSING SOURCE" with exact filename,
  not silently hide the category.

============================================================
8. "NO EXECUTION" TRUST SIGNALS (TEXT ONLY)
============================================================

Because the interface must not feel like a control panel, it MUST implement:

- A persistent, visible banner (text only):
  "READ-ONLY VIEW. NO EXECUTION. NO RECOMMENDATIONS. NO AI CALLS."
- Each layer page repeats a short layer-specific statement:
  "STRUCTURE DECLARATIONS ONLY. NOTHING IS RUNNING."

Forbidden:
- Security badges, trust scores, compliance checkmarks, green indicators.

============================================================
9. OPERATOR USABILITY ACCEPTANCE TESTS (PASS/FAIL)
============================================================

All tests are human-perception tests; they must be pass/fail.

T-1 30-second orientation
- Open UI
- Can answer Q-30-1 to Q-30-4 without external docs
PASS if yes, FAIL otherwise.

T-2 Responsibility comprehension
- Pick a random cell
- Can state: responsibility + boundary + what it is NOT
PASS if yes.

T-3 Decision verification
- Pick a decision doc
- Can reach its evidence pack and traceability index within 3 clicks
PASS if yes.

T-4 No "system running" illusion
- Human must report: "I do not feel the system is doing things by itself."
PASS if yes.

T-5 No recommendation illusion
- Human must report: "I do not feel the UI is nudging me to choose anything."
PASS if yes.

============================================================
10. COMMON FAILURE MODES (MUST BE PREVENTED)
============================================================

FM-1: "Flat text dump"
- Everything is on one page with no reading path.
Prevent by mandatory layers + paths + location markers.

FM-2: "Looks like a dashboard"
- KPIs, cards, highlights, progress feelings.
Prevent by banning dashboards and using text-only disclaimers.

FM-3: "Feels like a control panel"
- Buttons, toggles, run-like icons, action verbs.
Prevent by verb-free labels and removing any operation affordance.

FM-4: "Ambiguous entity meaning"
- Role looks like person/agent; Cell looks like actor.
Prevent by enforcing Role as cell-attached constraint only,
and language rules (no personification).

============================================================
11. LANGUAGE RULES (TEXT IN UI)
============================================================

Always use:
- "View", "Inspect", "Browse", "Read", "Reference"
Never use:
- "Run", "Execute", "Start", "Apply", "Fix", "Recommend", "Optimize"

Cell text:
- "Responsibility", "Boundary", "Constraints"
Avoid:
- "Owner", "Assignee", "Agent", "Worker", "Active"

Workflow text:
- "Declared relationship"
Avoid:
- "Next", "Step", "Pipeline", "Flow", "Current node"

============================================================
12. IMPLEMENTATION NOTES (NON-BINDING, NO TECH)
============================================================

This addendum does not require backend changes.
It requires the frontend to:
- Build clear information architecture from existing files.
- Provide deterministic navigation and reading presets.
- Provide explicit layer declarations and typed cross-links.

END OF FILE

