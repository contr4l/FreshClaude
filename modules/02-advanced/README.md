# 模块二：进阶功能与生态系统

## 学习目标
- 深入理解Skills系统并能自定义开发
- 掌握Hooks配置实现自动化
- 理解多Agent并行处理的业界最佳实践
- 能设计和实现复杂的Agent编排

## 预计时间
6小时

## 知识点

### 2.1 Skills系统深度剖析 (45分钟)
- Skill的本质和触发机制
- 内置Skills分类
- Skill文件结构

### 2.2 GitHub热门Skills实操 (1.5小时)
- 开发效率：commit, pr-review, refactor
- 代码质量：test-gen, doc-gen
- 项目管理：changelog, issue-triage

### 2.3 自定义Skill开发 (1小时)
- Frontmatter配置
- 触发条件设计
- 实战开发

### 2.4 Hooks系统精通 (1小时)
- 执行时机与生命周期
- PreToolCall / PostToolCall
- 实战：自动格式化、安全检查

### 2.5 Agent并行处理 (1.5小时)
- 理论：多Agent架构模式
- 实践：Map-Reduce、Pipeline、Swarm、Supervisor
- 最佳实践：决策框架、prompt设计、结果聚合

## 检查点
完成本模块后，你应该能够：
- [ ] 创建符合规范的自定义Skill
- [ ] 配置实用的Hooks实现自动化
- [ ] 选择合适的Agent并行模式
- [ ] 设计子Agent的prompt

## 扩展资源
- [Skills集合](https://github.com/anthropics/claude-code-skills)
- [Agent SDK](https://github.com/anthropics/claude-agent-sdk)
- [MetaGPT论文](https://arxiv.org/abs/2308.08155)
- [OpenAI Swarm](https://github.com/openai/swarm)
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [LangGraph](https://github.com/langchain-ai/langgraph)
