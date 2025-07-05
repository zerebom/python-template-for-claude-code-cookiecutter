# Python Template for Claude Code (Cookiecutter)

Claude Codeでの開発に最適化されたPythonプロジェクトテンプレートです。Cookiecutterを使用して、カスタマイズ可能なプロジェクト構造を提供します。

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
- ✅ Dependabot
- ✅ GitHub CLI integration
- ✅ Structured logging (structlog)
- ✅ Performance profiling

## 必要な環境

- Python 3.10+
- [Cookiecutter](https://cookiecutter.readthedocs.io/)

## 使用方法

### 1. Cookiecutterのインストール

```bash
pip install cookiecutter
# または
pipx install cookiecutter
```

### 2. テンプレートからプロジェクト生成

```bash
cookiecutter https://github.com/zerebom/python-template-for-calaude-code-cookicutter
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
use_dependabot [y]: 
use_github_cli_integration [y]: 
use_logging [y]: 
use_profiling [y]: 
license [MIT]: 
open_source_license [MIT]: 
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

## 関連リンク

- [Claude Code](https://www.anthropic.com/claude-code)
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [uv](https://github.com/astral-sh/uv)
- [Ruff](https://github.com/astral-sh/ruff)
- [pytest](https://pytest.org/)
- [Hypothesis](https://hypothesis.readthedocs.io/)