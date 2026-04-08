# 2.2 热门 Skills 实操

## 学习日期
2026-04-08

## 学习时长
预计1.5小时

---

## 你系统中实际可用的 Skills

基于你安装的 `commit-commands` 和 `superpowers` 插件，以下是完整的可用 Skill 列表：

---

## 一、Git 工作流类（commit-commands 插件）

### /commit — 智能提交

**作用**：分析变更，自动生成 commit message 并提交

**工作原理**：
```
自动执行 git status / git diff / git log
        ↓
分析变更内容，生成语义化 commit message
        ↓
git add + git commit
```

**源码解析**（仅 18 行 Markdown）：
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
```

**设计亮点**：
- `allowed-tools` 限制只能用 git 命令（安全）
- `!` 前缀自动执行命令注入上下文（高效）
- 读取最近 10 条 commit 来**模仿你的 commit 风格**

---

### /commit-push-pr — 一键提交+推送+创建PR

**作用**：从提交到创建 PR 一步到位

**工作流程**：
```
1. 如果在 main 分支 → 自动创建新分支
2. 生成 commit message → git commit
3. git push -u origin
4. gh pr create
```

**适用场景**：
- 快速修复一个 bug
- 小改动不想手动走 PR 流程

---

### /clean_gone — 清理过时分支

**作用**：删除远程已经不存在但本地还留着的分支

**工作流程**：
```
git branch -v → 找到标记为 [gone] 的分支
        ↓
检查是否有关联的 worktree
        ↓
移除 worktree + 删除分支
```

---

## 二、开发流程类（superpowers 插件）

### brainstorming — 创意发散 ⭐

**触发条件**：创建功能、构建组件、添加功能之前

**作用**：在动手写代码之前，先探索用户意图、需求和设计

**为什么重要**：
```
❌ 没有 brainstorming：
   "添加搜索功能" → 直接开始写代码 → 方向可能错误

✅ 有 brainstorming：
   "添加搜索功能" → 先讨论：搜索什么？全文还是模糊？
                     前端还是后端？实时还是提交后？
                   → 明确需求后再动手
```

---

### writing-plans — 编写实施计划

**触发条件**：有需求规格、需要多步骤实现时

**作用**：制定详细的实施方案，分解为可执行步骤

---

### executing-plans — 执行计划

**触发条件**：有已编写的实施计划时

**作用**：按计划逐步实施，设置审查检查点

---

### feature-dev — 特性开发全流程 ⭐⭐

**最完整的开发工作流 Skill**，包含 7 个阶段：

```
┌─────────────────────────────────────────────────────────────┐
│              feature-dev 七阶段流程                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Phase 1: Discovery（需求理解）                              │
│  → 创建 todo list，确认要解决的问题                          │
│                                                             │
│  Phase 2: Codebase Exploration（代码探索）                   │
│  → 2-3个并行 Agent 探索代码库不同方面                        │
│  → 读取 Agent 标注的关键文件                                 │
│                                                             │
│  Phase 3: Clarifying Questions（澄清问题）⭐关键             │
│  → 识别所有模糊点、边缘情况                                  │
│  → 列出问题等用户回答，不做假设                              │
│                                                             │
│  Phase 4: Architecture Design（架构设计）                    │
│  → 2-3个并行 Architect Agent 设计不同方案                    │
│  → 对比方案，给出推荐                                       │
│                                                             │
│  Phase 5: Implementation（实现）                             │
│  → 必须等用户批准后才开始                                    │
│  → 遵循代码库约定                                           │
│                                                             │
│  Phase 6: Quality Review（质量审查）                         │
│  → 3个并行 Reviewer Agent 审查不同维度                       │
│  → 简洁性/正确性/规范性                                      │
│                                                             │
│  Phase 7: Summary（总结）                                    │
│  → 文档化变更和决策                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**核心设计理念**：
- **先理解再动手** — 不急于写代码
- **多 Agent 并行** — 用不同视角探索代码库
- **人在决策环** — 每个阶段都等用户确认
- **多方案对比** — 不是给一个方案，而是给多个选择

---

### test-driven-development — TDD 开发

**触发条件**：实现功能或修 bug 之前

**作用**：先写测试，再写实现

```
红灯 → 绿灯 → 重构
 ↓       ↓       ↓
写失败测试  写最小实现  优化代码
```

---

### systematic-debugging — 系统化调试

**触发条件**：遇到 bug、测试失败、意外行为时

**作用**：系统化诊断问题，而不是盲目猜测

---

## 三、代码质量类

### review-pr — 综合 PR 审查 ⭐

**多 Agent 协同审查**，6个专项 Agent：

| Agent | 职责 |
|-------|------|
| comment-analyzer | 注释准确性与维护性 |
| pr-test-analyzer | 测试覆盖率与质量 |
| silent-failure-hunter | 静默失败检测 |
| type-design-analyzer | 类型设计分析 |
| code-reviewer | 通用代码审查 |
| code-simplifier | 代码简化建议 |

**使用方式**：
```
/review-pr              ← 全面审查
/review-pr tests errors ← 只审查测试和错误处理
/review-pr simplify     ← 只做代码简化建议
/review-pr all parallel ← 所有 Agent 并行执行
```

**输出格式**：
```markdown
# PR Review Summary

## Critical Issues (必须修复)
## Important Issues (应该修复)
## Suggestions (建议)
## Strengths (做得好的地方)
## Recommended Action (推荐操作)
```

---

### simplify — 代码简化

**作用**：审查变更代码的复用性、质量和效率

---

### verification-before-completion — 完成前验证

**触发条件**：即将声称工作完成时

**作用**：必须运行验证命令并确认输出，才能声称"完成"

**原则**：证据先于断言（Evidence before assertions）

---

## 四、协作与管理类

### dispatching-parallel-agents — 并行 Agent 调度

**触发条件**：有 2+ 个独立任务可以同时进行

**作用**：将无依赖的任务分发给多个 Agent 并行执行

---

### using-git-worktrees — Git Worktree 使用

**作用**：创建隔离的工作树，不影响当前工作区

---

### finishing-a-development-branch — 完成开发分支

**触发条件**：实现完成、测试通过后

**作用**：引导选择合并策略（merge/PR/cleanup）

---

## Skill 选择决策树

```
你要做什么？
    │
    ├─ 提交代码
    │   ├─ 只提交 ────────────→ /commit
    │   └─ 提交+推送+PR ─────→ /commit-push-pr
    │
    ├─ 开发新功能
    │   ├─ 明确需求 ──────────→ /feature-dev
    │   └─ 需求模糊 ──────────→ brainstorming 先
    │
    ├─ 审查代码
    │   ├─ PR 审查 ───────────→ /review-pr
    │   └─ 本地审查 ──────────→ simplify
    │
    ├─ 修复 Bug
    │   └─ ───────────────────→ systematic-debugging
    │
    ├─ 写测试
    │   └─ ───────────────────→ test-driven-development
    │
    └─ 清理分支
        └─ ───────────────────→ /clean_gone
```

---

## 核心要点

1. **Git 工作流三件套**：/commit, /commit-push-pr, /clean_gone 覆盖日常 git 操作
2. **feature-dev 是最完整的开发 Skill**：7阶段全流程，多 Agent 协同
3. **review-pr 是最复杂的审查 Skill**：6个专项 Agent 并行审查
4. **brainstorming 应该先于一切创造性工作**：先想清楚再动手
5. **verification-before-completion 防止"虚假完成"**：证据先于断言

---

## 待填写

### 实践结果
（记录你尝试的 Skill 和观察）

### 个人反思
（完成后填写）

### 自评
- 理解程度：_/5
- 实践熟练度：_/5
