# 2.1 Skills 系统深度剖析

## 学习日期
2026-04-08

## 学习时长
预计45分钟

---

## 核心概念

Skill 是 Claude Code 最强大的扩展机制之一。理解 Skill 是成为 Agent 工程师的关键一步。

```
┌─────────────────────────────────────────────────────────────┐
│                     Skill 是什么？                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  一个可复用的"专家指令包"                                    │
│                                                             │
│  Skill = SKILL.md (指令) + Scripts (脚本) + References (文档)│
│                                                             │
│  类比：                                                      │
│  - 如果 CLAUDE.md 是"公司员工手册"                           │
│  - 那 Skill 就是"特定岗位的操作手册"                         │
│  - 需要时才打开，用完就收起                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 与 CLAUDE.md 的关键区别

| 特性 | CLAUDE.md | Skill |
|------|-----------|-------|
| 加载时机 | **每次对话**自动加载 | **按需**触发加载 |
| Token 消耗 | 始终占用 | 触发时才占用 |
| 内容量 | 应保持精简 | 可以很详细 |
| 用途 | 项目全局规则 | 特定任务的专家流程 |
| 复用范围 | 本项目 | 跨项目复用 |

---

## 一、Skill 的架构

### 文件结构

```
my-skill/
├── SKILL.md              ← 必需：核心指令文件
│   ├── YAML frontmatter  ← 元数据（name, description）
│   └── Markdown 正文     ← 详细的工作流程指令
│
├── scripts/              ← 可选：可执行脚本
│   └── analyze.py        ← 确定性、可重复的操作
│
├── references/           ← 可选：参考文档
│   └── api-docs.md       ← 需要时加载到上下文
│
└── assets/               ← 可选：模板和资源
    └── template.html     ← 输出用的模板文件
```

### SKILL.md 的核心结构

```markdown
---
name: my-awesome-skill
description: 当用户需要做 X 时使用此 Skill。适用于 Y 场景。
---

# Skill 标题

## 工作流程
1. 第一步：...
2. 第二步：...

## 参考资料
（按需加载 references/ 下的文件）
```

**关键**：`description` 字段决定了 Skill 何时被触发。Claude 根据这个描述判断是否需要激活这个 Skill。

---

## 二、Skill 的触发机制

```
┌─────────────────────────────────────────────────────────────┐
│                   Skill 触发方式                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. 手动触发（Slash Command）                                │
│     /commit          → 调用 commit skill                    │
│     /code-review     → 调用 code-review skill               │
│     /review-pr 123   → 调用 pr-review skill，参数为 123     │
│                                                             │
│  2. 自动触发（AI 判断）                                      │
│     用户说"帮我提交代码" → Claude 自动匹配 commit skill      │
│     用户说"审查这个PR"  → Claude 自动匹配 review skill       │
│                                                             │
│  判断依据：SKILL.md 的 description 字段                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 自动触发的工作原理

```
用户输入 → Claude 分析意图
              │
              ▼
         匹配已安装 Skill 的 description
              │
              ├─ 匹配度高 → 自动加载 Skill 指令
              │
              └─ 无匹配   → 使用通用能力处理
```

---

## 三、Skill 的来源

### 1. 插件内置 Skill（Plugin Skills）

通过插件系统安装，存放在 `~/.claude/plugins/` 下。

**你当前已安装的插件（superpowers）包含的 Skill 类别**：

| 类别 | 示例 Skill | 用途 |
|------|-----------|------|
| 开发流程 | commit, commit-push-pr | 智能提交、推送、创建 PR |
| 代码质量 | code-review, review-pr | 多 Agent 协同代码审查 |
| 项目管理 | feature-dev | 特性开发全流程 |
| 前端设计 | frontend-design | UI 设计与实现 |
| 配置管理 | claude-md-improver | 优化 CLAUDE.md |
| MCP 开发 | build-mcp-server | 构建 MCP 服务器 |
| Skill 创建 | skill-creator | 创建和优化新 Skill |
| 插件开发 | plugin-dev | 开发 Claude Code 插件 |

### 2. 项目自定义 Skill

放在项目的 `.claude/skills/` 目录下：

```
my-project/
└── .claude/
    └── skills/
        └── my-project-skill/
            └── SKILL.md
```

### 3. 用户自定义 Skill

放在 `~/.claude/skills/` 下，所有项目可用。

---

## 四、实际 Skill 解析

### 示例1：commit Skill（最常用）

来看你系统中实际安装的 `/commit` 指令：

```markdown
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context
- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task
Based on the above changes, create a single git commit.
Stage and create the commit using a single message.
```

**精妙之处**：
1. `allowed-tools` — 限制 Skill 只能使用 git 相关命令
2. `!` 前缀命令 — 在加载时自动执行，注入实时上下文
3. 指令简洁明确 — 没有多余的解释

### 示例2：code-review Skill（多 Agent 协同）

这个 Skill 展示了 Agent 工程的高级模式：

```
code-review 的工作流程：

1. Haiku Agent → 检查 PR 是否需要审查
2. Haiku Agent → 收集相关 CLAUDE.md 文件
3. Haiku Agent → 获取 PR 变更摘要
4. 5 个并行 Sonnet Agent → 独立审查
   ├─ Agent 1: CLAUDE.md 合规检查
   ├─ Agent 2: 浅层 Bug 扫描
   ├─ Agent 3: Git 历史上下文审查
   ├─ Agent 4: 历史 PR 评论检查
   └─ Agent 5: 代码注释合规检查
5. 多个并行 Haiku Agent → 对每个发现打分 (0-100)
6. 过滤 → 只保留 80+ 分的高置信度问题
7. Haiku Agent → 重新检查 PR 资格
8. 最终输出 → 发表 GitHub 评论
```

**这就是 Agent 工程的核心**：任务分解 + 并行执行 + 结果聚合。
后续 2.5 会深入讲解这些模式。

---

## 五、Skill 设计的核心原则

### 1. 精准的 Description

```markdown
# ❌ 模糊的 description
description: 帮助处理代码

# ✅ 精准的 description
description: 当用户需要将 Python 2 代码迁移到 Python 3 时使用。
适用于：语法转换、库替换、兼容性检查。
```

### 2. 渐进式信息加载

```
Skill 加载时 → 只加载 SKILL.md 核心指令
执行过程中   → 按需读取 references/ 下的文档
需要计算时   → 调用 scripts/ 下的脚本
```

这比把所有内容塞进 CLAUDE.md 高效得多。

### 3. 工具权限限制

```markdown
---
# 限制 Skill 可以使用的工具
allowed-tools: Bash(npm test:*), Read, Edit
---
```

最小权限原则 — 只给 Skill 它需要的工具。

### 4. 幂等性

好的 Skill 应该是幂等的 — 执行多次结果一致，不会产生副作用。

---

## 六、Skill vs 其他扩展方式对比

```
┌─────────────────────────────────────────────────────────────┐
│               扩展 Claude Code 的方式                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLAUDE.md    │ 项目全局规则，始终加载                       │
│               │ → "每次都要知道的事"                         │
│               │                                             │
│  Skill        │ 按需加载的专家流程                           │
│               │ → "特定任务时才需要的专业知识"               │
│               │                                             │
│  Hook         │ 事件驱动的自动化脚本                        │
│               │ → "每次做 X 时自动执行 Y"                   │
│               │                                             │
│  MCP Server   │ 外部服务连接                                │
│               │ → "给 Claude 新的工具/数据源"                │
│               │                                             │
│  Memory       │ 跨会话持久化信息                            │
│               │ → "记住用户偏好和项目状态"                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 核心要点

1. **Skill = 按需加载的专家指令包**，比 CLAUDE.md 更适合放详细流程
2. **触发方式**：手动（/command）或自动（AI 根据 description 匹配）
3. **description 是灵魂** — 决定了 Skill 是否能被正确触发
4. **多 Agent 协同**是高级 Skill 的核心模式（如 code-review）
5. **渐进式加载** — 核心指令先加载，详细文档按需读取

---

## 扩展资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 插件开发文档 | https://docs.anthropic.com/en/docs/claude-code/plugins | 插件和 Skill 的官方文档 |
| Skill 最佳实践 | https://www.anthropic.com/engineering/claude-code-best-practices | 包含 Skill 设计建议 |
| 官方插件仓库 | https://github.com/anthropics/claude-code-plugins | 官方 Skill/Plugin 示例 |

---

## 待填写

### 实践结果
（记录你尝试的 Skill 和观察）

### 个人反思
（完成后填写）

### 自评
- 理解程度：_/5
- 实践熟练度：_/5
