# Spark-X2.5 Community Case Studies

Real stories from people who downloaded Spark-X2.5 (4B or 1.7B) from Hugging
Face or an official mirror, ran it on a real task — agentic workflow, coding,
long context, multilingual, or on-device deployment — and published the result
in the official Spark-X2.5 Discussions.

Models:
- https://huggingface.co/XHToken/Spark-X2.5-4B
- https://huggingface.co/XHToken/Spark-X2.5-1.7B
- Collection: https://huggingface.co/collections/XHToken/spark-x25

Discussions: https://huggingface.co/XHToken/Spark-X2.5-4B/discussions

## Publication rule

For this gallery, the public channel is intentionally limited to the official
Spark-X2.5 Discussions. Every accepted case must include at least one URL
matching:

    https://huggingface.co/XHToken/Spark-X2.5-4B/discussions/<number>
    https://huggingface.co/XHToken/Spark-X2.5-1.7B/discussions/<number>

Posts on other platforms may be shared separately, but they do not replace the
required Hugging Face Discussion and must not be listed in the channels field.
This keeps download instructions, runtime evidence, questions, and follow-up
answers next to the model that people need to download.

## What a strong case demonstrates

1. A genuine download of XHToken/Spark-X2.5-4B or Spark-X2.5-1.7B, not a copied
   output. Downloading from an official mirror (ModelScope, Modelers, SCNet,
   SourceFind, Ollama) is fine as long as the revision matches Hugging Face.
2. A real inference, agentic, coding, evaluation, or fine-tuning run using the
   downloaded snapshot.
3. The exact revision, runtime, hardware, input, output, and enough logs or
   screenshots for another person to reproduce the result.
4. A substantive Discussion post explaining the task, result, limitations,
   and what the author learned.

## Suggested directions

- Reproduce the official quick start with vLLM, SGLang, or llama.cpp; run
  locally through Ollama or LM Studio; exercise structured output and the
  `spark25` tool-call parser.
- Drive an agent harness (Codex, Claude Code, OpenClaw, Hermes) through a
  multi-step tool-use, planning, or automation task.
- Solve a real coding task: repository-level fix, competitive/online-judge
  problem, or an end-to-end code agent.
- Use the native 1M context for long-document QA, codebase understanding, or
  long-range retrieval.
- Cover 200+ languages: understanding, generation, translation, or a real
  cross-lingual scenario.
- Compare latency, memory, throughput, TTFT/TPOT, or quantization on available
  hardware (NVIDIA, 昇腾/Ascend, 海光/Hygon, HOUMO.AI, ...).
- Explore high-risk actions, ambiguity detection, confirmation, and refusal for
  agent/tool calls.
- Improve data, evaluation, training (LLaMA-Factory), deployment, or
  integration workflows and document a real before/after result.

## Requirements

Every submission must satisfy all of the following:

1. **Real download.** Download the model from XHToken/Spark-X2.5-4B or
   Spark-X2.5-1.7B (Hugging Face or an official mirror) using hf download,
   snapshot_download, Git LFS, or the mirror's client. Record the exact tested
   revision. Spark-X2.5 is licensed under Apache 2.0 — no extra usage terms to
   accept.
2. **Real execution.** Run the downloaded model or a derived artifact produced
   from that snapshot. Include representative inputs and raw outputs, plus a
   screenshot or log excerpt. For agentic runs, include the tool-call trace.
3. **Hugging Face Discussion.** Publish the full case in the official Spark-X2.5
   Discussions. A GitHub-only write-up is not sufficient.
4. **Reproducibility.** Record runtime and version, hardware, precision or
   quantization, key parameters, and the command or script used.
5. **Honest metrics.** State sample size and method for every accuracy,
   latency, memory, or throughput result. Do not compare incompatible setups.
6. **Safety and privacy.** Remove tokens, cache paths containing personal
   usernames, private prompts, sensitive data, and internal endpoints.
7. **Original work.** The run and evidence must be the submitter's own. AI may
   help edit prose, but it cannot replace an actual download and experiment.

## How to submit

1. Download a pinned snapshot, for example:

       hf download XHToken/Spark-X2.5-4B --revision <commit-sha>

2. Run a real Spark-X2.5 inference, agentic, coding, evaluation, or
   optimization experiment.
3. Create a new public Discussion with a title beginning:

       [HER Hack-Astron #5] <your case title>

4. Fork this repository and copy cases/TEMPLATE to cases/<case-id>.
5. Fill in every frontmatter field and section. The channels list must contain
   the public Discussion URL.
6. Open a PR titled:

       [case] <case-id> - <one-line result>

Reference the HER Hack-Astron #5 issue with Ref, not Closes, so one case does
not close the whole challenge.

## Directory layout

    cases/
    |-- README.md
    |-- TEMPLATE/
    |   -- README.md
    -- <case-id>/
        |-- README.md
        |-- preview.png
        -- optional supporting files

---

# Spark-X2.5 社区使用案例

这里收录真实的 Spark-X2.5 使用故事：参与者从 Hugging Face 或官方镜像下载模型
（4B 或 1.7B），完成一次真实的智能体、编码、长上下文、多语言或端侧部署实验，
并把完整过程发布在 Spark-X2.5 官方 Discussions。

## 唯一有效的公开发布渠道

活动案例必须发布到：

https://huggingface.co/XHToken/Spark-X2.5-4B/discussions

案例 frontmatter 的 channels 只能填写形如下面的链接：

    https://huggingface.co/XHToken/Spark-X2.5-4B/discussions/<编号>
    https://huggingface.co/XHToken/Spark-X2.5-1.7B/discussions/<编号>

其他平台可以自愿同步，但不能替代 Hugging Face Discussion，也不能作为活动验收链接。
这样每篇内容都会留在模型页旁边，让读者可以直接阅读、提问、下载并复现。

## 案例必须证明什么

1. 确实下载了 XHToken/Spark-X2.5-4B 或 Spark-X2.5-1.7B（HF 或官方镜像，镜像须与
   HF 同一 revision）；
2. 确实运行了所下载的 snapshot，或基于该 snapshot 生成的量化/微调产物；
3. 记录 revision、运行框架、硬件、输入、原始输出和复现命令；
4. 在官方 Discussion 发布有实质内容的完整案例，并在 GitHub 案例文件中回链。

## 提交步骤

1. 从 Hugging Face 或官方镜像下载固定 revision（Apache 2.0，无需签署额外条款）；
2. 完成真实推理、智能体、编码、评测、量化、训练或集成实验；
3. 新建标题以 HER Hack-Astron #5 开头的公开 Discussion；
4. 复制 cases/TEMPLATE 为 cases/<案例 id>；
5. 填写全部字段，channels 附上 Discussion 直达链接；
6. 提交标题为 [case] <案例 id> - <一句话结果> 的 PR，并在描述写 Ref 活动 issue。

详细验收字段见案例模板。不得提交模型权重、token、个人缓存路径、隐私数据或
未经授权的数据。
