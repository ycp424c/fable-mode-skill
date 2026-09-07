# 贡献指南 / Contributing

感谢你帮助改进 Fable Mode。问题、Pull Request 和讨论可以使用中文或英文。参与本项目时请遵守[行为准则](CODE_OF_CONDUCT.md)。

## 适合提交什么

- 可复现的失败场景：误判意图、覆盖明确约束、过度追问、把简单请求复杂化，或退出后仍延续模式。
- 安装说明、兼容性记录、翻译和文档修正。
- 有场景或证据支撑的 skill 改进，以及评估方法的改进。

较大方向调整建议先开 Issue 讨论，说明它解决什么问题、当前成本和长期维护收益。只修文字或链接可以直接提交 PR。

## 项目约定

`fable-mode/` 是可安装内容，包含 skill 正文、调用策略和许可证。`evals/`、`research/` 和 `scripts/` 服务于维护，不随 skill 安装。

维护时保留以下设计意图：

- 仅在显式调用时启用；`allow_implicit_invocation` 保持布尔值 `false`。
- 推断可以帮助补全语境，不能覆盖用户的明确要求或扩大行动授权。
- 简单请求直接完成；不因少数失败样例无限追加固定流程或模板。
- 研究、试用和已验证结论应清楚区分。不要把社区评价写成模型排名或未经验证的效果承诺。

## 本地检查

从仓库根目录执行。维护脚本需要 Python 3.10 或更高版本和 [requirements-dev.txt](requirements-dev.txt) 中的依赖；这些不是使用 skill 的依赖。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
git diff --check
```

Windows 可使用 `python -m venv .venv`，并将后续的 `.venv/bin/python` 替换为 `.venv\Scripts\python.exe`。

校验脚本检查元数据、显式调用配置、两份许可证一致性及 GitHub YAML 格式。它不调用模型，不检查远端链接，也不证明行为效果。[CI](.github/workflows/validate.yml) 在 Python 3.12 上执行同一检查。

修改 `LICENSE` 时同步更新 `fable-mode/LICENSE`，保证只下载 skill 子目录的使用者也能收到完整声明。

## npm 打包与发布

仓库根目录的 `package.json` 描述 npm 分发包；`fable-mode/` 仍是唯一的 skill 源码。发布文件使用白名单，保持无运行依赖和自动安装脚本。修改打包配置时，用 Node.js 和 npm 执行：

```sh
npm run check:package
npm pack --dry-run
```

检查会确认完整的 skill、调用策略、许可证和两份 README 都进入包中，并拒绝额外文件。开发环境、研究与维护工具不随 npm 包发布。该检查也在 CI 和 `prepublishOnly` 中执行，无需先运行 `npm install`。

首次发布前，按 [npm 的双重验证说明](https://docs.npmjs.com/configuring-two-factor-authentication/) 在账号设置中启用 2FA，再通过 `npm login --registry=https://registry.npmjs.org/` 登录。仅有普通登录不足以发布；发布命令提示验证时，在浏览器中完成验证。

维护者发布时先更新实际版本和变更记录，完成上述检查及临时项目中的 `skills add` 安装验证，再执行 `npm publish --access public`。发布后回读 `npm view fable-mode-skill version dist-tags --json`，确认 registry 中的版本，再下载该版本验证安装。Git 标签应在发布成功后创建，避免把失败的发布标成已经可用。

## 行为改动如何验证

修改协作取向或启用范围时，按 [evals/scenarios.md](evals/scenarios.md) 选择受影响的场景，并检查明确请求和显式调用范围是否退化。纯文档和许可证整理不需要重新运行模型试用。

行为验证记录应包含：

1. 对应的提交或 diff、宿主及版本、模型 ID、推理设置、工具条件；无法确认的字段写“未知”。
2. 经过脱敏的上下文与原始请求，以及实际回复或必要片段。
3. 预期行为、观察到的结果和判断依据，包括失败样例。
4. 实际未执行的场景和限制。格式通过、宿主发现和行为符合预期是不同证据。

新增记录放在 `evals/validation-YYYY-MM-DD.md`，同日多次可加描述性后缀。历史记录保留当时的环境和限制，后续结果另行补充，不把旧试用改写成新结论。引用外部材料请附原始来源，概括其局限，避免复制不必要的长段原文或私人对话。

## 提交 Pull Request

1. Fork 仓库，从最新 `main` 创建用途明确的分支。
2. 聚焦一个可解释的问题，并同步受影响的中英 README、场景或变更记录。
3. 完成本地检查，在 PR 中写明问题、修改后的行为、验证结果和剩余限制。

提交信息建议使用 `docs:`、`fix:`、`feat:` 或 `chore:` 等简明前缀。AI 辅助贡献与其他贡献接受相同的审查：请检查最终内容，并确保你有权提交。贡献的原创内容按本项目 [MIT License](LICENSE) 提供。

敏感安全问题请按 [SECURITY.md](SECURITY.md) 反馈，不在公开 Issue 或 PR 中粘贴利用细节、密钥或未脱敏材料。

## English quick check

Chinese and English contributions are welcome. Keep changes focused, preserve explicit invocation and user constraints, and include reproducible evidence for behavior changes. Use Python 3.10+ and the commands above for static validation; on Windows, use `.venv\Scripts\python.exe`.

Update both READMEs when relevant. Behavioral changes need selected scenarios from `evals/scenarios.md`, recording the actual host, model settings, inputs, outputs, and limitations. Documentation-only changes do not require model trials. Contributions are provided under the MIT License; report sensitive issues through the security policy.
