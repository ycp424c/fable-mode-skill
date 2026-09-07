# Fable Mode for Astra

中文 | [English](README.en.md)

**不用每次都把自己解释得那么清楚。**

Fable Mode 是一个面向 **GPT-6 Astra**、仅在显式调用时启用的日常协作 skill。希望你能自然地说话，把还没组织好的想法、随口一句感受或一个不完整的请求交给它，让它结合上下文多理解一些。

```text
$fable-mode 今天不想再纠结了，按刚才聊的帮我挑一个吧。
```

## 为什么做这个 skill

我的出发点很简单：**愿意牺牲一些性能，换更好的日常使用体验。**

日常用 AI，如果每次都得整理背景、精确措辞、补全条件，再反复解释自己到底想要什么，也挺累的。有时候只是想聊两句、改一段话、拿个主意，想法本来就可以边聊边清楚。

我希望模型多承担一些理解和权衡的工作：从已经聊过的内容里接住省略的信息，能判断的小事先帮我处理，拿不准又会影响方向的地方再问。即使理解偏了，也能通过一句纠正接着往下走。

为了这样的体验，我可以接受在速度、资源消耗，或某些任务的极致表现上做一些取舍。是否值得，最终看一段真实的日常使用中，自己是不是少费了心。这是项目的设计取向，具体的性能代价和体验收益还没有经过量化验证。

这是一个社区项目，未获 OpenAI 官方背书。Fable 是这套协作方式的名字；安装它不会切换模型，也不代表复刻另一种模型。

## 希望用起来是什么感觉

- **少重复背景**：已经说过的偏好、条件和取舍，后续能接着用。
- **少为小事来回确认**：上下文足够、容易调整的细节，先拿出一个有帮助的结果。
- **想法可以边聊边成形**：不必先有完整方案，也能用例子、草案和讨论找到方向。
- **纠正起来不费劲**：你说“不是这个意思”，它就更新理解，保留仍然有效的部分继续。
- **简单的事直接处理**：该给一句答案时就给一句，把阅读和决策负担也算进体验。

具体任务仍以你当下的要求为准，包括速度、篇幅和所需的准确性。推断不能覆盖明确要求，也不能扩大行动授权。完整的协作取向见 [SKILL.md](fable-mode/SKILL.md)。

## 安装

需要支持本地 skills 和 `agents/openai.yaml` 调用策略的 Codex 环境。请在宿主中自行选择 GPT-6 Astra；本仓库不管理模型或账号权限。skill 本身只有 Markdown 和 YAML，没有运行依赖或额外 API key；下面的 npm / npx 安装方式需要 Node.js。

### 通过 npx skills（推荐）

在要使用 skill 的项目目录运行：

```sh
npx skills add ycp424c/fable-mode-skill --skill fable-mode --agent codex
```

默认安装到当前项目；加 `-g` 安装到个人目录，加 `-y` 跳过交互确认。安装前请检查同名 skill 的本地修改，安装器可能覆盖已有安装。

此命令从 GitHub 获取源码，不需要先安装本项目的 npm 包。命令已按 [skills CLI](https://github.com/vercel-labs/skills#readme) `1.5.24` 核对，该版本要求 Node.js `>=22.20.0`。

### 从 npm 安装固定版本

[fable-mode-skill](https://www.npmjs.com/package/fable-mode-skill) 提供可固定版本的 skill 文件包。需要用项目依赖管理版本时运行：

```sh
npm install --save-dev --save-exact fable-mode-skill@0.1.0
npx skills add ./node_modules/fable-mode-skill --skill fable-mode --agent codex
```

npm 安装只下载文件，第二条命令将 skill 安装到 Codex 的发现目录。包中附带完整的 `agents/openai.yaml` 与 MIT 许可证，没有自动安装脚本。当前 `skills` CLI 接受上述仓库或本地路径，不直接解析普通 npm 包名。

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

沿用已经聊过的上下文，你可以这样说：

```text
$fable-mode 这版还是有点端着，改得像我平时会说的话。

$fable-mode 先帮我把这几条笔记串成一小段，不用确定最终用途。

$fable-mode 我还是更在意后面好不好维护，你按这个帮我选吧。
```

默认作用于本次任务及其连续追问；任务结束、转向无关任务或说“结束 Fable 模式”后停止。你也可以在调用时明确指定更长的范围。

[调用配置](fable-mode/agents/openai.yaml) 将 `policy.allow_implicit_invocation` 设为布尔值 `false`。支持该字段的 Codex 不会按请求内容自动选用此 skill，显式调用仍可使用；字段含义见 [官方调用策略说明](https://learn.chatgpt.com/docs/build-skills#optional-metadata)。其他宿主是否读取此配置，需要单独验证。

## 更新与卸载

- **skills CLI 安装**：可用 `npx skills update fable-mode` 更新 GitHub 来源的安装，用 `npx skills remove fable-mode --agent codex` 移除；个人安装移除时加 `-g`。从 npm 固定版本安装时，先更新 npm 依赖版本，再重新执行本地路径的 `skills add` 命令。
- **更新复制安装**：在源码仓库运行 `git pull --ff-only`，将原安装目录移到 skills 目录之外留作备份，再复制新的 `fable-mode` 子目录。保留你需要的本地修改，并检查调用策略仍为 `false`。
- **使用软链接开发**：仓库中的修改会直接影响安装内容。移动仓库后需要重新指向正确路径。
- **卸载**：移除已安装的 `fable-mode` 目录。如果使用软链接，只移除链接即可保留源码仓库。宿主仍显示旧条目时重启后检查。

## 评估与局限

初版有结构检查、一次本机发现记录和四个场景的独立定性试用；这些记录早于本次日常体验优先级的调整，不能直接证明调整后的效果。没有固定 Astra 模型 ID、推理设置和工具条件的多次对照实验，因此不能据此声称提升幅度或跨模型优势。静态配置检查也不能替代自动选用、退出和跨任务行为的端到端验证。

后续试用会重点观察用户需要重复多少背景、做多少次不必要的确认、花多少力气纠正误解，以及任务结果是否仍符合要求，同时记录耗时和资源消耗。当前已补充相关场景，尚未对这次调整运行新的独立行为试用。

- [行为检查场景](evals/scenarios.md)：用于检查语境理解、约束保留、澄清、纠正和显式调用范围。
- [2026-09-07 验证记录](evals/validation-2026-09-07.md)：已执行内容、环境线索与未验证项。
- [设计研究与来源](research/fable-reception-2026-09-07.md)：设计线索及证据边界。

研究材料和评估文件留在仓库中，不属于需要安装的 skill 内容。

## 参与维护

欢迎通过 [Issues](https://github.com/ycp424c/fable-mode-skill/issues) 提交可复现的问题、失败场景和改进建议，中文或英文均可。贡献前请阅读 [贡献指南](CONTRIBUTING.md)和[行为准则](CODE_OF_CONDUCT.md)；敏感安全问题按[安全政策](SECURITY.md)反馈。

本地校验方法见[贡献指南](CONTRIBUTING.md)。[GitHub Actions](.github/workflows/validate.yml) 检查 skill 元数据、显式调用配置、许可证副本、GitHub YAML 和 npm 发布文件清单；它不调用模型。项目变化记录在 [CHANGELOG.md](CHANGELOG.md)。

## 许可证

本项目的原创内容采用 [MIT License](LICENSE)。安装目录也附带[许可证副本](fable-mode/LICENSE)，便于单独分发 skill 时保留声明。研究中链接的第三方内容及相关名称、商标仍归各自权利人所有。
