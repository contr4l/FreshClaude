#!/usr/bin/env python3
"""
Claude Code 学习测验工具
从已完成模块中随机出题，测试学习效果
"""

import random
import sys

# ─── 题库 ────────────────────────────────────────────────────

QUESTIONS = {
    "1.1 核心概念": [
        {
            "q": "Claude Code 与传统 AI IDE（如 Cursor）的核心区别是什么？",
            "options": [
                "A. Claude Code 只能写 Python",
                "B. Claude Code 是「委托」模式，AI 自主规划执行",
                "C. Claude Code 不能读取文件",
                "D. Claude Code 必须联网使用",
            ],
            "answer": "B",
            "explanation": "Claude Code 采用 Native AI 模式，开发者设定目标，AI 自主规划执行路径。",
        },
        {
            "q": "Claude Code 的三层架构是什么？",
            "options": [
                "A. 前端层、后端层、数据库层",
                "B. 工具层、权限层、沙箱层",
                "C. UI层、逻辑层、网络层",
                "D. 输入层、处理层、输出层",
            ],
            "answer": "B",
            "explanation": "Claude Code 架构：工具层（执行操作）、权限层（安全控制）、沙箱层（隔离环境）。",
        },
        {
            "q": "Native AI 开发者最重要的能力转变是？",
            "options": [
                "A. 从'帮我写这段代码'到'帮我解决这个问题'",
                "B. 从 Python 转到 JavaScript",
                "C. 从本地开发转到云端开发",
                "D. 从手写代码转到复制粘贴",
            ],
            "answer": "A",
            "explanation": "核心转变：从指令式(告诉 AI 怎么做)到委托式(告诉 AI 要什么结果)。",
        },
    ],
    "1.2 基础工具链": [
        {
            "q": "在 Claude Code 中，搜索文件名应该用哪个工具？",
            "options": [
                "A. Grep",
                "B. Bash(find ...)",
                "C. Glob",
                "D. Read",
            ],
            "answer": "C",
            "explanation": "Glob 用于按文件名模式搜索，Grep 用于搜索文件内容。",
        },
        {
            "q": "以下哪种情况应该用 Edit 而不是 Write？",
            "options": [
                "A. 创建一个全新的文件",
                "B. 修改已有文件的几行代码",
                "C. 生成一份完整的配置文件",
                "D. 将内容写入空文件",
            ],
            "answer": "B",
            "explanation": "Edit 用于修改已有文件（只传 diff），Write 用于创建新文件或完全重写。",
        },
        {
            "q": "Claude Code 中可以并行调用工具的条件是？",
            "options": [
                "A. 工具调用之间有依赖关系",
                "B. 工具调用之间没有依赖关系",
                "C. 只有 Read 工具可以并行",
                "D. 任何情况都可以并行",
            ],
            "answer": "B",
            "explanation": "当多个工具调用之间没有数据依赖时，可以并行执行以提高效率。",
        },
    ],
    "1.3 内置指令": [
        {
            "q": "/compact 和 /clear 的区别是？",
            "options": [
                "A. 没有区别，都是清除上下文",
                "B. /compact 智能压缩保留关键信息，/clear 完全清除",
                "C. /clear 压缩上下文，/compact 清除上下文",
                "D. /compact 只清除代码，/clear 清除全部",
            ],
            "answer": "B",
            "explanation": "/compact 智能压缩，保留决策和结论；/clear 完全清除，从头开始。大多数情况 /compact 更好。",
        },
        {
            "q": "Claude Code 的记忆系统支持哪些类型？",
            "options": [
                "A. user, feedback, project, reference",
                "B. short-term, long-term",
                "C. code, text, image",
                "D. local, remote, cloud",
            ],
            "answer": "A",
            "explanation": "四种记忆类型：user（用户信息）、feedback（行为反馈）、project（项目状态）、reference（外部资源引用）。",
        },
        {
            "q": "在提示符中输入 ! git status 会发生什么？",
            "options": [
                "A. Claude 分析 git 状态并给建议",
                "B. 命令在终端直接执行，不经过 Claude",
                "C. 报错，不支持 ! 前缀",
                "D. Claude 用 Bash 工具执行命令",
            ],
            "answer": "B",
            "explanation": "! 前缀直接在终端执行命令，输出直接显示，适合交互式命令。",
        },
    ],
    "1.4 项目配置": [
        {
            "q": "CLAUDE.md 的黄金法则是？",
            "options": [
                "A. 写得越详细越好",
                "B. 只放你希望每次对话都生效的指令",
                "C. 必须包含完整的 API 文档",
                "D. 每次对话前手动更新",
            ],
            "answer": "B",
            "explanation": "CLAUDE.md 每次对话都会加载消耗 token，应只放静态规则，不放动态状态。",
        },
        {
            "q": "配置优先级最高的是？",
            "options": [
                "A. ~/.claude/settings.json",
                "B. 项目根目录 CLAUDE.md",
                "C. 命令行参数",
                "D. .claude/settings.json",
            ],
            "answer": "C",
            "explanation": "优先级从高到低：命令行参数 > 子目录配置 > 项目配置 > 用户配置 > 默认值。",
        },
        {
            "q": ".claudeignore 和 .gitignore 的关系是？",
            "options": [
                "A. .claudeignore 替代 .gitignore",
                "B. Claude 已自动尊重 .gitignore，.claudeignore 添加额外排除",
                "C. 两者完全独立，互不影响",
                "D. .gitignore 替代 .claudeignore",
            ],
            "answer": "B",
            "explanation": "Claude Code 默认尊重 .gitignore，.claudeignore 用于添加额外的排除规则。",
        },
    ],
    "2.1 Skills系统": [
        {
            "q": "Skill 和 CLAUDE.md 的核心区别是？",
            "options": [
                "A. Skill 每次对话都加载，CLAUDE.md 按需加载",
                "B. Skill 按需触发加载，CLAUDE.md 每次对话都加载",
                "C. 两者完全相同",
                "D. CLAUDE.md 不能包含指令",
            ],
            "answer": "B",
            "explanation": "CLAUDE.md 始终占用 token，Skill 只在触发时才加载，适合放详细流程。",
        },
        {
            "q": "Skill 自动触发的判断依据是什么？",
            "options": [
                "A. 文件名",
                "B. SKILL.md 中的 description 字段",
                "C. 文件大小",
                "D. 创建时间",
            ],
            "answer": "B",
            "explanation": "Claude 根据 SKILL.md 的 description 字段匹配用户意图，决定是否激活 Skill。",
        },
    ],
    "2.2 热门Skills": [
        {
            "q": "/commit Skill 的工作流程是？",
            "options": [
                "A. 直接执行 git commit",
                "B. 收集 git status/diff/log 上下文 → 生成 message → git add + commit",
                "C. 打开编辑器让用户写 commit message",
                "D. 只生成 commit message 不执行",
            ],
            "answer": "B",
            "explanation": "/commit 先用 ! 命令收集上下文，分析变更生成语义化 message，然后执行提交。",
        },
        {
            "q": "feature-dev Skill 共有几个阶段？",
            "options": [
                "A. 3个：设计、实现、测试",
                "B. 5个：需求、设计、实现、测试、部署",
                "C. 7个：发现、探索、澄清、架构、实现、审查、总结",
                "D. 2个：计划、执行",
            ],
            "answer": "C",
            "explanation": "feature-dev 包含完整的 7 阶段流程，每阶段都有多 Agent 协同和用户确认环节。",
        },
    ],
}


# ─── 测验逻辑 ─────────────────────────────────────────────────

def run_quiz(modules=None, count=5):
    """运行测验"""
    # 筛选模块
    available = list(QUESTIONS.keys())
    if modules:
        selected = [m for m in available if any(k in m for k in modules)]
    else:
        selected = available

    if not selected:
        print(f"未找到匹配的模块。可用模块：{', '.join(available)}")
        return

    # 收集题目
    pool = []
    for module in selected:
        for q in QUESTIONS[module]:
            pool.append((module, q))

    random.shuffle(pool)
    questions = pool[:count]

    # 开始测验
    print("\n" + "=" * 50)
    print("  Claude Code 学习测验")
    print("=" * 50)
    print(f"  模块范围：{', '.join(selected)}")
    print(f"  题目数量：{len(questions)}")
    print("=" * 50 + "\n")

    correct = 0
    total = len(questions)

    for i, (module, q) in enumerate(questions, 1):
        print(f"【第 {i}/{total} 题】[{module}]")
        print(f"  {q['q']}\n")
        for opt in q["options"]:
            print(f"    {opt}")

        while True:
            answer = input("\n  你的答案 (A/B/C/D): ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("  请输入 A、B、C 或 D")

        if answer == q["answer"]:
            correct += 1
            print(f"  ✓ 正确！")
        else:
            print(f"  ✗ 错误。正确答案是 {q['answer']}")
        print(f"  → {q['explanation']}\n")
        print("-" * 50 + "\n")

    # 评分
    score = correct / total * 100
    print("=" * 50)
    print(f"  测验结束！")
    print(f"  得分：{correct}/{total} ({score:.0f}%)")
    print()
    if score == 100:
        print("  评价：完美！你已经掌握了这些知识点。")
    elif score >= 80:
        print("  评价：优秀！大部分知识点已掌握。")
    elif score >= 60:
        print("  评价：及格。建议回顾错题对应的模块笔记。")
    else:
        print("  评价：需要加强。建议重新学习对应模块。")
    print("=" * 50 + "\n")


def print_usage():
    print("用法: python quiz.py [选项]")
    print()
    print("选项:")
    print("  -m <模块>    指定模块（如 1.1 或 2.1），可多次使用")
    print("  -n <数量>    题目数量（默认 5）")
    print("  -a           所有模块出题")
    print("  --list       列出所有可用模块")
    print()
    print("示例:")
    print("  python quiz.py                  # 随机 5 题")
    print("  python quiz.py -m 1.1 -m 1.2    # 只从 1.1 和 1.2 出题")
    print("  python quiz.py -a -n 10         # 所有模块出 10 题")
    print("  python quiz.py --list           # 列出模块和题目数量")


def main():
    modules = []
    count = 5
    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "-m" and i + 1 < len(args):
            modules.append(args[i + 1])
            i += 2
        elif args[i] == "-n" and i + 1 < len(args):
            count = int(args[i + 1])
            i += 2
        elif args[i] == "-a":
            modules = []
            i += 1
        elif args[i] == "--list":
            print("\n可用模块：")
            for mod, qs in QUESTIONS.items():
                print(f"  {mod} ({len(qs)} 题)")
            print(f"\n总计：{sum(len(qs) for qs in QUESTIONS.values())} 题")
            return
        elif args[i] in ("-h", "--help"):
            print_usage()
            return
        else:
            print(f"未知参数: {args[i]}")
            print_usage()
            return

    run_quiz(modules if modules else None, count)


if __name__ == "__main__":
    main()
