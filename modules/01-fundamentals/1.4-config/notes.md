# 1.4 项目配置体系

## 学习日期
2026-04-08

## 学习时长
预计45分钟

---

## 核心概念

Claude Code 的配置体系就像"给 AI 写一份工作手册"。不同层级的配置决定了 Claude 在你的项目中如何行为。

```
┌─────────────────────────────────────────────────────────────┐
│                   配置体系全景图                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLAUDE.md          项目的"系统提示词"                       │
│  settings.json      行为与权限配置                           │
│  .claudeignore      文件访问边界                             │
│  hooks              事件钩子配置                             │
│                                                             │
│  优先级：命令行参数 > 项目级 > 用户级 > 默认值               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 一、CLAUDE.md — 项目的"系统提示词" ⭐核心

### 什么是 CLAUDE.md？

CLAUDE.md 是一个放在项目中的 Markdown 文件，Claude Code 启动时会**自动读取**它，将内容注入到系统提示词中。它相当于给 Claude 一份"项目须知"。

### 放在哪里？

CLAUDE.md 支持**多层级放置**，不同位置有不同作用域：

```
~/.claude/CLAUDE.md              ← 全局级：所有项目都生效
~/personal/FreshClaude/CLAUDE.md ← 项目根目录：本项目生效
~/personal/FreshClaude/src/CLAUDE.md ← 子目录：处理该目录时生效
```

### 层级优先级

```
┌────────────────────────────────────────┐
│ 子目录 CLAUDE.md    ← 最高优先级       │
│ 项目根 CLAUDE.md    ← 中等优先级       │
│ ~/.claude/CLAUDE.md ← 最低优先级       │
└────────────────────────────────────────┘
```

当多个 CLAUDE.md 存在时，**所有层级都会被加载**，内容叠加。如果有冲突，更具体（更近）的层级优先。

### 应该写什么？

**CLAUDE.md 的黄金法则：写你希望每次对话都生效的指令。**

| 适合放入 | 不适合放入 |
|---------|-----------|
| 项目概述和目标 | 具体的任务指令 |
| 代码规范和约定 | 一次性的调试信息 |
| Commit 消息格式 | 详细的 API 文档 |
| 构建/测试命令 | 大段代码示例 |
| 文件组织规则 | 临时性的注意事项 |
| 重要的架构决策 | 可以从代码推导的信息 |

### 实际示例：我们项目的 CLAUDE.md

```markdown
# FreshClaude - Claude Code 学习项目

## 项目概述
这是一个系统学习Claude Code的交互式教程仓库。

## Commit规范
- `learn: ` - 学习记录提交
- `project: ` - 项目代码提交
- `docs: ` - 文档更新
- `reflect: ` - 反思总结提交

## 文件组织
- `modules/` - 按模块组织的学习内容
- `prompts/` - 提示词存档
- `projects/` - 实战项目代码
```

### 常见模式

**1. 后端 API 项目**
```markdown
# MyAPI

## 技术栈
- Python 3.12 + FastAPI
- PostgreSQL + SQLAlchemy
- pytest for testing

## 开发命令
- `make test` - 运行测试
- `make lint` - 代码检查
- `make dev` - 启动开发服务器

## 代码规范
- 使用 snake_case
- 所有 API 端点需要有类型注解
- 新增端点必须附带测试
```

**2. 前端项目**
```markdown
# MyApp

## 技术栈
- React 19 + TypeScript
- Tailwind CSS
- Vitest for testing

## 重要约定
- 组件文件使用 PascalCase
- 使用 Server Components 优先
- 样式使用 Tailwind，不要写 CSS 文件
```

**3. Monorepo 项目**
```markdown
# 根目录 CLAUDE.md
## 项目结构
- packages/api - 后端服务
- packages/web - 前端应用
- packages/shared - 共享类型

## 规则
- 修改 shared 包后必须检查所有依赖包
```

### 反模式（避免这样做）

```markdown
# ❌ 不好的 CLAUDE.md

## 所有 API 端点
GET /users - 获取用户列表
GET /users/:id - 获取单个用户
POST /users - 创建用户
PUT /users/:id - 更新用户
DELETE /users/:id - 删除用户
... (100+ 行 API 文档)

## 完整的数据库 Schema
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  ...
);
... (200+ 行 SQL)
```

问题：太长了，每次对话都会消耗大量上下文 token。这些信息应该放在代码中，Claude 需要时可以自己读取。

---

## 二、settings.json — 行为与权限配置

### 位置

settings.json 也有多个层级：

```
~/.claude/settings.json                                    ← 用户级（全局）
.claude/settings.json                                      ← 项目级（提交到 git）
.claude/settings.local.json                                ← 项目级本地（不提交）
```

### 你的全局 settings.json

目前你的全局配置是：
```json
{
  "model": "azure/anthropic/claude-opus-4-6",
  "enabledPlugins": {
    "superpowers@claude-plugins-official": true
  }
}
```

### 可配置内容

```json
{
  // 权限：允许的工具操作
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(npm run lint)",
      "Read",
      "Write(*.md)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force)"
    ]
  },

  // 环境变量
  "env": {
    "NODE_ENV": "development",
    "DEBUG": "true"
  },

  // MCP 服务器配置
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "..."
      }
    }
  }
}
```

### 权限配置详解

权限系统是安全的核心，决定了 Claude 可以自动执行什么、需要确认什么。

```
┌─────────────────────────────────────────────────────────────┐
│                    权限决策流程                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Claude 想执行一个操作                                       │
│       │                                                     │
│       ▼                                                     │
│  在 deny 列表中？──── 是 ────→ 🚫 拒绝                      │
│       │                                                     │
│       否                                                    │
│       ▼                                                     │
│  在 allow 列表中？──── 是 ────→ ✅ 自动执行                  │
│       │                                                     │
│       否                                                    │
│       ▼                                                     │
│  📋 弹出确认提示，等待用户决定                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**权限模式匹配语法**：
```
Bash(npm test)          ← 精确匹配命令
Bash(npm run *)         ← 通配符匹配
Read                    ← 允许所有读操作
Write(*.md)             ← 只允许写 .md 文件
Edit(src/**)            ← 只允许编辑 src 下的文件
```

### 项目级 vs 用户级

| 层级 | 文件 | 提交到 git？ | 适用场景 |
|------|------|-------------|---------|
| 用户级 | `~/.claude/settings.json` | 否 | 个人偏好、API key |
| 项目级（共享） | `.claude/settings.json` | 是 | 团队共享规则 |
| 项目级（本地） | `.claude/settings.local.json` | 否 | 个人在此项目的偏好 |

**优先级**：项目本地 > 项目共享 > 用户级

---

## 三、.claudeignore — 文件访问边界

### 什么是 .claudeignore？

类似 `.gitignore`，告诉 Claude Code **不要读取或处理**哪些文件。

### 放置位置

```
~/personal/FreshClaude/.claudeignore  ← 项目根目录
```

### 语法（与 .gitignore 相同）

```gitignore
# 忽略 node_modules
node_modules/

# 忽略构建产物
dist/
build/
*.min.js

# 忽略敏感文件
.env
.env.*
credentials.json
*.pem
*.key

# 忽略大文件
*.zip
*.tar.gz
data/*.csv

# 忽略日志
*.log
logs/
```

### 为什么需要 .claudeignore？

```
┌─────────────────────────────────────────────────────────────┐
│                 .claudeignore 的三个作用                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔒 安全     防止 Claude 读取/暴露敏感文件                    │
│              如 .env、密钥、凭证                              │
│                                                             │
│  ⚡ 效率     避免搜索大型目录浪费 token                       │
│              如 node_modules（数万文件）                      │
│                                                             │
│  🎯 聚焦     让 Claude 专注于项目代码                         │
│              忽略生成的文件、第三方代码                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### .claudeignore vs .gitignore

| 特性 | .gitignore | .claudeignore |
|------|-----------|---------------|
| 作用对象 | Git 版本控制 | Claude Code 文件访问 |
| 默认行为 | Claude 已自动尊重 .gitignore | 额外的排除规则 |
| 典型内容 | 构建产物、依赖 | 敏感文件、大型数据文件 |

**重要**：Claude Code 默认已经尊重 `.gitignore`。`.claudeignore` 是用来添加**额外**的排除规则，比如你想在 git 中跟踪但不想让 Claude 读取的文件。

---

## 四、Hooks 配置（预览）

Hooks 是事件驱动的 shell 命令，在 Claude 执行特定操作时自动触发。

### 配置位置

在 settings.json 中配置：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'About to run a bash command'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "say 'Claude needs your attention'"
          }
        ]
      }
    ]
  }
}
```

### Hook 事件类型

| 事件 | 触发时机 | 典型用途 |
|------|---------|---------|
| PreToolUse | 工具调用前 | 验证、拦截危险操作 |
| PostToolUse | 工具调用后 | 自动格式化、lint |
| Notification | Claude 需要注意时 | 声音/桌面通知 |
| Stop | 回合结束时 | 自动测试、检查 |

这部分在模块二会深入学习。

---

## 五、配置优先级总览

```
┌─────────────────────────────────────────────────────────────┐
│                   配置优先级（高→低）                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. 命令行参数                                               │
│     claude --model sonnet --allowedTools "Bash(npm *)"      │
│                                                             │
│  2. 子目录 CLAUDE.md                                        │
│     ./src/CLAUDE.md                                         │
│                                                             │
│  3. 项目根 CLAUDE.md                                        │
│     ./CLAUDE.md                                             │
│                                                             │
│  4. 项目级设置（本地）                                       │
│     .claude/settings.local.json                             │
│                                                             │
│  5. 项目级设置（共享）                                       │
│     .claude/settings.json                                   │
│                                                             │
│  6. 用户级 CLAUDE.md                                        │
│     ~/.claude/CLAUDE.md                                     │
│                                                             │
│  7. 用户级设置                                               │
│     ~/.claude/settings.json                                 │
│                                                             │
│  8. 系统默认值                                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 实际场景

```
场景：你在公司项目中工作

~/.claude/CLAUDE.md        → "我喜欢简洁的回复"
~/.claude/settings.json    → model: opus

project/CLAUDE.md          → "使用 TypeScript，遵循团队规范"
project/.claude/settings.json → allow: Bash(npm test)

project/src/CLAUDE.md      → "组件使用函数式写法"

→ 最终效果：所有规则叠加生效，冲突时更具体的层级胜出
```

---

## 六、实战练习

### 练习1：查看当前配置

让我们看看你当前项目的实际配置状态。

**当前 CLAUDE.md 内容**已在你的项目根目录中。

**当前 settings.json**：
- 全局：`~/.claude/settings.json` → 设置了模型和插件
- 项目级：不存在（可以创建）

**当前 .claudeignore**：不存在（可以创建）

### 练习2：为本项目创建 .claudeignore

根据项目特点，以下文件应该被忽略：

```gitignore
# Python
__pycache__/
*.pyc
.venv/

# 敏感文件
.env
.env.*

# 大型文件
*.zip
*.tar.gz

# OS 文件
.DS_Store
Thumbs.db
```

### 练习3：思考 CLAUDE.md 优化

看我们当前的 CLAUDE.md，思考：
1. 有没有不必要的内容？（每次都会消耗 token）
2. 有没有缺失的重要信息？
3. 内容是否足够简洁？

---

## 核心要点

1. **CLAUDE.md 是最重要的配置** — 它决定了 Claude 对项目的"理解"
2. **写得精简** — CLAUDE.md 每次对话都会加载，内容越多消耗越大
3. **多层级叠加** — 所有层级的配置都会生效，越具体优先级越高
4. **安全第一** — 用 .claudeignore 保护敏感文件，用 permissions 限制危险操作
5. **团队协作** — .claude/settings.json 提交到 git，settings.local.json 留本地

---

## 与 Cursor 的对比

| 配置项 | Cursor | Claude Code |
|--------|--------|-------------|
| 项目指令 | `.cursorrules` | `CLAUDE.md` |
| 行为设置 | Cursor Settings UI | `settings.json` |
| 文件忽略 | `.cursorignore` | `.claudeignore` |
| 配置层级 | 2层（全局+项目） | 4层（全局+项目+子目录+本地） |
| 格式 | 纯文本 | Markdown / JSON |

**关键区别**：Claude Code 的配置更灵活（支持子目录级别），但也需要更多主动管理。

---

## 扩展资源

| 资源 | 链接 | 说明 |
|------|------|------|
| CLAUDE.md 最佳实践 | https://www.anthropic.com/engineering/claude-code-best-practices | 官方推荐的 CLAUDE.md 写法 |
| 配置文档 | https://docs.anthropic.com/en/docs/claude-code/settings | settings.json 完整参考 |
| Hooks 文档 | https://docs.anthropic.com/en/docs/claude-code/hooks | Hooks 配置详解 |

---

## 待填写

### 实践结果
（记录你尝试的配置和观察）

### 个人反思
（完成后填写）

### 自评
- 理解程度：_/5
- 实践熟练度：_/5
