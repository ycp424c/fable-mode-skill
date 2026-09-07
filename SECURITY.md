# 安全政策 / Security Policy

## 范围与维护

本项目提供协作提示与配置，不运行服务，也不在 skill 内包含联网、凭证读取或安装脚本。宿主仍可能为用户的任务调用工具；模型实际可访问的数据和操作权限由宿主、工具及用户授权决定。提示词不是安全隔离机制。

安全修复优先进入 `main`，历史提交不单独维护。报告问题时请提供受影响的提交、宿主版本、模型信息和最小复现。运行维护校验所用的 Python 依赖不属于 skill 运行依赖。

可能需要敏感反馈的问题包括诱导未授权操作、泄露私人信息的指令变化，以及安装或维护配置被植入恶意行为。一般回答质量、语气或安装疑问可以使用普通 Issue，并先移除敏感材料。

## 如何报告

1. 查看仓库的 [Security Advisories](https://github.com/ycp424c/fable-mode-skill/security/advisories)。如果显示 **Report a vulnerability**，可通过该入口私密提交。
2. 如果没有私密报告入口，请[创建一个仅请求安全联系渠道的 Issue](https://github.com/ycp424c/fable-mode-skill/issues/new)，由维护者 [@ycp424c](https://github.com/ycp424c) 提供后续私密联系方法。公开内容只写联系请求，不附漏洞细节、利用步骤、密钥或私人数据。
3. 建立私密渠道后，提供影响、受影响文件及版本、经过脱敏的最小复现和预期行为。请只使用自己有权测试的数据与环境。

`SECURITY.md` 本身不会启用 GitHub 私密漏洞报告功能；入口取决于仓库设置，参见 [GitHub 官方报告说明](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately)。

维护者会根据可复现信息确认影响、准备修复并协商披露。项目按维护者可用时间处理，不承诺固定响应或修复时限。

## English

This project ships instructions and configuration, with no runtime service or skill scripts for networking, credential access, or installation. A host may still use tools for the user's task. Instructions are not a security boundary; access depends on the host, tools, and user authorization. Maintenance dependencies are not runtime requirements for the skill.

Security fixes target `main`; historical commits are not separately maintained. Report the affected commit, host version, model details, impact, and a sanitized minimal reproduction. Routine quality and installation issues can use public Issues after removing sensitive material.

For sensitive reports, use **Report a vulnerability** on the repository's [advisories page](https://github.com/ycp424c/fable-mode-skill/security/advisories) if available. If private reporting is unavailable, [open an issue asking only for a security contact](https://github.com/ycp424c/fable-mode-skill/issues/new). Do not include vulnerability details, exploit steps, credentials, or private data until a private channel is agreed with [@ycp424c](https://github.com/ycp424c).

Adding this file does not enable private reporting. Reports are handled as maintainer time permits, without a fixed response or resolution deadline. The maintainer will use reproducible evidence to assess impact and coordinate a fix and disclosure.
