#!/usr/bin/env python3
"""
NVIDIA Alfred Portal 自动化脚本
用于登录 http://dev.alfred.nvidia.com 并执行常见操作

使用方法:
    1. 安装依赖: pip install playwright && playwright install chromium
    2. 首次运行会打开浏览器让你手动完成SSO登录
    3. 登录状态会保存，后续运行可自动跳过登录

作者: 由 Claude Code 协助创建
日期: 2026-04-08
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright, Browser, Page

# 配置
ALFRED_URL = "http://dev.alfred.nvidia.com"
USER_DATA_DIR = Path(__file__).parent / ".browser_data"  # 保存登录状态


class AlfredAutomation:
    """Alfred Portal 自动化操作类"""

    def __init__(self):
        self.browser: Browser = None
        self.page: Page = None
        self.playwright = None

    async def start(self, headless: bool = False):
        """
        启动浏览器

        Args:
            headless: 是否无头模式（SSO登录时建议False，以便手动操作）
        """
        self.playwright = await async_playwright().start()

        # 使用持久化上下文保存登录状态
        self.browser = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=headless,
            # 模拟真实浏览器
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )

        self.page = self.browser.pages[0] if self.browser.pages else await self.browser.new_page()
        print("✓ 浏览器已启动")

    async def login(self, wait_for_manual_sso: bool = True):
        """
        登录 Alfred Portal

        SSO登录通常需要手动完成（2FA、证书等），
        脚本会等待你完成登录后继续。
        """
        print(f"→ 正在访问 {ALFRED_URL}")
        await self.page.goto(ALFRED_URL)

        # 检查是否已经登录
        if await self._is_logged_in():
            print("✓ 已检测到登录状态，跳过登录")
            return True

        if wait_for_manual_sso:
            print("\n" + "="*50)
            print("请在浏览器中完成 SSO 登录")
            print("登录完成后，脚本会自动继续...")
            print("="*50 + "\n")

            # 等待登录完成（检测URL变化或特定元素出现）
            # TODO: 根据实际页面结构调整检测逻辑
            await self._wait_for_login()

        return await self._is_logged_in()

    async def _is_logged_in(self) -> bool:
        """
        检查是否已登录

        TODO: 根据实际页面调整判断逻辑
        可能的判断方式：
        - 检查URL是否不再是登录页
        - 检查是否存在用户头像/用户名元素
        - 检查是否存在登出按钮
        """
        current_url = self.page.url

        # 示例：如果URL包含login/sso等，说明还在登录流程中
        login_indicators = ['login', 'sso', 'auth', 'signin']
        is_on_login_page = any(ind in current_url.lower() for ind in login_indicators)

        return not is_on_login_page

    async def _wait_for_login(self, timeout: int = 300):
        """等待用户完成登录，最多等待timeout秒"""
        import time
        start = time.time()

        while time.time() - start < timeout:
            if await self._is_logged_in():
                print("✓ 登录成功！")
                return
            await asyncio.sleep(2)  # 每2秒检查一次

        raise TimeoutError("登录超时，请检查网络或重试")

    # ==================== 业务操作 ====================

    async def navigate_to(self, path: str):
        """
        导航到指定页面

        Args:
            path: 相对路径，如 "/vehicles" 或 "/bench/firmware"
        """
        url = f"{ALFRED_URL.rstrip('/')}/{path.lstrip('/')}"
        print(f"→ 导航到: {url}")
        await self.page.goto(url)
        await self.page.wait_for_load_state("networkidle")

    async def book_vehicle(self, vehicle_id: str = None):
        """
        订车操作

        TODO: 根据实际页面结构实现
        """
        print("→ 开始订车流程...")

        # 示例流程（需要根据实际页面调整）
        # 1. 导航到订车页面
        # await self.navigate_to("/vehicles/book")

        # 2. 选择车辆
        # if vehicle_id:
        #     await self.page.click(f'[data-vehicle-id="{vehicle_id}"]')

        # 3. 填写表单
        # await self.page.fill('#date-picker', '2026-04-10')

        # 4. 提交
        # await self.page.click('button[type="submit"]')

        print("⚠️ 订车功能待实现 - 请根据实际页面结构补充代码")

    async def update_bench_firmware(self, bench_id: str, firmware_version: str = None):
        """
        更新 Bench 固件

        TODO: 根据实际页面结构实现
        """
        print(f"→ 开始更新 Bench {bench_id} 固件...")

        # 示例流程（需要根据实际页面调整）
        # 1. 导航到bench管理页面
        # await self.navigate_to(f"/bench/{bench_id}/firmware")

        # 2. 选择固件版本
        # if firmware_version:
        #     await self.page.select_option('#firmware-select', firmware_version)

        # 3. 确认更新
        # await self.page.click('#update-firmware-btn')

        # 4. 等待完成
        # await self.page.wait_for_selector('.update-complete', timeout=60000)

        print("⚠️ 固件更新功能待实现 - 请根据实际页面结构补充代码")

    async def take_screenshot(self, name: str = "screenshot"):
        """截图保存当前页面"""
        path = Path(__file__).parent / f"{name}.png"
        await self.page.screenshot(path=str(path))
        print(f"✓ 截图已保存: {path}")

    async def close(self):
        """关闭浏览器"""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        print("✓ 浏览器已关闭")


# ==================== 使用示例 ====================

async def main():
    """主函数 - 演示基本用法"""
    alfred = AlfredAutomation()

    try:
        # 1. 启动浏览器（非无头模式，以便手动SSO登录）
        await alfred.start(headless=False)

        # 2. 登录
        logged_in = await alfred.login(wait_for_manual_sso=True)

        if not logged_in:
            print("✗ 登录失败")
            return

        # 3. 截图确认登录成功
        await alfred.take_screenshot("after_login")

        # 4. 执行操作（取消注释你需要的操作）
        # await alfred.book_vehicle("vehicle-001")
        # await alfred.update_bench_firmware("bench-042", "v2.1.0")

        # 5. 保持浏览器打开，等待用户手动关闭
        print("\n浏览器保持打开状态，你可以手动操作")
        print("按 Ctrl+C 退出脚本...")

        # 无限等待，直到用户中断
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("\n用户中断")
    finally:
        await alfred.close()


if __name__ == "__main__":
    asyncio.run(main())
