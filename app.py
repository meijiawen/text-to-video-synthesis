#!/usr/bin/env python

from __future__ import annotations

import os
import pathlib
import random
import shlex
import subprocess

import gradio as gr
import torch
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline

DESCRIPTION = '# [ModelScope 文本生成视频](https://modelscope.cn/models/damo/text-to-video-synthesis/summary)'

pipe = p = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')


def generate(prompt: str, seed: int) -> str:
    if seed == -1:
        seed = random.randint(0, 1000000)
    torch.manual_seed(seed)
    return pipe({'text': prompt})[OutputKeys.OUTPUT_VIDEO]


examples = [
    ['An astronaut riding a horse.', 0],
    ['A panda eating bamboo on a rock.', 0],
    ['Spiderman is surfing.', 0],
]

with gr.Blocks(css='style.css') as demo:
    with gr.Row():
        with gr.Column():
            prompt = gr.Text(label='Prompt', max_lines=1)
            seed = gr.Slider(
                label='Seed',
                minimum=-1,
                maximum=1000000,
                step=1,
                value=-1,
                info='If set to -1, a different seed will be used each time.')
            run_button = gr.Button('Run')
        with gr.Column():
            result = gr.Video(label='Result')

    inputs = [prompt, seed]
    gr.Examples(examples=examples,
                inputs=inputs,
                outputs=result,
                fn=generate,
                cache_examples=True)

    prompt.submit(fn=generate, inputs=inputs, outputs=result)
    run_button.click(fn=generate, inputs=inputs, outputs=result)

demo.queue(api_open=False, max_size=15).launch()
