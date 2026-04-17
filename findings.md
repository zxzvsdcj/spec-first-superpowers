# spec-first-superpowers v5 升级可行性调研报告

> 调研日期：2026-04-17
> 基准版本：v4（2026-03-19 完成）
> 目标：核查五大集成项目更新动态 + 评估 MemPalace 集成可行性 + 设计 v5 升级方案

---

## 一、五大集成项目更新动态（v4 基准 → 当前最新）

### 1. Spec-Kit (github/spec-kit) — ⚠️ 重大演进

| 维度 | v4 基准 (2026-03-19) | 当前最新 v0.7.1 (2026-04-15) | 差距 |
|------|---------------------|------------------------------|------|
| 版本 | 未标注具体版本 | v0.7.1 | 多个版本迭代 |
| 核心变更 | `/speckit.implement` 等 3 新命令 | **Workflow Engine + Catalog System** (v0.7.0) | 🔴 架构级新增 |
| Agent 支持 | 20+ AI Agent | + Goose AI Agent (v0.6.2) | 新 Agent |
| 安装方式 | `uv tool install` | `--ai` 废弃 → `--integration` | 🟡 API 变更 |
| CI | 无 Windows | Windows 测试加入 CI 矩阵 | 改善 |
| Stars | ~80K+ | 84,648 | 持续增长 |

**关键发现**：v0.7.0 引入的 **Workflow Engine + Catalog System** 是架构级变更，允许用户注册/发现/组合自定义工作流。这与本项目的 `/super-spec` 编排逻辑有天然协同潜力。

---

### 2. OpenSpec (Fission-AI/OpenSpec) — 稳定迭代 + 新方向

| 维度 | v4 基准 (2026-03-19) | 当前最新 v1.2.0 (2026-02-23) | 差距 |
|------|---------------------|-------------------------------|------|
| 版本 | 基于 v1.0.0 OPSX Release | v1.2.0 | 2 个版本 |
| Profile 系统 | core / expanded | core / **custom** (profile 名称变更) | 🟡 术语变更 |
| 活跃 PR | — | `/opsx:refine` · sub-agent spec discovery · monorepo specs | 🟡 即将变更 |
| 新 Agent | — | + Pi (pi.dev) · Kiro (AWS) | 扩展 |
| 最后推送 | — | 2026-03-11 | 活跃 |
| Stars | ~35K | 36,954 | 持续增长 |

**关键发现**：`/opsx:refine` 命令正在开发中（PR 阶段），将支持 artifact review。Sub-agent spec discovery 是新方向，与本项目的自动化审查循环可深度整合。

---

### 3. Superpowers (obra/superpowers) — ⚠️⚠️ 架构级重大变更

| 维度 | v4 基准 (2026-03-19) | 当前最新 v5.0.7 (2026-03-31) | 差距 |
|------|---------------------|-------------------------------|------|
| 版本 | 基于 v5.0.3 左右 | v5.0.7 | 4 个版本 |
| **审查循环** | Subagent review loops（spec-document-reviewer + plan-document-reviewer） | ⚠️ **已用 inline self-review 替代** (v5.0.6) | 🔴 **架构级变更** |
| 效果 | ~25 分钟/轮 | ~30 秒/轮，质量可比 | 🔴 必须适配 |
| 新 Agent | — | + GitHub Copilot CLI v1.0.11 | 扩展 |
| Brainstorm Server | 单目录 | content/ + state/ 分离 | 安全改善 |
| Stars | ~140K | 141,472 | 持续增长 |

**🔴 这是最关键的发现**：我们 v4 花大量篇幅整合的 **Spec Review Loop** 和 **Plan Review Loop**（subagent 方式），在 Superpowers v5.0.6 中已被**彻底替换为 inline self-review checklists**。官方理由：
- 消除 ~25 分钟的 subagent 开销
- inline checklist 在 ~30 秒内捕获 3-5 个真实问题
- 质量与 subagent 审查可比

**这意味着我们 v4 中 G1/G2 的 Review Loop 机制、synergy-patterns 中的审查循环描述、quality-gates 中的 subagent reviewer 规范全部需要重写。**

---

### 4. planning-with-files (OthmanAdi/planning-with-files) — 稳定增强

| 维度 | v4 基准 (2026-03-19) | 当前最新 v2.30.0 (2026-04-03) | 差距 |
|------|---------------------|-------------------------------|------|
| 版本 | ~v2.25 | v2.30.0 | 5 个版本 |
| 新功能 | — | `--template analytics` 分析工作流 | 🟢 可选增强 |
| 国际化 | — | + 繁体中文 (zh-TW) | 扩展 |
| 新 Agent | — | + Kiro Agent | 扩展 |
| Stars | ~16K | ~18,000 | 持续增长 |

**关键发现**：核心功能保持稳定，三文件体系 + 会话恢复未变。analytics 模板是有价值的增量功能，可在调研类任务中使用。

---

### 5. ui-ux-pro-max (nextlevelbuilder/ui-ux-pro-max-skill) — 重大扩展

| 维度 | v4 基准 (2026-03-19) | 当前最新 v2.5.0 (2026-03-10) | 差距 |
|------|---------------------|-------------------------------|------|
| 版本 | v2.0 | v2.5.0 | 5 个版本 |
| 新 Skills | — | + banner-design · slides · ui-styling · design-system · design · brand | 🟡 6 个新 Skills |
| 数据 | 67 styles, 161 palettes, 57 fonts | + 1923 Google Fonts DB · 55 logo styles | 🟡 显著扩展 |
| 新 Stack | 13 stacks | + Three.js | 扩展 |
| Stars | ~50K | 56,576 | 持续增长 |

**关键发现**：v2.5.0 已远超我们 v4 文档中引用的 v2.0 数据。新增的 brand、design-system、slides 等 Skills 使其从"UI 设计辅助"升级为"全栈设计平台"。

---

## 二、MemPalace 核心能力分析

### 2.1 项目概况

| 指标 | 数据 |
|------|------|
| 版本 | v3.3.0 (2026-04-14) |
| Stars | 47,200 |
| Forks | 6,200 |
| 技术栈 | Python 88.5% · ChromaDB · SQLite |
| 许可 | MIT |
| MCP Tools | 29 个 |
| 基准 R@5 | 96.6%（无 API 调用） |

### 2.2 核心架构 — 记忆宫殿隐喻

```
Palace（宫殿）
├── Wing（翼）— 人物或项目
│   ├── Room（房间）— 具体主题
│   │   ├── Hall（大厅）— 概念分类
│   │   │   ├── hall_facts — 决策
│   │   │   ├── hall_events — 事件
│   │   │   ├── hall_discoveries — 发现
│   │   │   ├── hall_preferences — 偏好
│   │   │   └── hall_advice — 建议
│   │   └── Drawer（抽屉）— 原文存储
│   └── Tunnel（隧道）— 跨翼连接
└── Knowledge Graph — 时间线实体关系图
```

### 2.3 六大核心能力

| # | 能力 | 说明 | 对本项目价值 |
|---|------|------|-------------|
| 1 | **Verbatim Storage** | 逐字存储，不摘要/不提取/不改写 | 精准还原 spec/design 决策原文 |
| 2 | **Semantic Search + Scoping** | 语义搜索 + Wing/Room 过滤 | 跨项目 spec 模式发现 |
| 3 | **Knowledge Graph** | 时间线实体关系（SQLite），含有效期管理 | 追踪架构决策的时间演化 |
| 4 | **Agent Diary** | 每个 Agent 独立日记，AAAK 格式 | 工作流阶段审计追踪 |
| 5 | **Auto-Save Hooks** | 定时 + 上下文压缩前自动保存 | 防止长会话记忆丢失 |
| 6 | **MCP 原生集成** | 29 个 MCP 工具，支持 Cursor/Claude/ChatGPT/Gemini | 与本项目技术栈完美契合 |

### 2.4 MemPalace vs mem0 对比

| 维度 | MemPalace | mem0 |
|------|-----------|------|
| 存储方式 | 逐字存储（Verbatim） | LLM 提取摘要 |
| R@5 基准 | **96.6%**（无 API） | ~85% |
| 部署 | 本地优先（零 API 调用） | 云优先（需 API Key） |
| 费用 | 免费（MIT） | 免费层 / $19-249/月 |
| Knowledge Graph | SQLite（本地） | Neo4j（云） |
| MCP Tools | 29 个 | 9 个 |
| 结构化组织 | Wing/Room/Hall 层级 | 扁平记忆 |
| 时间追踪 | 内置有效期管理 | 无 |
| 隐私 | 100% 本地 | 需云上传 |

**结论**：MemPalace 在检索精度、结构化组织、隐私保护、成本方面全面优于 mem0。但 mem0 在"开箱即用"简易性和跨平台云同步方面仍有优势。两者应为互补关系，而非替代。

---

## 三、v4 → v5 差距汇总

### 3.1 紧急差距（🔴 架构级）

| # | 差距 | 影响 | 来源 |
|---|------|------|------|
| 1 | **Review Loops 已被 inline self-review 替代** | v4 核心机制失效 | Superpowers v5.0.6 |
| 2 | **Spec-Kit Workflow Engine + Catalog** | 新架构级能力未整合 | Spec-Kit v0.7.0 |

### 3.2 重要差距（🟡）

| # | 差距 | 影响 | 来源 |
|---|------|------|------|
| 3 | OpenSpec Profile 术语变更 (expanded → custom) | 文档不准确 | OpenSpec v1.2.0 |
| 4 | `/opsx:refine` 即将发布 | 新能力预适配 | OpenSpec PR |
| 5 | ui-ux-pro-max 6 个新 Skills 未整合 | 设计能力未释放 | ui-ux-pro-max v2.5.0 |
| 6 | Spec-Kit `--ai` → `--integration` API 变更 | 安装脚本失效 | Spec-Kit v0.7.1 |
| 7 | planning-with-files analytics 模板未利用 | 调研流程可优化 | planning-with-files v2.30.0 |
| 8 | 无持久化记忆系统集成 | 跨会话知识易丢失 | MemPalace |

### 3.3 低优先级差距（🟢）

| # | 差距 | 来源 |
|---|------|------|
| 9 | 新 Agent 支持（Goose, Pi, Kiro, Copilot CLI） | 各项目 |
| 10 | planning-with-files 繁体中文 | v2.28.0 |
| 11 | Three.js stack 未列出 | ui-ux-pro-max v2.5.0 |

---

## 四、升级方案设计

### 方案 A：全面升级 v5（推荐） ⭐

**范围**：修复所有 🔴🟡 差距 + 集成 MemPalace 作为第六大核心工具

**核心变更**：

#### A1. Review Loops → Inline Self-Review（🔴 最高优先级）
- 重写 `quality-gates.md` G1/G2 部分
- 将 subagent reviewer 替换为 inline checklist
- 更新 `synergy-patterns.md` 中的审查链
- 更新 SKILL.md description 移除 "spec/plan review loops" subagent 相关描述
- 效果：每轮审查从 ~25 分钟降至 ~30 秒

#### A2. Spec-Kit Workflow Engine 整合
- 更新 `spec-kit-workflow.md` 增加 Catalog System 说明
- 将 `/super-spec` 编排与 Workflow Engine 对齐
- 更新安装脚本 (`--ai` → `--integration`)

#### A3. MemPalace 集成（第六大核心工具）
- **新增 `references/mempalace-integration.md`**
- 在 SKILL.md 中增加 MemPalace 编排描述
- 定义 5 个集成点：
  1. **Session Recovery 增强**：palace search 补充 task_plan.md 恢复
  2. **Spec 决策持久化**：Knowledge Graph 记录架构决策时间线
  3. **跨项目模式发现**：Wing/Room 结构搜索相似 spec
  4. **Agent Diary 工作流审计**：每个 Phase 写入日记条目
  5. **Auto-Save Hooks**：适配 Cursor 环境的自动保存

#### A4. ui-ux-pro-max v2.5.0 数据同步
- 更新 SKILL.md 和 README 中的数据引用
- 整合 banner-design / slides / design-system 等新 Skills
- 更新 `synergy-patterns.md` Chain 3

#### A5. OpenSpec 术语修正 + 预适配
- 修正 Profile 术语 (expanded → custom)
- 预留 `/opsx:refine` 整合位置

#### A6. planning-with-files 增强
- 整合 analytics 模板
- 更新版本引用

**预估工作量**：8-10 个文件修改，新增 1 个 reference 文件

---

### 方案 B：最小升级（仅修复破坏性变更）

**范围**：仅修复 🔴 差距

- B1. Review Loops → Inline Self-Review
- B2. Spec-Kit `--ai` → `--integration`
- B3. 更新各版本号引用

**预估工作量**：4-5 个文件修改

**缺点**：不引入 MemPalace，不释放 ui-ux-pro-max v2.5.0 新能力，错过 Spec-Kit Workflow Engine 协同

---

### 方案 C：渐进升级（分两阶段）

**阶段 1（v4.1 热修复）**：修复 Review Loops 变更 + API 变更，1-2 小时完成
**阶段 2（v5.0 全面升级）**：集成 MemPalace + 全面更新，独立规划

**优点**：快速止血 + 充分规划
**缺点**：两次发布成本

---

## 五、方案对比

| 维度 | 方案 A（全面升级） | 方案 B（最小升级） | 方案 C（渐进） |
|------|-------------------|-------------------|----------------|
| 修复紧急差距 | ✅ | ✅ | ✅（阶段1） |
| MemPalace 集成 | ✅ | ❌ | ✅（阶段2） |
| ui-ux-pro-max v2.5.0 | ✅ | ❌ | ✅（阶段2） |
| Workflow Engine | ✅ | ❌ | ✅（阶段2） |
| 工作量 | 中大 | 小 | 小+中大 |
| 风险 | 中（一次性多变更） | 低 | 低 |
| 总发布次数 | 1 | 1 | 2 |

**AI 推荐：方案 A（全面升级）**

理由：
1. 🔴 Review Loops 变更使 v4 的核心卖点之一（自动化审查循环）实质失效，必须立即修复
2. MemPalace 是当前 AI 记忆领域的标杆项目（47K stars, 96.6% R@5），与本项目的"规范优先"理念天然互补——记忆系统确保 spec 决策跨会话不丢失
3. 各集成项目在过去一个月内均有显著更新，集中升级比分散修补更高效
4. v4 → v5 的版本跳跃契合重大能力升级的语义

---

## 六、MemPalace 集成架构设计（预案）

### 6.1 在 spec-first-superpowers 中的定位

```
spec-first-superpowers v5 编排层
├── Spec-Kit / OpenSpec — 规范生成
├── Superpowers — TDD + inline review + subagent
├── planning-with-files — 三文件持久规划
├── ui-ux-pro-max — 设计系统
└── 🆕 MemPalace — 跨会话记忆 + 知识图谱 + 决策追踪
```

### 6.2 五个集成点详细设计

#### 集成点 1：Session Recovery 增强

**现状**：仅靠 task_plan.md 恢复上下文
**升级后**：
```
Session Recovery =
  task_plan.md（当前任务上下文）
  + mempalace_search（相关历史决策）
  + mempalace_diary_read（上次工作流状态）
  + mempalace_kg_query（项目实体关系）
```

#### 集成点 2：Spec 决策 Knowledge Graph

**流程**：
```
用户确认 Spec (G1 通过)
  → mempalace_kg_add("ProjectX", "chose_auth", "Clerk", valid_from="2026-04-17")
  → mempalace_add_drawer(wing="ProjectX", room="auth", content=spec全文)

后续 Spec 变更
  → mempalace_kg_invalidate("ProjectX", "chose_auth", "Clerk")
  → mempalace_kg_add("ProjectX", "chose_auth", "Auth0", valid_from="2026-05-01")
  → 完整决策时间线可追溯
```

#### 集成点 3：跨项目 Spec 模式发现

**流程**：
```
新项目需要 "auth" spec
  → mempalace_search("auth spec decision", limit=5)
  → 返回历史项目的 auth spec 全文
  → AI 参考历史模式生成新 spec（非盲目生成）
```

#### 集成点 4：Agent Diary 工作流审计

**流程**：
```
Phase 1 (Spec) 完成
  → mempalace_diary_write(agent="spec-orchestrator",
      entry="G1|passed|auth-feature|spec-confirmed|inline-review:2-issues-fixed")

Phase 4 (Implementation) 完成
  → mempalace_diary_write(agent="spec-orchestrator",
      entry="G4|passed|auth-feature|tests:42/42|review:no-P0P1")
```

#### 集成点 5：Auto-Save Hooks (Cursor 适配)

**设计**：Cursor 不支持 Claude Code 式 hooks，但可通过 MCP 工具周期性调用实现类似效果：
- 每完成一个 Gate → 自动保存当前上下文到 Palace
- 会话结束前 → 强制保存所有未持久化的发现

### 6.3 与现有记忆系统的关系

| 系统 | 升级后角色 | 变化 |
|------|----------|------|
| mem0 | 保留，作为云端备份和简易查询 | 降级为辅助 |
| 寸止记忆 | 保留，用于用户偏好和交互规则 | 不变 |
| Serena Memory | 保留，用于项目级符号分析 | 不变 |
| planning-with-files | 保留，当前任务过程文件 | 不变 |
| 🆕 MemPalace | **新增**，主力跨会话持久记忆 | 新增 |

---

## 七、来源

| 项目 | 版本 | 来源 |
|------|------|------|
| Spec-Kit | v0.7.1 | https://github.com/github/spec-kit/releases |
| OpenSpec | v1.2.0 | https://github.com/Fission-AI/OpenSpec/releases |
| Superpowers | v5.0.7 | https://github.com/obra/superpowers/releases |
| planning-with-files | v2.30.0 | https://github.com/OthmanAdi/planning-with-files |
| ui-ux-pro-max | v2.5.0 | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases |
| MemPalace | v3.3.0 | https://github.com/MemPalace/mempalace + https://mempalaceofficial.com |
