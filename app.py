import gradio as gr
from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
import numpy as np
import cv2 as cv

generator = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')


def read_video(video_path):
    cap = cv.VideoCapture(video_path)
    video = []
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        video.append(frame)
    return video
    

def video_generation(text):
    test_text = {
            'text': text,
        }
    output_video_path = generator(test_text,)[OutputKeys.OUTPUT_VIDEO]
    return read_video(output_video_path)


model_input = gr.Textbox(lines=7, placeholder='A panda eating bamboo on a rock.', label='Input a sentence in English')
model_output = "playable_video"
demo = gr.Interface(fn=video_generation, inputs=model_input, outputs=model_output, allow_flagging="never")
demo.launch()
