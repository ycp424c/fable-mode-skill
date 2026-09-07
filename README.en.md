# Fable Mode for Astra

[中文](README.md) | English

An explicitly invoked collaboration skill for **GPT-6 Astra**. It aims to reduce the effort of turning an unfinished thought into a complete instruction: understand the context, give vague ideas a useful shape, and preserve your goals and tradeoffs as work progresses.

```text
$fable-mode I feel these scattered notes are connected, but I haven't worked out how.
```

This is a community project, without official OpenAI endorsement. Fable names the collaboration approach. Installing the skill does not switch models or reproduce another model.

## When it helps

- **Unfinished ideas**: propose connections grounded in the available material, using examples or drafts that you can refine.
- **Tradeoffs**: offer concrete judgment based on deployment, maintenance, expression, or the intended use, including longer-term options.
- **Ongoing work**: update the approach when evidence or your corrections change, while retaining valid goals and constraints.
- **Clear requests**: complete the request directly, without adding a mode announcement, questionnaire, or fixed response template.

Inferences cannot override explicit requirements or expand permission to act. The [skill instructions](fable-mode/SKILL.md) are maintained in Chinese; you can invoke the skill with English requests. Cross-language behavior has not been separately evaluated.

## Installation

Use a Codex environment that supports local skills and the invocation policy in `agents/openai.yaml`. Select GPT-6 Astra in your host yourself; this repository does not manage models or account access. The skill consists of Markdown and YAML and requires no Python, Node.js, or additional API key.

### With skill-installer

In a Codex environment with the built-in installer, send:

```text
$skill-installer Install the fable-mode subdirectory from https://github.com/ycp424c/fable-mode-skill.
```

### Manual installation (macOS / Linux)

Install the **`fable-mode` subdirectory**, rather than the repository root. These checks stop if a directory or symlink with that name already exists:

```sh
git clone https://github.com/ycp424c/fable-mode-skill.git &&
  cd fable-mode-skill &&
  mkdir -p "$HOME/.agents/skills" &&
  test ! -e "$HOME/.agents/skills/fable-mode" &&
  test ! -L "$HOME/.agents/skills/fable-mode" &&
  cp -R fable-mode "$HOME/.agents/skills/fable-mode"
```

The installed folder should contain `SKILL.md`, `agents/openai.yaml`, and `LICENSE`. For project-scoped use, place the complete `fable-mode` folder under that project's `.agents/skills/` instead. Avoid duplicate installations across scopes.

Codex supports these local discovery paths and symlinked skill folders. If the skill does not appear, restart the host and check its skill selector. See the [official OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills).

## Usage and scope

Include `$fable-mode` explicitly in your request or select it in your host's skill selector. Merely discussing or quoting its name does not activate it.

```text
$fable-mode This plan feels heavy. I maintain it alone and want straightforward deployment and debugging.

$fable-mode Connect these notes into a short passage without deciding their final purpose yet.

$fable-mode Implement the approach we just agreed on and run the relevant checks.
```

The default scope is the current task and its follow-ups. It ends when the task finishes, you move to an unrelated task, or you say “End Fable mode.” You can explicitly request a longer scope when invoking it.

The [invocation configuration](fable-mode/agents/openai.yaml) sets `policy.allow_implicit_invocation` to the boolean `false`. Codex hosts supporting this field keep explicit invocation available while disabling automatic selection; see the [official policy reference](https://learn.chatgpt.com/docs/build-skills#optional-metadata). Other hosts need separate compatibility checks.

## Updating and uninstalling

- **Copied installation**: run `git pull --ff-only` in the source checkout, move the installed folder outside the skills directory as a backup, and copy the updated `fable-mode` folder. Preserve any local edits you need and check that the invocation policy remains `false`.
- **Symlinked development installation**: checkout changes immediately affect the installed skill. Moving the checkout requires updating the link.
- **Uninstalling**: remove the installed `fable-mode` folder. For a symlink, remove only the link to retain the checkout. Restart the host if an old entry remains visible.

## Evaluation and limitations

The repository contains structural checks, one local discovery record, and an independent qualitative trial of four scenarios. There is no repeated controlled comparison with a verified Astra model ID and fixed reasoning and tool settings. These observations do not establish a measured improvement or an advantage over another model. Static configuration checks do not verify automatic selection, exiting the mode, or behavior across tasks.

The following maintenance documents are in Chinese:

- [Behavioral scenarios](evals/scenarios.md): context, constraints, clarification, corrections, and invocation scope.
- [Validation record, 2026-09-07](evals/validation-2026-09-07.md): performed checks, environment evidence, and untested cases.
- [Design research and sources](research/fable-reception-2026-09-07.md): design inputs and evidence limits.

Research and evaluation files stay in the repository and are not part of the installed skill.

## Contributing

Reproducible problems, failure cases, and proposals are welcome through [Issues](https://github.com/ycp424c/fable-mode-skill/issues), in Chinese or English. Read the [contribution guide](CONTRIBUTING.md) (Chinese, with an English quick check) and [code of conduct](CODE_OF_CONDUCT.md). Use the [security policy](SECURITY.md) for sensitive reports.

Local validation instructions are in the contribution guide. [GitHub Actions](.github/workflows/validate.yml) runs the same script to check skill metadata, the invocation policy, license copies, and GitHub YAML, without calling a model. Changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## License

Original project content is available under the [MIT License](LICENSE). A [copy is included in the installable skill](fable-mode/LICENSE) so it accompanies standalone distribution. Linked third-party content, names, and trademarks remain with their respective owners.
