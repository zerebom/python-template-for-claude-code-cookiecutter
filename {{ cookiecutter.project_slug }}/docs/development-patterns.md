# Development Patterns and Best Practices

このドキュメントでは、{{ cookiecutter.project_name }}プロジェクトで推奨される開発パターンとベストプラクティスを説明します。

## 目次

- [プロジェクト構造](#プロジェクト構造)
- [コーディングパターン](#コーディングパターン)
- [テストパターン](#テストパターン)
- [ロギングパターン](#ロギングパターン)
- [エラーハンドリング](#エラーハンドリング)
- [パフォーマンス測定](#パフォーマンス測定)

## プロジェクト構造

### 推奨ディレクトリ構成

```
src/{{ cookiecutter.package_name }}/
├── __init__.py              # パッケージエクスポート
├── py.typed                 # 型情報マーカー
├── types.py                 # 型定義
├── core/                    # コアビジネスロジック
│   ├── __init__.py
│   └── example.py
├── utils/                   # ユーティリティ
│   ├── __init__.py
{%- if cookiecutter.use_logging %}
│   ├── logging_config.py    # ロギング設定
{%- endif %}
{%- if cookiecutter.use_profiling %}
│   ├── profiling.py         # パフォーマンス測定
{%- endif %}
│   └── helpers.py           # ヘルパー関数
└── cli/                     # CLI関連（必要に応じて）
    ├── __init__.py
    └── commands.py
```

### モジュール分割の原則

1. **core/**: ビジネスロジックの中核
2. **utils/**: 再利用可能なユーティリティ
3. **types.py**: 型定義の集約
4. **cli/**: コマンドラインインターフェース

## コーディングパターン

### 1. 型ヒントの活用

```python
from typing import Protocol
from dataclasses import dataclass

# データクラスの使用
@dataclass
class Config:
    name: str
    max_items: int = 100
    enable_validation: bool = True
    
    def __post_init__(self) -> None:
        if self.max_items <= 0:
            raise ValueError("max_items must be positive")

# Protocolの活用
class DataProcessor(Protocol):
    def process(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Process data and return result."""
        ...
```

### 2. エラーハンドリングのパターン

```python
# 具体的で実用的なエラーメッセージ
def validate_config(config: dict[str, Any]) -> None:
    if "name" not in config:
        raise ValueError(
            "Missing required field 'name' in configuration. "
            "Please provide a valid name string."
        )
    
    if not isinstance(config["name"], str):
        raise TypeError(
            f"Expected 'name' to be str, got {type(config['name']).__name__}. "
            f"Please provide a string value."
        )
```

### 3. ロギングパターン

{%- if cookiecutter.use_logging %}
```python
from {{ cookiecutter.package_name }}.utils.logging_config import get_logger

logger = get_logger(__name__)

def process_data(items: list[dict]) -> list[dict]:
    logger.debug(
        "Starting data processing",
        item_count=len(items),
        function="process_data"
    )
    
    try:
        result = []
        for i, item in enumerate(items):
            processed = transform_item(item)
            result.append(processed)
            
            if i % 100 == 0:
                logger.debug(
                    "Processing progress",
                    processed=i,
                    total=len(items),
                    progress_percent=round((i / len(items)) * 100, 1)
                )
        
        logger.info(
            "Data processing completed",
            input_count=len(items),
            output_count=len(result),
            success=True
        )
        return result
        
    except Exception as e:
        logger.error(
            "Data processing failed",
            error_type=type(e).__name__,
            error_message=str(e),
            item_count=len(items),
            exc_info=True
        )
        raise
```
{%- else %}
```python
import logging

logger = logging.getLogger(__name__)

def process_data(items: list[dict]) -> list[dict]:
    logger.info(f"Processing {len(items)} items")
    # 処理ロジック
    logger.info("Processing completed")
```
{%- endif %}

## テストパターン

### 1. 単体テスト

```python
import pytest
from {{ cookiecutter.package_name }}.core.example import ExampleConfig

class TestExampleConfig:
    def test_正常系_有効な設定で作成できる(self) -> None:
        """有効な設定でインスタンスが作成できることを確認。"""
        config = ExampleConfig(name="test", max_items=10)
        
        assert config.name == "test"
        assert config.max_items == 10
        assert config.enable_validation is True
    
    def test_異常系_不正な値でエラー(self) -> None:
        """不正な値でValueErrorが発生することを確認。"""
        with pytest.raises(ValueError, match="max_items must be positive"):
            ExampleConfig(name="test", max_items=0)
```

{%- if cookiecutter.use_hypothesis %}
### 2. プロパティベーステスト

```python
from hypothesis import given, strategies as st

class TestConfigProperty:
    @given(
        name=st.text(min_size=1),
        max_items=st.integers(min_value=1, max_value=1000)
    )
    def test_プロパティ_有効な値では常に成功(self, name: str, max_items: int) -> None:
        """有効な値の組み合わせでは常に成功することを検証。"""
        config = ExampleConfig(name=name, max_items=max_items)
        assert config.name == name
        assert config.max_items == max_items
```
{%- endif %}

### 3. 統合テスト

```python
def test_統合_設定とプロセッサの連携(tmp_path):
    """設定とデータ処理の統合動作を確認。"""
    # 設定ファイル作成
    config_file = tmp_path / "config.json"
    config_file.write_text('{"name": "test", "max_items": 5}')
    
    # 設定読み込み
    config = load_config(config_file)
    processor = DataProcessor(config)
    
    # データ処理
    result = processor.process([{"id": 1, "value": 10}])
    
    assert len(result) == 1
    assert result[0]["processed"] is True
```

## パフォーマンス測定

{%- if cookiecutter.use_profiling %}
### プロファイリングの活用

```python
from {{ cookiecutter.package_name }}.utils.profiling import profile, Timer

# 関数デコレーター
@profile
def heavy_computation(data: list[int]) -> int:
    return sum(x**2 for x in data)

# コンテキストマネージャー
def process_large_dataset(data: list[dict]) -> list[dict]:
    with Timer("Large dataset processing") as timer:
        result = []
        for item in data:
            processed = complex_transform(item)
            result.append(processed)
    
    logger.info(f"Processing took {timer.elapsed:.2f} seconds")
    return result
```
{%- endif %}

### ベンチマークテスト

{%- if cookiecutter.use_benchmarks %}
```python
import pytest

def test_performance_baseline(benchmark):
    """パフォーマンスのベースライン測定。"""
    data = list(range(1000))
    
    result = benchmark(process_data, data)
    
    assert len(result) == 1000
    # ベンチマーク結果は自動的に記録される
```
{%- endif %}

## ファイル操作パターン

### 設定ファイルの処理

```python
from pathlib import Path
import json
from typing import Any

def load_config(config_path: Path) -> dict[str, Any]:
    """設定ファイルを安全に読み込む。"""
    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}. "
            f"Create one with: touch {config_path}"
        )
    
    try:
        with config_path.open(encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON in {config_path}: {e}. "
            f"Please check the file format."
        ) from e
```

## CLI パターン

### Click を使用したCLI

```python
import click
from {{ cookiecutter.package_name }}.core.example import ExampleConfig

@click.command()
@click.option("--config", "-c", type=click.Path(exists=True), help="Configuration file")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def main(config: str, verbose: bool) -> None:
    """{{ cookiecutter.project_short_description }}"""
    if verbose:
        setup_logging(level="DEBUG")
    
    if config:
        cfg = load_config(Path(config))
    else:
        cfg = ExampleConfig(name="default")
    
    # メインロジック実行
    result = process_data(cfg)
    click.echo(f"Processed {len(result)} items")
```

## まとめ

これらのパターンを参考に、一貫性のある保守性の高いコードを書いてください。

- **型ヒント**: 必ず使用
- **エラーメッセージ**: 具体的で実用的に
- **ロギング**: 適切なレベルで構造化
- **テスト**: 単体・統合・プロパティベースを組み合わせ
- **ドキュメント**: コードの意図を明確に

詳細な実装例は `src/` および `tests/` ディレクトリを参照してください。