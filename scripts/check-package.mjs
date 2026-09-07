import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const manifest = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));
const expected = [
  'LICENSE',
  'README.en.md',
  'README.md',
  'fable-mode/LICENSE',
  'fable-mode/SKILL.md',
  'fable-mode/agents/openai.yaml',
  'package.json',
].sort();

assert.equal(manifest.name, 'fable-mode-skill');
assert.equal(manifest.license, 'MIT');
assert.equal(manifest.publishConfig.registry, 'https://registry.npmjs.org/');
assert.equal(manifest.publishConfig.access, 'public');

// npm supplies its JS entry point when running this script, including on Windows.
const npmExecPath = process.env.npm_execpath;
assert.ok(npmExecPath, 'Run this check with npm run check:package.');
const result = spawnSync(
  process.execPath,
  [npmExecPath, 'pack', '--dry-run', '--json', '--ignore-scripts'],
  { cwd: root, encoding: 'utf8' },
);
if (result.error) throw result.error;
assert.equal(result.status, 0, result.stderr || 'npm pack failed');
const packages = JSON.parse(result.stdout);
assert.equal(packages.length, 1, 'Expected one publishable package');
const [packed] = packages;
assert.equal(packed.name, manifest.name);
assert.equal(packed.version, manifest.version);
assert.deepEqual(
  packed.files.map((file) => file.path).sort(),
  expected,
  'The npm archive must contain only the complete skill, READMEs, licenses, and package metadata.',
);
assert.equal(
  readFileSync(new URL('../LICENSE', import.meta.url), 'utf8'),
  readFileSync(new URL('../fable-mode/LICENSE', import.meta.url), 'utf8'),
  'The installable skill must carry the same license as the package.',
);
console.log(`${packed.name}@${packed.version}: ${expected.length} files, ${packed.size} bytes packed.`);
