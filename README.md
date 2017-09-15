# check-grgen

[pre-commit][pc] hook to validate grgen files.

You have to have a file named "Rules.grg" in the same directory otherwise it can't check .gm .grs etc..

## Usage

### pre-commit

Add the following entry to `.pre-commit-config.yaml`:

```yaml
- repo: git://github.com/balrok/check-grgen
  sha: master
  hooks:
  - id: check-grgen
```

Alternatively, since the checks take quite a while, you can install this hook only for push
```yaml
- repo: git://github.com/balrok/check-grgen
  sha: master
  hooks:
  - id: check-grgen
    stages: [push]
```
and `pre-commit install -t pre-push`

Options:

* `-x PATTERN, --exclude PATTERN` filename patterns to exclude from validation.

[pc]: http://pre-commit.com
