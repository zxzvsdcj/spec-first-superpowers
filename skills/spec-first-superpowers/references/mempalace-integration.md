# MemPalace Integration Guide

MemPalace is a local-first AI memory system that stores conversation history as verbatim text and retrieves it with semantic search. It is the **sixth core tool** in spec-first-superpowers v5, providing cross-session memory persistence for spec decisions, design rationale, and workflow state.

## Why MemPalace

| Dimension | Value |
|-----------|-------|
| Retrieval quality | 96.6% R@5 on LongMemEval (no API calls required) |
| Privacy | 100% local-first — nothing leaves your machine |
| Cost | Free (MIT license) |
| MCP tools | 29 tools covering palace, knowledge graph, navigation, diary |
| Storage | Verbatim — no summarization, no paraphrasing |

## Installation

```bash
pip install mempalace
mempalace init ~/projects/your-project
```

### Cursor MCP Configuration

Add to Cursor Settings → MCP:

```json
{
  "mcpServers": {
    "mempalace": {
      "command": "python",
      "args": ["-m", "mempalace.mcp_server"]
    }
  }
}
```

### With Custom Palace Path

```json
{
  "mcpServers": {
    "mempalace": {
      "command": "python",
      "args": ["-m", "mempalace.mcp_server", "--palace", "/path/to/palace"]
    }
  }
}
```

## Palace Architecture

```
Palace
├── Wing — a person or project (e.g., wing_myapp)
│   ├── Room — specific topic (e.g., auth-migration, api-design)
│   │   ├── hall_facts — decisions made
│   │   ├── hall_events — sessions, milestones
│   │   ├── hall_discoveries — breakthroughs, insights
│   │   ├── hall_preferences — habits, opinions
│   │   └── hall_advice — recommendations
│   └── Drawer — original stored text (verbatim)
├── Tunnel — cross-wing connections
└── Knowledge Graph — temporal entity-relationship (SQLite)
```

## Five Integration Points

### 1. Session Recovery (G0 Enhancement)

Augments the existing task_plan.md-based recovery with palace context.

```
Session start:
  1. Read task_plan.md + findings.md + progress.md (existing)
  2. mempalace_status → palace overview
  3. mempalace_search("project-name recent decisions") → relevant history
  4. mempalace_diary_read(agent="spec-orchestrator") → last workflow state
  5. mempalace_kg_query("ProjectName") → entity timeline
  6. Merge all sources → comprehensive context recovery
```

### 2. Spec Decision Persistence (at G1)

Records architecture decisions in the Knowledge Graph with temporal tracking.

```
User confirms spec (G1 passed):
  → mempalace_kg_add("ProjectX", "chose_auth", "Clerk", valid_from="2026-04-17")
  → mempalace_add_drawer(wing="ProjectX", room="auth", content=<full spec text>)

Later, spec changes:
  → mempalace_kg_invalidate("ProjectX", "chose_auth", "Clerk", ended="2026-05-01")
  → mempalace_kg_add("ProjectX", "chose_auth", "Auth0", valid_from="2026-05-01")
  → Complete decision timeline preserved
```

### 3. Cross-Project Pattern Discovery

Finds how similar problems were solved in other projects.

```
New project needs "auth" spec:
  → mempalace_search("auth spec decision", limit=5)
  → Returns verbatim specs from historical projects
  → AI references historical patterns (not generating from scratch)
```

Wing/room scoping enables precise queries:
- `mempalace_search("rate limiting", wing="project_api")` — project-specific
- `mempalace_search("rate limiting")` — cross-project discovery

### 4. Agent Diary Audit Trail (at each Gate)

Records workflow phase transitions for traceability.

```
Phase 1 (Spec) complete:
  → mempalace_diary_write(
      agent="spec-orchestrator",
      entry="G1|passed|auth-feature|spec-confirmed|inline-review:2-issues-fixed",
      topic="workflow"
    )

Phase 4 (Implementation) complete:
  → mempalace_diary_write(
      agent="spec-orchestrator",
      entry="G4|passed|auth-feature|tests:42/42|review:no-P0P1",
      topic="workflow"
    )
```

### 5. Knowledge Archive (at G4)

Persists key findings and lessons for future reference.

```
G4 passed:
  → mempalace_add_drawer(
      wing="ProjectX",
      room="auth",
      content="Key findings: [technical insights from implementation]"
    )
  → mempalace_kg_add("ProjectX", "implemented", "auth-feature", valid_from=today)
```

## Tool Reference (Key Tools)

| Category | Tool | When to Use |
|----------|------|-------------|
| **Read** | `mempalace_status` | Session start — palace overview |
| **Read** | `mempalace_search` | Before spec/design — find relevant history |
| **Read** | `mempalace_kg_query` | Check current facts about entities |
| **Read** | `mempalace_kg_timeline` | View chronological decision history |
| **Write** | `mempalace_add_drawer` | Store verbatim spec/design content |
| **Write** | `mempalace_kg_add` | Record decisions as entity relationships |
| **Write** | `mempalace_kg_invalidate` | Mark decisions as superseded |
| **Diary** | `mempalace_diary_write` | Record workflow phase transitions |
| **Diary** | `mempalace_diary_read` | Retrieve last workflow state |
| **Nav** | `mempalace_traverse` | Find connected ideas across projects |
| **Nav** | `mempalace_find_tunnels` | Discover cross-project connections |

Full tool reference: [mempalaceofficial.com/reference/mcp-tools](https://mempalaceofficial.com/reference/mcp-tools)

## Relationship to Other Memory Systems

MemPalace complements (not replaces) existing memory tools:

| System | Role | Scope |
|--------|------|-------|
| **MemPalace** | Primary cross-session memory — verbatim storage + knowledge graph | Long-term, structured |
| **mem0** | Cloud backup + simple semantic search | Cross-platform |
| **Serena Memory** | Project-level symbol analysis | Project scope |
| **planning-with-files** | Current task process files | Task scope |

## Configuration

MemPalace is optional. When not configured, all v5 features work without it — the MemPalace integration points simply skip.

Detection: If `mempalace` MCP server is available → integration is active. No additional configuration beyond MCP setup.
