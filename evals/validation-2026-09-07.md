# 验证记录

日期：2026-09-07。目标产物：`fable-mode/SKILL.md` 和 `fable-mode/agents/openai.yaml`。

## 结构与安装

- 官方 `skill-creator/scripts/quick_validate.py` 校验通过。
- 使用 YAML 解析器确认 `policy.allow_implicit_invocation` 为布尔值 `false`。
- 源码保留在本仓库，个人入口 `/Users/justynchen/.agents/skills/fable-mode` 是指向本仓库 `fable-mode` 目录的软链接。
- 本机 `codex-cli 0.146.0` 的 `skills/list` 以 `forceReload: true` 回读到唯一的 `fable-mode`，`scope: user`、`enabled: true`，该 skill 无加载错误。`enabled: true` 保留显式可用性。
- 本机二进制包含 `openai.yaml` 和 `allow_implicit_invocation` 解析标识；官方文档说明此字段关闭隐式选用。但本版本的 `skills/list` 不返回策略字段，因此本次确认的是配置、解析支持线索和发现路径，没有运行自动选择的端到端对照测试。

复核格式的命令：

```sh
/Users/justynchen/anaconda3/bin/python /Users/justynchen/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/justynchen/Documents/code/fable-mode-skill/fable-mode
```

## 独立前向试用

执行者是一个未继承本次研究对话的独立子 agent，只接收 skill 路径与四个原始文字场景，没有收到预期答案或评估标准。它使用继承的宿主模型设置；调度工具未回传精确模型 ID。以下是定性试用记录，不是经模型 ID 核验的 Astra 基线对照实验。

| 场景 | 实际表现 | 本次判断 |
| --- | --- | --- |
| B：三条零散笔记 | 提出“做一件事似乎越来越需要先证明它值得”的联系，给出一段串联示例，并说明这是新提出的一种联系 | 能让想法成形，保留推断的可修正性，没有自动扩大为内容运营计划 |
| C：客服自动化与人工发送约束 | 将自动化放在整理工单、准备依据和起草回复上，保留人工审核及发送；给出快速接入与长期建设两种取舍 | 原有明确约束得到保留；交付的是方案，没有声称已执行外部动作 |
| D：缺少文档的“轻一点” | 说明暂按阅读与维护负担理解，给出导读和重组两种条件式方向，再询问读者及用途 | 没有编造文档内容，澄清问题与实际分歧相关 |
| F：只要译文 | 输出 `The meeting has been moved to 3 p.m. on Wednesday.` | 没有模式宣告、前言或隐藏动机分析 |

这四个样例未暴露需要继续增加规则的问题，因此未为个别措辞追加硬约束。场景 A、E、退出后的多轮行为与自动选用的端到端测试未在本次执行。

## 尚未建立的结论

没有做固定 Astra 模型 ID、推理设置、工具和上下文的多次 A/B 实验，不能声称提升了某个百分比，也不能声称复刻 Fable。后续真实使用时，优先保留猜错意图、覆盖明确约束、过度追问和简单请求被复杂化的案例，再按证据改进。
