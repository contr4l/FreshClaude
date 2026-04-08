# Claude Code 系统学习计划
## 目标：成为合格的初级Agent工程师

---

## 核心理念：从AI IDE到Native AI的观念转变

### 传统AI IDE (Cursor/Copilot) vs Native AI (Claude Code)

| 维度 | AI IDE模式 | Native AI模式 |
|------|-----------|---------------|
| **交互方式** | 补全/建议/对话窗口 | 完全对话驱动，AI是主导执行者 |
| **控制权** | 开发者主导，AI辅助 | 开发者设定目标，AI自主规划执行 |
| **上下文** | IDE管理文件上下文 | 开发者需要主动管理上下文 |
| **工作流** | 融入传统开发流程 | 重新定义开发流程 |
| **思维模式** | "帮我写这段代码" | "帮我解决这个问题" |

### Native AI开发者需要培养的核心能力

1. **问题定义能力** - 清晰表达目标而非具体步骤
2. **上下文管理能力** - 知道何时提供什么信息
3. **验证审查能力** - 审查AI输出而非逐行编写
4. **任务分解能力** - 将复杂任务拆解为可验证的子任务
5. **反馈迭代能力** - 有效地纠正和引导AI行为
6. **工具编排能力** - 理解并配置AI的工具链

---

## 模块一：基础入门与观念重塑 (3小时)

### 1.1 Claude Code核心概念 (30分钟)
- [ ] Claude Code架构理解：工具、权限、沙箱
- [ ] 对话即编程：prompt作为新的编程语言
- [ ] 理解"委托"而非"指令"的思维方式
- [ ] 📝 学习记录 & 个人总结

### 1.2 基础工具链精通 (45分钟)
- [ ] 文件操作三件套：Read/Write/Edit的最佳使用场景
- [ ] 搜索工具：Glob vs Grep，何时用哪个
- [ ] Bash工具：能做什么、不该做什么
- [ ] 工具组合：并行调用与串行依赖
- [ ] 📝 学习记录 & 个人总结

### 1.3 内置指令深度解析 (45分钟)
- [ ] /help, /status - 环境感知
- [ ] /clear, /compact - 上下文管理的艺术
- [ ] /config, /permissions - 权限与配置
- [ ] /memory, /forget - 持久化记忆
- [ ] /cost - 成本意识培养
- [ ] 📝 学习记录 & 个人总结

### 1.4 项目配置体系 (45分钟)
- [ ] CLAUDE.md：项目的"系统提示词"
- [ ] settings.json：行为配置详解
- [ ] .claudeignore：安全与效率的边界
- [ ] 多层配置优先级理解
- [ ] 📝 学习记录 & 个人总结

### 📚 模块一扩展资源
| 资源类型 | 链接 | 说明 |
|---------|------|------|
| 官方文档 | https://docs.anthropic.com/en/docs/claude-code | Claude Code完整文档 |
| GitHub仓库 | https://github.com/anthropics/claude-code | 官方仓库，含示例配置 |
| 视频教程 | https://www.youtube.com/watch?v=3G9-mtJ3XDo | Anthropic官方介绍视频 |
| 博客 | https://www.anthropic.com/engineering/claude-code-best-practices | 官方最佳实践博客 |

### 🎯 模块一检查点
- 能独立配置一个新项目的Claude Code环境
- 理解工具选择的决策逻辑
- 完成观念转变自我评估

---

## 模块二：进阶功能与生态系统 (6小时)

### 2.1 Skills系统深度剖析 (45分钟)
- [ ] Skill的本质：可复用的prompt模板
- [ ] 内置Skills分类与使用场景
- [ ] Skill触发机制：自动vs手动
- [ ] 📝 学习记录 & 个人总结

### 2.2 GitHub热门Skills实操 (1.5小时)

#### 开发效率类
- [ ] **commit** - 智能提交信息生成
- [ ] **pr-review** - 代码审查自动化
- [ ] **refactor** - 重构建议与执行

#### 代码质量类
- [ ] **test-gen** - 测试用例生成
- [ ] **doc-gen** - 文档自动生成

#### 项目管理类
- [ ] **changelog** - 变更日志生成
- [ ] **issue-triage** - Issue分类处理

- [ ] 📝 学习记录 & 个人总结

### 2.3 自定义Skill开发 (1小时)
- [ ] Skill文件结构规范
- [ ] Frontmatter配置详解
- [ ] 触发条件设计
- [ ] 实战：创建个人专属Skill
- [ ] 📝 学习记录 & 个人总结

### 2.4 Hooks系统精通 (1小时)
- [ ] Hook的执行时机与生命周期
- [ ] PreToolCall：拦截与增强
- [ ] PostToolCall：后处理与验证
- [ ] 实战：自动格式化Hook
- [ ] 实战：安全检查Hook
- [ ] 📝 学习记录 & 个人总结

### 2.5 Agent并行处理 - 业界最佳实践 (1.5小时)

#### 理论基础
- [ ] 多Agent架构模式
- [ ] 任务依赖图与并行度分析
- [ ] 上下文隔离vs共享策略

#### 实践模式
- [ ] **Map-Reduce模式**：大规模代码分析
- [ ] **Pipeline模式**：多阶段处理流程
- [ ] **Swarm模式**：独立任务并行执行
- [ ] **Supervisor模式**：主Agent协调子Agent

#### 最佳实践
- [ ] 何时并行、何时串行的决策框架
- [ ] 子Agent prompt设计原则
- [ ] 结果聚合与冲突处理

- [ ] 📝 学习记录 & 个人总结

### 📚 模块二扩展资源
| 资源类型 | 链接 | 说明 |
|---------|------|------|
| Skills集合 | https://github.com/anthropics/claude-code-skills | 官方Skills示例 |
| 社区Skills | https://github.com/topics/claude-code-skill | GitHub社区Skills |
| Hooks文档 | https://docs.anthropic.com/en/docs/claude-code/hooks | Hooks配置详解 |
| Agent SDK | https://github.com/anthropics/claude-agent-sdk | Agent SDK源码 |
| 多Agent论文 | https://arxiv.org/abs/2308.08155 | MetaGPT多Agent协作论文 |
| Swarm框架 | https://github.com/openai/swarm | OpenAI Swarm（参考设计） |
| CrewAI | https://github.com/joaomdmoura/crewAI | 多Agent编排框架 |
| LangGraph | https://github.com/langchain-ai/langgraph | Agent工作流框架 |

### 🎯 模块二检查点
- 能创建和使用自定义Skills
- 能配置实用的Hooks
- 掌握至少3种Agent并行模式

---

## 模块三：工程实践与项目实战 (6小时)

### 3.1 Git工作流集成 (45分钟)
- [ ] Claude Code的Git最佳实践
- [ ] 自动commit：何时做、怎么做
- [ ] PR驱动开发流程
- [ ] Git worktree隔离开发
- [ ] 📝 学习记录 & 个人总结

### 3.2 任务管理系统 (45分钟)
- [ ] Task工具的完整用法
- [ ] Plan模式：复杂任务的规划
- [ ] 任务依赖与阻塞管理
- [ ] 📝 学习记录 & 个人总结

### 3.3 测试驱动开发(TDD)配合 (30分钟)
- [ ] TDD在Native AI中的新实践
- [ ] 让Claude Code先写测试
- [ ] 红-绿-重构的AI版本
- [ ] 📝 学习记录 & 个人总结

### 3.4 实战项目 (3小时)

#### 项目A：CLI工具开发（入门级，1小时）
**目标**：开发一个命令行Todo管理工具
- 需求分析与任务分解
- 使用TDD方式开发
- 完整的Git工作流

**评价维度**：
| 维度 | 1分 | 3分 | 5分 |
|------|-----|-----|-----|
| 代码质量 | 能运行 | 结构清晰 | 可维护性强 |
| 测试覆盖 | 无测试 | 主流程覆盖 | 边界情况覆盖 |
| Git规范 | 单次提交 | 有逻辑分割 | 原子提交+清晰信息 |
| Prompt效率 | >15轮 | 8-15轮 | <8轮 |

#### 项目B：API服务开发（中级，1小时）
**目标**：开发一个RESTful API服务
- 多文件项目组织
- 并行Agent处理多个endpoint
- 集成测试编写

**评价维度**：
| 维度 | 1分 | 3分 | 5分 |
|------|-----|-----|-----|
| API设计 | 能工作 | RESTful规范 | 一致性+文档 |
| 错误处理 | 无处理 | 基本处理 | 完整+友好提示 |
| Agent使用 | 未使用 | 合理使用 | 高效并行 |

#### 项目C：代码重构实战（高级，1小时）
**目标**：对一个遗留代码库进行重构
- 代码理解与分析
- 重构计划制定
- 渐进式重构执行

**评价维度**：
| 维度 | 1分 | 3分 | 5分 |
|------|-----|-----|-----|
| 安全性 | 破坏功能 | 功能保持 | 有回归测试 |
| 改进幅度 | 微小改动 | 明显改善 | 质的提升 |
| 过程管理 | 无规划 | 有计划 | 可追溯+可回滚 |

- [ ] 📝 学习记录 & 个人总结

### 3.5 评价反馈体系 (15分钟)

#### 自我评估量表
| 维度 | 初级(1-2) | 中级(3-4) | 高级(5) |
|------|-----------|-----------|---------|
| Prompt质量 | 能表达基本需求 | 提供清晰上下文 | 预见AI需要的信息 |
| 任务分解 | 单一任务 | 多步骤任务 | 复杂依赖任务 |
| 验证能力 | 依赖AI自检 | 发现明显问题 | 系统性验证 |
| 工具使用 | 基础工具 | Skills & Hooks | 自定义扩展 |
| 效率 | >10轮/功能 | 5-10轮/功能 | <5轮/功能 |

#### 每日反思三问
1. 今天哪个prompt最有效？为什么？
2. 哪里走了弯路？如何改进？
3. 学到了什么新的交互模式？

- [ ] 📝 学习记录 & 个人总结

### 📚 模块三扩展资源
| 资源类型 | 链接 | 说明 |
|---------|------|------|
| 练习项目 | https://github.com/codecrafters-io/build-your-own-x | 各类项目练手素材 |
| 重构案例 | https://github.com/emilybache/GildedRose-Refactoring-Kata | 经典重构练习 |
| TDD教程 | https://github.com/testdouble/contributing-tests/wiki | TDD最佳实践Wiki |
| Git工作流 | https://www.atlassian.com/git/tutorials/comparing-workflows | Git工作流比较 |
| 代码评审 | https://google.github.io/eng-practices/review/ | Google代码评审指南 |

### 🎯 模块三检查点
- 完成至少2个实战项目
- 建立个人的评价反馈习惯
- 形成自己的最佳实践清单

---

## 模块四：高级定制与专业化 (3小时)

### 4.1 Memory系统深度使用 (45分钟)
- [ ] 四种记忆类型的使用场景
- [ ] 记忆的生命周期管理
- [ ] 跨会话知识积累
- [ ] 📝 学习记录 & 个人总结

### 4.2 MCP生态系统 (1小时)
- [ ] MCP协议理解
- [ ] 常用MCP服务器（文件系统、数据库、GitHub等）
- [ ] 自定义MCP服务器开发入门
- [ ] 📝 学习记录 & 个人总结

### 4.3 自动化与CI/CD集成 (45分钟)
- [ ] 定时任务(Cron)配置
- [ ] GitHub Actions集成
- [ ] 自动化代码审查流程
- [ ] 📝 学习记录 & 个人总结

### 4.4 Agent工程师能力矩阵 (30分钟)

#### 技术能力清单
- [ ] Prompt工程
- [ ] 工具链配置
- [ ] 多Agent协调
- [ ] 安全与权限管理

#### 软技能清单
- [ ] 需求到Prompt的转化
- [ ] AI输出的批判性审查
- [ ] 人机协作效率优化

- [ ] 📝 学习记录 & 个人总结

### 📚 模块四扩展资源
| 资源类型 | 链接 | 说明 |
|---------|------|------|
| MCP规范 | https://modelcontextprotocol.io/ | MCP官方文档 |
| MCP服务器 | https://github.com/modelcontextprotocol/servers | 官方MCP服务器集合 |
| Prompt工程 | https://www.promptingguide.ai/ | Prompt工程完整指南 |
| Anthropic Cookbook | https://github.com/anthropics/anthropic-cookbook | Anthropic官方示例 |
| AI工程路线图 | https://github.com/dair-ai/AI-Engineer-Roadmap | AI工程师学习路线 |
| 视频课程 | https://www.deeplearning.ai/short-courses/ | DeepLearning.AI短课程 |

### 🎯 模块四检查点
- 能配置完整的自动化工作流
- 理解Agent工程师的能力要求
- 完成能力自评估

---

## 学习跟踪系统

### 目录结构
```
FreshClaude/
├── LEARNING_PLAN.md              # 学习计划（本文件）
├── CLAUDE.md                     # 项目配置
├── PROGRESS.md                   # 总体进度跟踪
│
├── modules/
│   ├── 01-fundamentals/
│   │   ├── README.md             # 模块概述
│   │   ├── 1.1-core-concepts/
│   │   │   ├── notes.md          # 学习笔记
│   │   │   ├── prompts.md        # 使用的提示词
│   │   │   └── reflection.md     # 个人总结
│   │   └── ...
│   ├── 02-advanced/
│   ├── 03-engineering/
│   └── 04-customization/
│
├── prompts/
│   ├── README.md                 # 提示词索引
│   ├── effective/                # 有效的提示词
│   └── ineffective/              # 无效的提示词（及原因）
│
├── projects/
│   ├── project-a-cli-todo/       # 实战项目A
│   ├── project-b-api-service/    # 实战项目B
│   └── project-c-refactoring/    # 实战项目C
│
└── evaluation/
    ├── self-assessment.md        # 自我评估
    ├── daily-reflections/        # 每日反思
    └── skill-matrix.md           # 能力矩阵跟踪
```

### 知识点记录模板
```markdown
# [知识点名称]

## 学习日期
YYYY-MM-DD

## 核心概念
（要点总结）

## 使用的Prompts
（记录实际使用的提示词）

## 实践结果
（操作结果与观察）

## 遇到的问题
（问题及解决方案）

## 个人反思
- 这个知识点改变了我什么认知？
- 我会如何在实际工作中应用？
- 还有什么疑问？

## 自评
- 理解程度：1-5
- 实践熟练度：1-5
- 能否教给别人：是/否
```

---

## 时间总览

| 模块 | 时长 | 复杂度 |
|------|------|--------|
| 模块一：基础入门 | 3小时 | ⭐⭐ |
| 模块二：进阶功能 | 6小时 | ⭐⭐⭐⭐ |
| 模块三：工程实践 | 6小时 | ⭐⭐⭐⭐ |
| 模块四：高级定制 | 3小时 | ⭐⭐⭐ |
| **总计** | **18小时** | 建议1-2周完成 |

---

## 下一步行动
1. ✅ 确认此计划
2. 创建目录结构
3. 初始化CLAUDE.md项目配置
4. 第一次commit & push
5. 开始模块一学习

---

> **核心提醒**：这不仅是学习工具，更是学习一种新的开发范式。
> 保持开放心态，记录每一次"啊哈"时刻。
