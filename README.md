---
domain:
- multi-modal
tags:
- text2video generation
- diffusion model
- 文到视频
- 文生视频
- 文本生成视频
- 生成
models:
- damo/text-to-video-synthesis
license: Apache License 2.0
deployspec:
  cpu: 4
  memory: 32000
  entry_file: app.py
  gpu: 0
  gpu_memory: 32
  instance: 1
license: Apache License 2.0
---
#### Clone with HTTP
```bash
 git clone https://www.modelscope.cn/studios/damo/text-to-video-synthesis.git
```