# SuperClaude コマンドリファレンス

このディレクトリには、Pythonプロジェクト開発を効率化するためのカスタムスラッシュコマンドが定義されています。

## コマンドカテゴリ

### 分析・改善
- `/analyze` - 多次元コード分析（品質、セキュリティ、パフォーマンス）
- `/improve` - エビデンスベースの改善提案と実装
- `/scan` - セキュリティと品質の包括的検証

### 開発・デバッグ
- `/troubleshoot` - 体系的なデバッグとトラブルシューティング
- `/task` - 複雑なタスクの管理とトラッキング

## 基本的な使用方法

```bash
# コード品質の分析
/analyze --code

# パフォーマンスの改善
/improve --perf --iterate

# セキュリティスキャン
/scan --security --owasp

# タスクの作成と管理
/task:create "新機能の実装"
```

## 既存ツールとの連携

これらのコマンドは、プロジェクトの既存ツールと連携して動作します：

- `make format/lint/typecheck` - コード品質チェック
- `make test` - テスト実行
- `make security/audit` - セキュリティ検証
- `uv` - パッケージ管理
- `gh` - GitHub操作

## 効率的なワークフロー

### 新機能開発
```bash
/task:create "機能名" → /analyze → 実装 → /improve → /scan --validate → make test
```

### バグ修正
```bash
/troubleshoot --fix → /analyze --code → 修正 → make test → /scan --validate
```

### パフォーマンス最適化
```bash
/analyze --perf → /improve --perf --iterate → make benchmark → /scan --validate
```

## 記号体系

効率的なコミュニケーションのための記号：

- `→` : 処理の流れ
- `|` : 選択・区切り
- `&` : 結合・並列
- `:` : 定義
- `»` : シーケンス
- `@` : 場所・参照
