# Alfred Portal 自动化脚本

这是一个用于演示 "委托式开发" 的示例项目。

## 背景

**用户的原始 Prompt**:
```
创建一个脚本，它可以在我的电脑上登陆 http://dev.alfred.nvidia.com
SSO登陆，浏览器自动化，登陆后我可能要访问相关页面完成订车或者是更新某些bench的固件的操作
```

## Claude Code 的处理方式

1. **理解目标**：自动化登录内部系统，执行业务操作
2. **技术选型**：Playwright（现代浏览器自动化库）
3. **架构设计**：模块化类结构，便于扩展
4. **务实考虑**：
   - SSO登录需要手动介入（2FA/证书）
   - 业务逻辑留下框架，需根据实际页面补充
   - 保存登录状态，避免重复登录

## 安装

```bash
# 安装 Playwright
pip install playwright

# 安装浏览器（首次运行需要）
playwright install chromium
```

## 使用

```bash
# 运行脚本
python alfred_automation.py
```

首次运行会打开浏览器，需要手动完成 SSO 登录。登录状态会保存在 `.browser_data/` 目录。

## 扩展

要添加新的自动化操作：

1. 在 `AlfredAutomation` 类中添加新方法
2. 使用 `self.page` 与页面交互
3. 常用操作：
   - `await self.page.goto(url)` - 导航
   - `await self.page.click(selector)` - 点击
   - `await self.page.fill(selector, text)` - 填写表单
   - `await self.page.wait_for_selector(selector)` - 等待元素

## 学习要点

这个示例展示了 **委托式开发** 的特点：

| 方面 | 说明 |
|------|------|
| 用户输入 | 目标 + 约束，而非具体步骤 |
| Claude 输出 | 完整可运行的项目结构 |
| 迭代空间 | 框架先行，细节后续填充 |
| 实用性 | 考虑了真实场景（SSO、状态保存） |

## 后续迭代

用户可以继续委托：
- "帮我实现订车功能，页面结构是这样的..."
- "添加命令行参数支持"
- "加入错误重试机制"
