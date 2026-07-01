# Nexus Skills 中文介绍

Nexus Skills 是一组面向 coding agent 的技能，用来设计**项目专属的本地机器学习实验工作台**。

它不是把我的 Nexus 系统安装到别人的项目里，而是教 AI 在用户自己的仓库中设计和实现一个适合该项目的、主要给人看的实验分析、对比和可视化系统。

[English README](README.md)

## 这是什么

这些 Skills 可以帮助 coding agent：

- 读取或摄入已有的 metrics、日志、数据集文件和训练产物；
- 生成 EDA 报告和实验 dashboard；
- 对比不同实验和 baseline；
- 设计清晰的图表，并支持 hover 显示精确数值；
- 在明确需要自动化时，可选设计机器可读输出。

生成出来的系统应该属于目标项目本身，符合那个项目的技术栈、目录结构和界面风格。

## 这不是什么

Nexus Skills 不会：

- 复制或安装原始 Nexus 实现；
- 强制使用固定 Python 包或 SQLite schema；
- 要求用户修改训练代码或接入 SDK；
- 要求视觉本地工作流必须提供 CLI 或 JSON 协议；
- 携带任何私人实验数据；
- 绑定 Codex、Claude Code、Trae、Qoder、Cursor、Zed 等某一个平台。

## 包含的 Skills

### `nexus-workbench-designer`

用于设计或添加主要给人看的本地 ML 实验可视化工作台、EDA/报告系统、训练结果 dashboard 或 Nexus-like 可视化工作流。

### `nexus-experiment-ux`

用于设计实验 dashboard、对比图、EDA 报告、指标卡片、hover tooltip 和视觉 QA。

### `nexus-agent-protocol`

可选项。仅在明确需要命令行自动化、JSON 输出协议、结构化错误、CI hook、远程摄入或 coding agent 项目规则时使用。

## 仓库结构

```text
skills/
  nexus-workbench-designer/
  nexus-experiment-ux/
  nexus-agent-protocol/

fixtures/
  python-classification/
```

`fixtures/` 用于测试 agent 是否能利用这些 Skills 在一个小型 ML 项目里生成自己的实验工作台。

## 安装

### Codex

把两个视觉核心 skill 文件夹复制到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -r skills/nexus-workbench-designer ~/.codex/skills/
cp -r skills/nexus-experiment-ux ~/.codex/skills/
```

如果明确需要 CLI / JSON / agent 自动化，再额外安装：

```bash
cp -r skills/nexus-agent-protocol ~/.codex/skills/
```

复制后重启 Codex。

### 其他 Coding Agent

核心内容都是 Markdown。对于 Claude Code、Trae、Qoder、Cursor、Zed、Cline、Continue 等工具，可以把相同内容改写到它们支持的规则或技能格式中，例如：

- `CLAUDE.md`
- `AGENTS.md`
- `.cursorrules`
- 项目规则文件
- 自定义 skill 文件夹

更多说明见 [INSTALL.md](INSTALL.md)。

## 示例提示词

```text
使用 Nexus Skills 为这个 ML 仓库设计一个本地实验工作台。
```

```text
添加一个实验 dashboard，可以摄入 metrics CSV 并对比不同 runs。
```

只有明确需要自动化时才使用这个提示词：

```text
为这个实验 dashboard 添加一个可选的 agent-friendly CLI/JSON 协议。
```

```text
优化这个实验 dashboard，让图表上的点 hover 时显示精确数值。
```

## 设计理念

Nexus Skills 分发的是设计能力，不是固定应用。

默认方式是 file-first / artifact-first：优先利用已有的本地 CSV、JSON、日志、数据样本、TensorBoard 导出、WandB/MLflow 导出和 notebook 输出，而不是要求用户修改训练代码。

生成出来的系统应该默认安全：

- 不直接修改原始数据；
- 不在没有确认时删除实验；
- 不把 secrets 写进报告；
- CLI 和机器可读协议保持可选，只有 agent、CI 或远程工具需要调用命令时才加入。

## 当前状态

初始公开版本。两个视觉优先核心 Skills 和一个可选自动化 Skill 已通过 Codex skill 结构校验，并包含一个小型 forward-test fixture。
