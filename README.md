# Python Template for Claude Code (Cookiecutter)

Claude Codeでの開発に最適化されたPythonプロジェクトテンプレートです。Cookiecutterを使用して、カスタマイズ可能なプロジェクト構造を提供します。

> 💡 このテンプレートは [discus0434さんのpython-template-for-claude-code](https://github.com/discus0434/python-template-for-claude-code) をベースに、Cookiecutter対応とカスタマイズ機能を追加したものです。

## 特徴

- 🚀 **Claude Code最適化**: Claude Codeでの開発に特化した設定とドキュメント
- 🔧 **カスタマイズ可能**: 必要な機能のみを選択して生成
- 📦 **モダンなツールチェーン**: uv, Ruff, mypy, pytest等の最新ツール
- 🧪 **充実したテスト環境**: 単体テスト、プロパティベーステスト、統合テスト
- 🔍 **厳格な品質管理**: strict modeの型チェック、リント、フォーマット
- 📊 **パフォーマンス測定**: ベンチマークとプロファイリング機能
- 🔗 **GitHub統合**: Actions、CLI、Issue/PRテンプレート

## 生成される機能（選択可能）

- ✅ GitHub Actions CI/CD
- ✅ pre-commit hooks
- ✅ mypy strict mode
- ✅ Hypothesis property-based testing
- ✅ Performance benchmarks
- ✅ Structured logging (structlog)
- ✅ Performance profiling

## 必要な環境

- Python 3.10+
- [Cookiecutter](https://cookiecutter.readthedocs.io/)

## Cookiecutterについて

このテンプレートは**Cookiecutter**を使用しています。Cookiecutterは単なるプロジェクト雛形ツールを超えた、強力なカスタマイズ機能を持つテンプレートエンジンです：

### 🎯 主な特徴

- **設定ファイル (`cookiecutter.json`)**: プロジェクト生成時の質問項目を定義
- **Jinja2テンプレートエンジン**: 変数埋め込み、条件分岐、ループ処理が可能
- **フック機能**: 生成前後にPythonスクリプトを実行（検証、初期化など）
- **柔軟なコマンドライン**: `--no-input`、`--output-dir`等のオプション
- **ユーザーデフォルト設定**: `~/.cookiecutterrc`で個人設定を保存
- **Python API**: スクリプトから直接呼び出し可能

### 🔧 このテンプレートでの活用例

```json
// cookiecutter.json - 設定項目の定義
{
  "use_logging": true,
  "license": ["MIT", "BSD-3-Clause", "Apache-2.0"]
}
```

```jinja
<!-- テンプレート内 - 条件分岐 -->
{% if cookiecutter.use_logging %}
├── utils/logging_config.py
{% endif %}
```

```python
# hooks/post_gen_project.py - 生成後処理
if not {{cookiecutter.use_logging}}:
    remove_file("utils/logging_config.py")
```

### 📚 高度な使い方

```bash
# デフォルト値で自動生成（CI/CD向け）
cookiecutter gh:zerebom/python-template-for-claude-code-cookiecutter --no-input

# 出力先指定
cookiecutter . --output-dir ~/projects/

# 設定ファイル指定
cookiecutter . --config-file custom-config.yaml
```

## 使用方法

### 1. Cookiecutterのインストール

```bash
pip install cookiecutter
# または
pipx install cookiecutter
```

### 2. テンプレートからプロジェクト生成

```bash
cookiecutter https://github.com/zerebom/python-template-for-claude-code-cookiecutter
```

### 3. インタラクティブな設定

プロンプトに従って以下の項目を設定：

```
project_name [My Python Project]: 
project_slug [my-python-project]: 
package_name [my_python_project]: 
author_name [Your Name]: 
author_email [your.email@example.com]: 
github_username [yourusername]: 
project_short_description [A short description of the project]: 
version [0.1.0]: 
python_version [3.12]: 
use_github_actions [y]: 
use_pre_commit [y]: 
use_mypy_strict [y]: 
use_hypothesis [y]: 
use_benchmarks [y]: 
use_logging [y]: 
use_profiling [y]: 
license [MIT]: 
```

### 4. プロジェクト初期化

```bash
cd your-project-name
make setup
```

## 生成されるプロジェクト構造

```
your-project/
├── .github/                     # GitHub設定（条件付き）
│   ├── workflows/ci.yml         # CI/CD workflow
│   ├── dependabot.yml           # Dependabot設定
│   └── ISSUE_TEMPLATE/          # Issue/PRテンプレート
├── src/
│   └── your_package/            # メインパッケージ
│       ├── __init__.py
│       ├── core/                # コアロジック
│       └── utils/               # ユーティリティ（条件付き）
│           ├── logging_config.py
│           └── profiling.py
├── template/                    # 参考実装
│   ├── src/your_package/        # モデルコード
│   └── tests/                   # テスト例
├── tests/                       # テストディレクトリ
│   ├── unit/                    # 単体テスト
│   ├── property/                # プロパティテスト（条件付き）
│   ├── integration/             # 統合テスト
│   └── conftest.py
├── docs/                        # ドキュメント
├── scripts/                     # ユーティリティスクリプト
├── .pre-commit-config.yaml      # pre-commit設定（条件付き）
├── pyproject.toml               # プロジェクト設定
├── Makefile                     # 開発コマンド
├── CLAUDE.md                    # Claude Code設定
└── README.md                    # プロジェクト説明
```

## よく使用するコマンド

```bash
# 開発環境セットアップ
make setup

# テスト実行
make test                # 全テスト
make test-unit          # 単体テストのみ
make test-property      # プロパティテストのみ（条件付き）

# コード品質チェック
make format             # フォーマット
make lint               # リント
make typecheck          # 型チェック（条件付き）
make check              # 全チェック

# GitHub操作（条件付き）
make pr TITLE="Title" BODY="Body"
make issue TITLE="Title" BODY="Body"

# その他
make benchmark          # ベンチマーク（条件付き）
make clean              # クリーンアップ
make help               # ヘルプ
```

## カスタマイズ

生成後、以下のファイルを編集してプロジェクトをカスタマイズ：

- `CLAUDE.md`: Claude Code固有の設定
- `pyproject.toml`: 依存関係と設定
- `Makefile`: 開発コマンド
- `.github/workflows/`: CI/CD設定

## ライセンス

このテンプレート自体はMITライセンスです。
生成されたプロジェクトは選択したライセンスに従います。

## 貢献

Issues、Pull Requestをお待ちしています！

## クレジット

このテンプレートは以下のプロジェクトをベースにしています：

- **原作**: [discus0434/python-template-for-claude-code](https://github.com/discus0434/python-template-for-claude-code)
- **解説記事**: [Claude Code用のPythonテンプレートを作った](https://zenn.dev/discus0434/articles/claude-code-python-template)

## 関連リンク

- [Claude Code](https://www.anthropic.com/claude-code)
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [uv](https://github.com/astral-sh/uv)
- [Ruff](https://github.com/astral-sh/ruff)
- [pytest](https://pytest.org/)
- [Hypothesis](https://hypothesis.readthedocs.io/)
