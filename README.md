# Fable Mode for Astra

中文 | [English](README.en.md)

一个面向 **GPT-6 Astra**、仅在显式调用时启用的协作 skill。它希望让你少做一层“把脑中的想法翻译成完整指令”的工作：接住上下文，让模糊想法变得可讨论，并在推进中保持你的目标与取舍。

```text
$fable-mode 我感觉这些零散记录有点关系，但还没想清楚。
```

这是一个社区项目，未获 OpenAI 官方背书。Fable 是这套协作方式的名字；安装它不会切换模型，也不代表复刻另一种模型。

## 它适合什么

- **想法尚未成形**：从已有材料提出可供辨认、修正的联系，用例子或草案帮助讨论。
- **方案需要取舍**：结合部署、维护、表达或使用场景，给出具体判断与长期选择。
- **任务持续推进**：在收到新证据和纠正后更新理解，同时保留仍然成立的目标与约束。
- **需求已经明确**：直接完成请求，不额外增加模式宣告、问卷或固定输出模板。

推断不能覆盖明确要求，也不能扩大行动授权。完整的协作取向见 [SKILL.md](fable-mode/SKILL.md)。

## 安装

需要支持本地 skills 和 `agents/openai.yaml` 调用策略的 Codex 环境。请在宿主中自行选择 GPT-6 Astra；本仓库不管理模型或账号权限。skill 本身只有 Markdown 和 YAML，无需安装 Python、Node.js 或额外 API key。

### 通过 skill-installer

在支持内置安装器的 Codex 环境中发送：

```text
$skill-installer 从 https://github.com/ycp424c/fable-mode-skill 安装 fable-mode 子目录。
```

### 手动安装（macOS / Linux）

克隆仓库后，将 **`fable-mode` 子目录**安装到个人 skills 目录。下面的检查会在同名目录或链接已存在时停止，避免覆盖已有安装：

```sh
git clone https://github.com/ycp424c/fable-mode-skill.git &&
  cd fable-mode-skill &&
  mkdir -p "$HOME/.agents/skills" &&
  test ! -e "$HOME/.agents/skills/fable-mode" &&
  test ! -L "$HOME/.agents/skills/fable-mode" &&
  cp -R fable-mode "$HOME/.agents/skills/fable-mode"
```

安装后应能找到 `~/.agents/skills/fable-mode/SKILL.md`、`agents/openai.yaml` 和 `LICENSE`。如果只希望一个项目发现它，可将完整的 `fable-mode` 文件夹放入该项目的 `.agents/skills/`；避免在多个作用域重复安装同名 skill。

Codex 支持这些本地发现路径和目录软链接。未看到新 skill 时，可重启宿主再检查技能列表。安装与发现机制见 [OpenAI 官方 skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用与退出

在请求中显式写出 `$fable-mode`，或通过宿主的技能选择器选中它。普通提及或引用这个名字不算启用。

```text
$fable-mode 这个方案有点重。我一个人维护，希望容易部署和排错。

$fable-mode 先帮我把这几条笔记串成一小段，不用确定最终用途。

$fable-mode 按刚才确认的方案修改，并完成相关验证。
```

默认作用于本次任务及其连续追问；任务结束、转向无关任务或说“结束 Fable 模式”后停止。你也可以在调用时明确指定更长的范围。

[调用配置](fable-mode/agents/openai.yaml) 将 `policy.allow_implicit_invocation` 设为布尔值 `false`。支持该字段的 Codex 不会按请求内容自动选用此 skill，显式调用仍可使用；字段含义见 [官方调用策略说明](https://learn.chatgpt.com/docs/build-skills#optional-metadata)。其他宿主是否读取此配置，需要单独验证。

## 更新与卸载

- **更新复制安装**：在源码仓库运行 `git pull --ff-only`，将原安装目录移到 skills 目录之外留作备份，再复制新的 `fable-mode` 子目录。保留你需要的本地修改，并检查调用策略仍为 `false`。
- **使用软链接开发**：仓库中的修改会直接影响安装内容。移动仓库后需要重新指向正确路径。
- **卸载**：移除已安装的 `fable-mode` 目录。如果使用软链接，只移除链接即可保留源码仓库。宿主仍显示旧条目时重启后检查。

## 评估与局限

目前有结构检查、一次本机发现记录和四个场景的独立定性试用。没有固定 Astra 模型 ID、推理设置和工具条件的多次对照实验，因此不能据此声称提升幅度或跨模型优势。静态配置检查也不能替代自动选用、退出和跨任务行为的端到端验证。

- [行为检查场景](evals/scenarios.md)：用于检查语境理解、约束保留、澄清、纠正和显式调用范围。
- [2026-09-07 验证记录](evals/validation-2026-09-07.md)：已执行内容、环境线索与未验证项。
- [设计研究与来源](research/fable-reception-2026-09-07.md)：设计线索及证据边界。

研究材料和评估文件留在仓库中，不属于需要安装的 skill 内容。

## 参与维护

欢迎通过 [Issues](https://github.com/ycp424c/fable-mode-skill/issues) 提交可复现的问题、失败场景和改进建议，中文或英文均可。贡献前请阅读 [贡献指南](CONTRIBUTING.md)和[行为准则](CODE_OF_CONDUCT.md)；敏感安全问题按[安全政策](SECURITY.md)反馈。

本地校验方法见[贡献指南](CONTRIBUTING.md)。[GitHub Actions](.github/workflows/validate.yml) 使用同一脚本检查 skill 元数据、显式调用配置、许可证副本和 GitHub YAML；它不调用模型。项目变化记录在 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

本项目的原创内容采用 [MIT License](LICENSE)。安装目录也附带[许可证副本](fable-mode/LICENSE)，便于单独分发 skill 时保留声明。研究中链接的第三方内容及相关名称、商标仍归各自权利人所有。
