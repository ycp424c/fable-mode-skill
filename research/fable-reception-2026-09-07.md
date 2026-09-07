# Fable 社交评价与 Astra prompt 设计依据

检索与回读日期：2026-09-07。用途：为面向 GPT-6 Astra、仅显式调用的 `fable-mode` 提取可尝试的协作取向。本文件不随 skill 执行加载。

## 结论与证据边界

在可回读的样本中，用户欣赏的体验包括理解整件事的目的、维持项目语境、发现局部修补遗漏的根因，以及成为能贡献判断的讨论伙伴。同时存在越过明确要求、过度设计、投入很大却未带来更好结果的投诉。它们支持把这些行为纳入设计与验证，不能证明 Fable 在意图理解上普遍优于 Astra，更不能证明本 prompt 已复现这种差异。

本次保留八个原始讨论来源，覆盖 Reddit、LinkedIn、note 和 V2EX。它们来自定向搜索，样本偏向开发工作，并非随机抽样；同一帖里的赞同回复、跨版转载和自动摘要均不作为独立证据。没有访问评论者的运行环境，也没有复现他们的任务，因此“发言可回读”和“效果已证实”严格分开。

## 来源与采用方式

| 编号 | 原始来源与身份线索 | 可回读的评价 | 局限及设计用途 |
| --- | --- | --- | --- |
| S1 | [Dean Ahlgren 的 LinkedIn 帖子](https://www.linkedin.com/posts/dean-ahlgren_fable-5-is-back-for-a-week-anyway-then-activity-7478183663722049536-vz8W)，页面显示约两个月前 | 自述短期使用 Fable 5 后，感到它能把握整件事情及未明说的目的；用去洗车的例子说明遗漏的常识前提。 | 原 URL 经 Jina Reader 回读正文；页面标题明确标为 AI 概括，未作为作者原话。例子没有配套模型运行记录，不能当作对照实验。采用“理解情境与目的”，不把这道题写成套路。 |
| S2 | [名由 蒼真：Fable 5は何を残したか](https://note.com/nayu_souma/n/nd9d592d0a7e1)，2026-07-29 | 作者将体验概括为区分目的与手段、根据事实修正方案，并在长任务中维持目标；也承认并非总能成功。 | 已回读日文原文；先发现的英文页注明 AI 翻译，核心意思与日文核对。属于个人观察与概念文章，缺少公开实验。采用持续理解与修正，未照搬文中的台账、流程和检查点体系。 |
| S3 | [Final-Choice8412：I canceled Claude because I wanted to test Astra](https://www.reddit.com/r/ClaudeCode/comments/1w8u4jm/i_canceled_claude_because_i_wanted_to_test_astra/)；回读时为近期帖子 | 自述 Fable 5.1 更符合已有代码的约定和结构；回复中有人强调两边使用时长、记忆和工具配置可能不对等。 | 原帖与回复可回读，但缺少代码、完整提示及运行记录。采用尊重既有语境和约束；不把产品整体体验归因成基础模型能力排名。 |
| S4 | [Gru8_：Fable is damn impressive!!](https://www.reddit.com/r/codex/comments/1uoknpp/fable_is_damn_impressive/)，页面显示约两个月前 | 描述旧 Unity 游戏插件的布料快照问题，并在评论贴出涉及坐标系的诊断片段；称此前反复修补未解决。 | 有具体场景与输出片段，比纯赞叹更可检查，但没有完整工程、日志与复现步骤。本次未核实 Unity 技术结论。采用“必要时重新审视问题与假设”，不采纳耗时或跨模型胜负为事实。 |
| S5 | [ZealousidealHealth48：5.6 is just not comparable to Fable](https://www.reddit.com/r/Anthropic/comments/1uwbyow/56_is_just_not_comparable_to_fable/)，页面显示约两个月前 | 部分回复欣赏整体理解和自然讨论；另有 Nnaz123 抱怨明确要求被惯用方法覆盖，也有用户报告过度设计、漏细节或相反的模型偏好。 | 保留同一讨论中的反例，未将互相附和计作独立验证；关于模型大小、训练、降级原因的推测不采纳。用于“有判断、可修正，且明确约束不被推断覆盖”。这是 Fable 与旧 GPT 5.6 的体验，不外推为 Astra 的限制。 |
| S6 | [Dyrect_：an honest review of gpt 5.6 and fable](https://www.reddit.com/r/Anthropic/comments/1uvor7l/an_honest_review_of_gpt_56_and_fable/)，搜索索引标注 2026-07-13 | 给出相同的模糊代码审查请求，报告两者结果质量近似，而资源消耗不同。 | 提供提示原文和自报设置，但没有可复现实验材料。作为“更多工作不等于更有帮助”的反例；不把报告的计费、配额或 token 数当作当前产品事实。 |
| S7 | [Sweet-Helicopter2769：I thought I will never say this about Fable](https://www.reddit.com/r/ClaudeAI/comments/1w8h07m/i_thought_i_will_never_say_this_about_fable/)；回读时为近期帖子 | 主帖热情赞扬 Astra；wish-for-rain 的回复称会在开放式设计等没有唯一正确答案的工作上选择 Fable，同时明确表示缺少控制实验。 | 主帖缺少任务材料，证据较弱；同标题跨版帖及 TLDR 汇总去重。用于提醒偏好具有场景性，并为开放式想法成形提供设计线索，不支持统一模型排名。 |
| S8 | [blackantt：为啥 fable 5-max 有时给的方案没有 gemini 好呢？](https://www.v2ex.com/t/1237961)，平台 API 时间戳对应 2026-08-28 | 主帖质疑单次方案质量；chjqpmain 等回复要求补充需求、提示和两份方案，强调只凭结论难以判断。 | 通过 V2EX 官方公开 API 回读主帖和八条回复。主帖未提供对照材料，不能确认模型优劣；评论中的训练和服务端降级推测也未采纳。用于校准评价材料的可信程度。 |

### 未作为已核实评价采用的线索

- [ZryMiller 的 X 原帖链接](https://x.com/ZryMiller/status/2096419086171582651)仅在搜索结果及 [Zamantika 镜像](https://zamantika.com/ZryMiller/status/2096419086171582651)中出现可读转述。X 原页和 Reader 回源均失败，本机 xreach 实际调用也未认证。即使镜像内容贴合“理解未说出口的意图”，也未据此确认作者原文、日期或效果。
- 一个呈现 LinkedIn 路径、却托管在无关房地产域名的结果被排除；不沿用它的作者归属或比较结论。
- 商业 API 中转站、导购页和新闻再整理只用作发现线索，未当作独立实测。Fable 同名文档产品、研究缩写和物理学作者姓氏已排除。
- 社交页面的相对时间与搜索索引日期并不总一致。只有正文或平台 API 提供明确日期时才记录绝对日期；没有用检索时间冒充发布时间，也没有验证作者是否真人或是否存在未披露商业关系。

## 官方资料只核对产品与配置事实

- [Anthropic Fable 产品页](https://www.anthropic.com/claude/fable)：核对讨论对象为 Claude Fable，区分 Fable 5 和 5.1。厂商定位及精选客户证言不计作独立社交验证。
- [OpenAI Astra 官方指南](https://developers.openai.com/api/docs/guides/latest-model)：支持通过提示调节主动性、澄清习惯及写作方式，并提醒 Astra 对 skill 指令敏感。没有提供“隐藏意图理解”或本 skill 的效果保证。
- [OpenAI skill 文档](https://learn.chatgpt.com/docs/build-skills)：`agents/openai.yaml` 的 `policy.allow_implicit_invocation: false` 关闭隐式选用，保留显式调用。该字段不选择模型，也不使 skill 成为常驻系统提示。

## 转化为 Astra 的设计选择

这些是本次设计判断，而非从社交数据中证明的因果结论：

| 体验线索 | 写入 prompt 的取向 | 保留的自由度 |
| --- | --- | --- |
| 理解整件事，而非遗漏上下文中的目的（S1、S2） | 理解此时的请求、希望达到的结果与已成立的取舍 | 不要求先输出意图分析或把所有需求改写成正式规格 |
| 开放问题中有贡献的讨论伙伴（S5、S7） | 让模糊想法通过例子、草案和新联系变得可讨论 | 不规定方向数量，不强行收敛到唯一解释 |
| 贴合已有项目语境（S3） | 保留已确认的约定、品味与明确要求 | 上下文决定“重”“简单”等词的意思 |
| 跳出无效局部修补、持续修正方案（S2、S4） | 根据新证据调整假设，并以实际结果判断完成 | 不强制长计划、台账、检查点或额外工具 |
| 自作主张、过度设计及相反体验（S5、S6、S8） | 推断可纠正且不能覆盖明确约束；匹配探索、决策和行动语境 | 不设置僵硬的置信度阈值、追问上限或自动执行关键词 |

运行时仅保留 `SKILL.md` 与显式调用配置；不携带原帖、模型优劣宣称、其他模型路由或低能力模型的分步脚手架。示例是自行编写的语境对照，没有复刻社交帖子中的示范题。

## 验证与后续观察

结构校验与加载回读只能验证 skill 格式、发现路径及显式调用策略。行为样例可以暴露明显误解，但不能证明提升幅度。评估时应固定 Astra、上下文、工具与推理设置，对相同任务比较是否更贴近目标、是否减少不必要追问、是否尊重明确约束，并保留失败样例；无需追求回答更长或行动更多。
