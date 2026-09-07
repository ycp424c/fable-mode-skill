# Fable Mode for Astra

[中文](README.md) | English

**You shouldn't have to explain yourself so precisely every time.**

Fable Mode is an explicitly invoked skill for everyday collaboration with **GPT-6 Astra**. It aims to let you speak naturally: bring an unfinished thought, a passing impression, or an incomplete request, and let the model use the context to understand more of what you mean.

```text
$fable-mode I don't feel like weighing this up anymore. Pick one for me based on what we just discussed.
```

## Why I made this skill

The starting point is simple: **I'm willing to trade some performance for an easier everyday experience.**

Using AI can be tiring when every message requires organizing the background, choosing precise wording, listing all the conditions, and explaining again what you actually want. Sometimes you just want to talk something through, revise a paragraph, or make a small decision. The idea can become clearer as the conversation goes.

I want the model to take on more of the work of understanding and weighing things up: carry forward context we've already discussed, handle small decisions it has enough information to make, and ask when uncertainty would materially change the direction. If it gets something wrong, a brief correction should be enough to continue.

For that experience, I'm willing to accept tradeoffs in speed, resource use, or the best possible performance on some tasks. What matters is whether a stretch of real, everyday use takes less effort from me. This is a design preference; the performance costs and experience gains have not been measured.

This is a community project, without official OpenAI endorsement. Fable names the collaboration approach. Installing the skill does not switch models or reproduce another model.

## How it should feel

- **Less repeated background**: carry forward preferences, conditions, and tradeoffs already discussed.
- **Fewer small decisions sent back to you**: when the context is sufficient and a detail is easy to change, offer something useful to work with.
- **Room for unfinished ideas**: use examples, drafts, and conversation to find a direction before you have a complete plan.
- **Easy corrections**: when you say “That's not what I meant,” update the understanding and continue with what still applies.
- **Direct help with simple requests**: give a one-line answer when that's enough, treating reading and decision effort as part of the experience.

Your requirements for the current task still take priority, including speed, length, and the accuracy it needs. Inferences cannot override explicit requirements or expand permission to act. The [skill instructions](fable-mode/SKILL.md) are maintained in Chinese; you can invoke the skill with English requests. Cross-language behavior has not been separately evaluated.

## Installation

Use a Codex environment that supports local skills and the invocation policy in `agents/openai.yaml`. Select GPT-6 Astra in your host yourself; this repository does not manage models or account access. The skill consists of Markdown and YAML, with no runtime dependencies or additional API key. The npm / npx installation methods below require Node.js.

### With npx skills (recommended)

Run this from the project where you want to use the skill:

```sh
npx skills add ycp424c/fable-mode-skill --skill fable-mode --agent codex
```

This installs into the current project. Add `-g` for a personal installation or `-y` to skip interactive confirmation. Check any local edits to an existing skill first, as the installer may overwrite it.

This command fetches the GitHub source; installing this project's npm package first is unnecessary. The syntax was checked against [skills CLI](https://github.com/vercel-labs/skills#readme) `1.5.24`, which requires Node.js `>=22.20.0`.

### Install a fixed version from npm

[fable-mode-skill](https://www.npmjs.com/package/fable-mode-skill) distributes versioned skill files. To manage the version as a project dependency:

```sh
npm install --save-dev --save-exact fable-mode-skill@0.1.0
npx skills add ./node_modules/fable-mode-skill --skill fable-mode --agent codex
```

The npm command downloads the files; the second command installs the skill into Codex's discovery directory. The package includes the complete `agents/openai.yaml` and MIT license, with no automatic installation scripts. The current skills CLI accepts the repository or local path above, rather than resolving a plain npm package name.

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

With the earlier conversation as context, you could say:

```text
$fable-mode This still sounds a bit stiff. Make it sound more like something I'd actually say.

$fable-mode Connect these notes into a short passage without deciding their final purpose yet.

$fable-mode Ease of maintenance matters more to me after all. Help me choose on that basis.
```

The default scope is the current task and its follow-ups. It ends when the task finishes, you move to an unrelated task, or you say “End Fable mode.” You can explicitly request a longer scope when invoking it.

The [invocation configuration](fable-mode/agents/openai.yaml) sets `policy.allow_implicit_invocation` to the boolean `false`. Codex hosts supporting this field keep explicit invocation available while disabling automatic selection; see the [official policy reference](https://learn.chatgpt.com/docs/build-skills#optional-metadata). Other hosts need separate compatibility checks.

## Updating and uninstalling

- **skills CLI installation**: update a GitHub installation with `npx skills update fable-mode`, or remove it with `npx skills remove fable-mode --agent codex`; add `-g` when removing a personal installation. For a fixed npm version, update the npm dependency and repeat `skills add` with the local path.
- **Copied installation**: run `git pull --ff-only` in the source checkout, move the installed folder outside the skills directory as a backup, and copy the updated `fable-mode` folder. Preserve any local edits you need and check that the invocation policy remains `false`.
- **Symlinked development installation**: checkout changes immediately affect the installed skill. Moving the checkout requires updating the link.
- **Uninstalling**: remove the installed `fable-mode` folder. For a symlink, remove only the link to retain the checkout. Restart the host if an old entry remains visible.

## Evaluation and limitations

The initial version has structural checks, one local discovery record, and an independent qualitative trial of four scenarios. Those records predate this change in everyday-experience priorities and do not directly establish its effects. There is no repeated controlled comparison with a verified Astra model ID and fixed reasoning and tool settings. These observations do not establish a measured improvement or an advantage over another model. Static configuration checks do not verify automatic selection, exiting the mode, or behavior across tasks.

Further trials should examine repeated background, unnecessary confirmation, the effort needed to correct misunderstandings, and whether results still meet the task's requirements, alongside time and resource use. Relevant scenarios have been added, but this revision has not yet had a new independent behavioral trial.

The following maintenance documents are in Chinese:

- [Behavioral scenarios](evals/scenarios.md): context, constraints, clarification, corrections, and invocation scope.
- [Validation record, 2026-09-07](evals/validation-2026-09-07.md): performed checks, environment evidence, and untested cases.
- [Design research and sources](research/fable-reception-2026-09-07.md): design inputs and evidence limits.

Research and evaluation files stay in the repository and are not part of the installed skill.

## Contributing

Reproducible problems, failure cases, and proposals are welcome through [Issues](https://github.com/ycp424c/fable-mode-skill/issues), in Chinese or English. Read the [contribution guide](CONTRIBUTING.md) (Chinese, with an English quick check) and [code of conduct](CODE_OF_CONDUCT.md). Use the [security policy](SECURITY.md) for sensitive reports.

Local validation instructions are in the contribution guide. [GitHub Actions](.github/workflows/validate.yml) checks skill metadata, the invocation policy, license copies, GitHub YAML, and the npm package file list, without calling a model. Changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## License

Original project content is available under the [MIT License](LICENSE). A [copy is included in the installable skill](fable-mode/LICENSE) so it accompanies standalone distribution. Linked third-party content, names, and trademarks remain with their respective owners.
