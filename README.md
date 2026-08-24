<p align="center">
  <img src="assets/xhtoken.png" width="15%" />
</p>
<h1 align="center">Spark-X2.5</h1>

<div align="center">
  
[![Slack](https://img.shields.io/badge/Slack-Join-4A154B?logo=slack&logoColor=white)](https://join.slack.com/t/tokenspark/shared_invite/zt-432qf8l2f-5~dLyXv8uETr0P0UuC07nw)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/kTDE2Hg8aw)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@SparkLLM)
[![dev.to](https://img.shields.io/badge/dev.to-Follow-0A0A0A?logo=devdotto&logoColor=white)](https://dev.to/sparkllm)
[![Bluesky](https://img.shields.io/badge/Bluesky-Follow-0285FF?logo=bluesky&logoColor=white)](https://bsky.app/profile/sparkllm.bsky.social)
[![X](https://img.shields.io/badge/X-Follow-000000?logo=x&logoColor=white)](https://x.com/sparkllm)
[![Zhihu](https://img.shields.io/badge/Zhihu-Follow-0084FF?logo=zhihu&logoColor=white)](https://www.zhihu.com/people/zhiikz7qh7m)
[![WeChat](https://img.shields.io/badge/WeChat-Join-07C160?logo=wechat&logoColor=white)](https://github.com/XHToken/community/blob/main/docs/images/xhtoken-wechat.jpg)

</div>

Welcome to the GitHub repository of Spark-X2.5 open model series. You can find official information about Spark-X2.5, and post your questions [here(Issues)](https://github.com/XHToken/Spark-X2.5/issues).

## Introduction

Today, we are introducing Spark-X2.5-4B and Spark-X2.5-1.7B, two compact, general-purpose language models designed to make capable AI more practical, efficient, and accessible. The models deliver strong performance across a broad range of everyday tasks—including conversation, writing, translation, reasoning, coding, tool use, and agentic workflows—achieving leading results among open-source models of comparable size. Spark-X2.5 combines an efficiency-oriented architecture with native context windows of up to 1M tokens, and support for more than 200 languages. 

**Technical Highlights**:
- **Efficient Architecture and Native 1M-token Context**: The models use a hybrid attention architecture that combines one full-attention layer with three sliding-window attention layers. This design substantially reduces the computational overhead typically associated with long-context models while natively supporting a context window of up to 1M tokens.
- **Strong Coding and Agent Capabilities**: The models are deeply integrated with popular agent harnesses, including Codex, Claude Code, OpenClaw, and Hermes. They deliver state-of-the-art performance among models of comparable size across everyday coding, agentic workflows, reasoning, and instruction-following tasks.
- **Broad Hardware and Software Compatibility**: The models support a wide range of hardware platforms, including NVIDIA, Huawei, Hygon, HOUMO.AI, etc. It is compatible with leading inference frameworks such as vLLM, SGLang, llama.cpp, MLX, and can be deployed quickly through platforms including Ollama and LM Studio. The models can also be customized using popular fine-tuning frameworks such as LLaMA-Factory. Across multiple hardware platforms, they deliver superior TTFT, TOPT, and overall inference efficiency compared with similarly sized models.
- **Advanced Training Algorithms**: The models were trained on Huawei Ascend clusters. Large-scale reinforcement learning and post-training techniques such as MOPD significantly enhance its reasoning, coding, agentic, and instruction-following capabilities.

<p align="center">
  <img src="assets/benchmark.svg" />
</p>

## Model Downloads

The Spark-X2.5-4B and Spark-X2.5-1.7B are available on the following platforms. Choose the most suitable download source for your region and environment:

| Platform | Download | Description |
| --- | --- | --- |
| Hugging Face | [Spark-X2.5 in Huggingface](https://huggingface.co/collections/XHToken/spark-x25) | Official Hugging Face model collection for Spark-X2.5 |
| ModelScope | [Spark-X2.5 in ModelScope](https://www.modelscope.cn/collections/XHToken/Spark-X25) | Recommended download source for users in China |
| Modelers | [Spark-X2.5 in Modelers](https://modelers.cn/user/XHToken) | Recommended download source for users with Ascend chips |
| Ollama | [Spark-X2.5 in Ollama](https://ollama.com/SparkLLM) | Download and run the model locally with Ollama |
| SCNet | [Spark-X2.5 in SCNet](https://www.scnet.cn/ui/aihub/models/XHToken/Spark-X2.5-4B) | Recommended download source for users with Hygon chips | 
<!-- | SourceFind | [Spark-X2.5 in SourceFind](https://developer.sourcefind.cn/modelzoo) | Recommended download source for users with Hygon chips | -->

> If Hugging Face is slow or unavailable in your region, try ModelScope, Modelers or SCNet instead.

<!-- > If Hugging Face is slow or unavailable in your region, try ModelScope, Modelers, SCNet, or SourceFind instead. -->


## Benchmarks
<div style="overflow-x: auto; width: 100%;">
<table style="width: 100%; min-width: 1080px; border-collapse: collapse; text-align: center;">
  <colgroup>
    <col style="width: 190px;">
    <col span="8" style="width: 110px;">
  </colgroup>
  <thead>
    <tr>
      <th align="center">Benchmark</th>
      <th align="center"><span style="white-space: nowrap;">Spark‑X2.5‑4B</span></th>
      <th align="center"><span style="white-space: nowrap;">Spark‑X2.5‑1.7B</span></th>
      <th align="center"><span style="white-space: nowrap;">Qwen3.5‑9B</span></th>
      <th align="center"><span style="white-space: nowrap;">Qwen3.5‑4B</span></th>
      <th align="center"><span style="white-space: nowrap;">Qwen3.5‑2B</span></th>
      <th align="center"><span style="white-space: nowrap;">Gemma4‑12B</span></th>
      <th align="center"><span style="white-space: nowrap;">Gemma4‑E4B</span></th>
      <th align="center"><span style="white-space: nowrap;">Gemma4‑E2B</span></th>
    </tr>
  </thead>
  <tbody>
    <tr><th colspan="9" align="left">Agent</th></tr>
    <tr><td align="center">BFCL‑V4</td><td align="center">65.1</td><td align="center">46.9</td><td align="center"><strong>66.1*</strong></td><td align="center">50.3*</td><td align="center">43.6*</td><td align="center">37.4</td><td align="center">36.9</td><td align="center">30.2</td></tr>
    <tr><td align="center">τ²‑bench</td><td align="center">75.1</td><td align="center">65.3</td><td align="center">79.1*</td><td align="center"><strong>79.9*</strong></td><td align="center">48.8*</td><td align="center">69.0*</td><td align="center">42.2*</td><td align="center">24.5*</td></tr>
    <tr><td align="center">τ³‑bench</td><td align="center"><strong>30.4</strong></td><td align="center">20.1</td><td align="center">9.3</td><td align="center">6.7</td><td align="center">4.1</td><td align="center">13.3</td><td align="center">10.1</td><td align="center">8.8</td></tr>
    <tr><td align="center">MCP‑Atlas</td><td align="center"><strong>54.6</strong></td><td align="center">23.4</td><td align="center">47.4*</td><td align="center">40.8*</td><td align="center">14.8</td><td align="center">30.5*</td><td align="center">15.0*</td><td align="center">12.6</td></tr>
    <tr><td align="center">MCP‑Mark</td><td align="center"><strong>14.2</strong></td><td align="center">2.3</td><td align="center">13.4</td><td align="center">12.5</td><td align="center">–</td><td align="center">–</td><td align="center">–</td><td align="center">–</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">Workspace Bench</span></td><td align="center"><strong>31.2</strong></td><td align="center">18.9</td><td align="center">25.5</td><td align="center">21.3</td><td align="center">7.7</td><td align="center">–</td><td align="center">–</td><td align="center">–</td></tr>
    <tr><td align="center">VitaBench2.0</td><td align="center"><strong>25.2</strong></td><td align="center">8.3</td><td align="center">15.6</td><td align="center">18.2</td><td align="center">5.2</td><td align="center">12.4</td><td align="center">4.8</td><td align="center">4.4</td></tr>
    <tr><td align="center">BrowseComp</td><td align="center"><strong>40.9</strong></td><td align="center">29.7</td><td align="center">8.3</td><td align="center">14.3</td><td align="center">3.1</td><td align="center">10.0</td><td align="center">8.3</td><td align="center">3.7</td></tr>
    <tr><th colspan="9" align="left">Code</th></tr>
    <tr><td align="center"><span style="white-space: nowrap;">SWE‑Bench Pro</span></td><td align="center"><strong>44.4</strong></td><td align="center">10.4</td><td align="center">33.8*</td><td align="center">29.4*</td><td align="center">1.9</td><td align="center">21.9*</td><td align="center">4.0*</td><td align="center">–</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">SWE‑Bench Verified</span></td><td align="center">41.6</td><td align="center">28.3</td><td align="center"><strong>53.1*</strong></td><td align="center">38.8*</td><td align="center">6.8</td><td align="center">44.2*</td><td align="center">14.0*</td><td align="center">–</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">SWE‑Bench Multilingual</span></td><td align="center"><strong>53.3</strong></td><td align="center">23.3</td><td align="center">43.3</td><td align="center">27.7</td><td align="center">5.0</td><td align="center">32.5*</td><td align="center">–</td><td align="center">–</td></tr>
    <tr><td align="center">SciCode</td><td align="center">34.7</td><td align="center">18.2</td><td align="center">32.7*</td><td align="center">24.0</td><td align="center">6.0</td><td align="center"><strong>39.8</strong></td><td align="center">27.5</td><td align="center">20.5</td></tr>
    <tr><th colspan="9" align="left">Math</th></tr>
    <tr><td align="center"><span style="white-space: nowrap;">Gaokao 2026</span></td><td align="center">133.4</td><td align="center">114.8</td><td align="center"><strong>135.5</strong></td><td align="center">130.3</td><td align="center">94.0</td><td align="center">130.6</td><td align="center">102.4</td><td align="center">81.8</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">AIME 2026</span></td><td align="center"><strong>90.7</strong></td><td align="center">69.4</td><td align="center">88.2</td><td align="center">83.0</td><td align="center">30.8</td><td align="center">82.1*</td><td align="center">42.5*</td><td align="center">37.5*</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">HMMT Feb 2026</span></td><td align="center"><strong>81.2</strong></td><td align="center">48.4</td><td align="center">70.8</td><td align="center">69.7</td><td align="center">21.5</td><td align="center">65.6</td><td align="center">34.2</td><td align="center">20.5</td></tr>
    <tr><td align="center"><span style="white-space: nowrap;">IMO‑AnswerBench</span></td><td align="center"><strong>74.2</strong></td><td align="center">45.4</td><td align="center">69.8</td><td align="center">68.5</td><td align="center">–</td><td align="center">57.2</td><td align="center">26.9</td><td align="center">22.6</td></tr>
    <tr><th colspan="9" align="left">General &amp; Knowledge</th></tr>
    <tr><td align="center">IFEval</td><td align="center">93.0</td><td align="center">89.5</td><td align="center">91.5*</td><td align="center">89.8*</td><td align="center">78.6*</td><td align="center"><strong>94.8</strong></td><td align="center">45.3</td><td align="center">34.8</td></tr>
    <tr><td align="center">IFBench</td><td align="center"><strong>75.0</strong></td><td align="center">66.3</td><td align="center">64.5</td><td align="center">59.2</td><td align="center">41.3*</td><td align="center">73.5*</td><td align="center">44.0*</td><td align="center">22.7</td></tr>
    <tr><td align="center">AA‑LCR</td><td align="center">56.3</td><td align="center">24.3</td><td align="center"><strong>63.0*</strong></td><td align="center">57.0*</td><td align="center">25.6*</td><td align="center">55.3*</td><td align="center">34.7</td><td align="center">18.3</td></tr>
    <tr><td align="center">HLE</td><td align="center">12.3</td><td align="center">6.3</td><td align="center"><strong>14.3</strong></td><td align="center">8.6</td><td align="center">2.1</td><td align="center">13.1</td><td align="center">3.9</td><td align="center">2.5</td></tr>
    <tr><td align="center">GPQA</td><td align="center">67.4</td><td align="center">43.8</td><td align="center"><strong>77.2</strong></td><td align="center">67.2</td><td align="center">44.6</td><td align="center">72.8</td><td align="center">54.5</td><td align="center">43.8</td></tr>
  </tbody>
</table>
</div>

> - \* denotes reported results from publicly‑released model cards / papers and - denotes scores not yet available.
> - All evaluations are conducted in thinking mode. The recommended sampling parameters for Spark-X2.5 are temperature=1.0, top_p=0.95, and top_k=-1.
> - Gaokao 2026 consists of the five 2026 Chinese GAOKAO examinations (National I,National II, Beijing, Shanghai, Tianjin), each graded out of 150 points.

## Quickstart

### SGLang

#### Install SGLang

Use the pre-built image that tracks the Spark-X2.5 runtime:

```bash
docker pull lmsysorg/sglang:nightly-dev-cu13-20260827-20621aa1
```

#### Run Inference

The following command can be used to start an OpenAI-compatible API server on a single GPU with maximum context length 1,048,576 tokens.

#### Server

```bash
docker run -it \
  --gpus '"device=0"' \
  --ipc=host \
  -p 30000:30000 \
  -v "$MODEL_PATH":/root/Spark-X2.5-4B \
  lmsysorg/sglang:nightly-dev-cu13-20260827-20621aa1 \
  python -m sglang.launch_server \
    --model-path /root/Spark-X2.5-4B \
    --served-model-name spark2.5 \
    --tool-call-parser spark25 \
    --reasoning-parser qwen3 \
    --tp-size 1 \
    --mem-fraction-static 0.8 \
    --context-length 1048576 \
    --chat-template /root/Spark-X2.5-4B/chat_template.jinja \
    --host 0.0.0.0 \
    --port 30000
```

#### Client

Thinking is enabled by default by both the chat template and the qwen3 reasoning parser. To disable thinking for a specific request, set "chat_template_kwargs": {"enable_thinking": false}.

```bash
curl -s http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "spark2.5",
    "messages": [
      {
        "role": "user",
        "content": "安徽的省会在哪里？"
      }
    ],
    "max_tokens": 131072,
    "temperature": 1,
    "top_k": -1,
    "top_p": 0.95,
    "repetition_penalty": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0
  }'
```

### vLLM

#### Install vLLM

```bash
pip install uv
uv venv ~/spark2_5
source ~/spark2_5/bin/activate
git clone https://github.com/XHToken/Spark-plugin.git
cd ./Spark-plugin
uv pip install .
```

#### Server

```bash
vllm serve "./Spark-X2.5-4B" \
 --port "30000" \
 --trust-remote-code \
 --served-model-name spark25 \
 --tensor-parallel-size 1 \
 --gpu-memory-utilization 0.7 \
 --enable-prefix-caching \
 --chat-template Spark-X2.5-4B/chat_template.jinja
```

#### Client

```bash
curl -s http://127.0.0.1:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "spark25",
    "messages": [{"role": "user", "content": "安徽的省会在哪里？"}],
    "temperature": 1.0, 
    "top_k": -1,
    "top_p": 0.95
  }'
```

### MLX
Spark-MLX-LLM runs the original Spark-X2.5 Hugging Face checkpoints locally. It supports Apple silicon GPU, Linux CPU, and NVIDIA CUDA on Linux. No GGUF conversion is required.

#### Installation

```bash
git clone https://github.com/XHToken/Spark-MLX-LLM.git
cd Spark-MLX-LLM

python3 -m venv .venv
source .venv/bin/activate

# Apple silicon
python -m pip install -e .
# Linux cpu
python -m pip install -e '.[cpu]'
# Linux with cuda12
python -m pip install -e '.[cuda12]' 
# Linux with cuda13
python -m pip install -e '.[cuda13]'
```

Run Spark-X2.5

```bash
spark-mlx-generate \
  --device gpu \
  --dtype bfloat16 \
  --model XHToken/Spark-X2.5-1.7B \
  --prompt "安徽的省会在哪里？" \
  --max-tokens 512 \
  --temp 0
```

### Ollama

#### Build

```bash
git clone https://github.com/XHToken/llama.cpp.git llama.cpp-spark
git clone https://github.com/ollama/ollama.git ollama-spark
cd ollama-spark
export OLLAMA_LLAMA_CPP_SOURCE="$(cd ../llama.cpp-spark && pwd)"
cmake -S . -B build
cmake --build build --parallel 8
```

#### Create and Run

```bash
printf 'FROM /absolute/path/to/your.gguf\n' > ./Modelfile.spark
./ollama serve
./ollama create Spark-X2.5-1.7B -f ./Modelfile.spark
./ollama run Spark-X2.5-1.7B
```

### LM Studio

#### Build

```bash
git clone https://github.com/XHToken/llama.cpp.git llama.cpp-spark
cd llama.cpp-spark
cmake -S . -B build
cmake --build build --parallel 8
```

#### Set Up LM Studio

1. Close LM Studio.

2. Back up the selected runtime directory:

   ```text
   <LM_STUDIO_HOME>/extensions/backends/<selected-runtime>/
   ```

3. Copy the `llama.cpp-spark` build output into the selected runtime directory, overwriting the existing files.

4. Place the GGUF model in the following directory:

   ```text
   <LM_STUDIO_HOME>/models/<org>/<name>/
   ```

Example runtime directory on macOS:

```text
./build/bin/* -> ~/.lmstudio/extensions/backends/llama.cpp-mac-arm64-apple-metal-advsimd-<version>/
```

#### Run with LM Studio

Open My Models, select the Spark-X2.5 model, click Load, then start a new Chat.

#### Run with lms cli

```bash
# Replace `<model>` with a model listed by `lms ls`
lms load <model>
lms chat <model>
```

### Finetuning

We advise you to use [Llama-Factory](https://github.com/XHToken/LlamaFactory) to finetune your models.


## License

The Spark-X2.5 model series is licensed under the [Apache 2.0 License](LICENSE).

## Citation
If you find our work helpful, feel free to give us a cite.

```bibtex
@misc{sparkx2.5,
    title  = {Spark-X2.5 4B&1.7B: Pushing the Limits of Agentic Capabilities in On-Device Models},
    author = {SparkLLM Team},
    year   = {2026}
}
```
