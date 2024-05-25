from ultralytics.models import YOLOv10, YOLO
import cv2
import time 
import logging 
import sys
import torch 
import platform
import argparse


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Benchmark YOLOV10 model on a video file.")
    
    parser.add_argument('--video_path', type=str, required=True, 
                        help='Path to the video file')
    parser.add_argument('--device', type=str, choices=['cpu', 'cuda'], default='cuda',
                        help='Device to run the model on (cpu, cuda)')
    parser.add_argument(
        '--model_path',
        type=str,
        default='yolov10n.pt',
        help='Path to the model file (default: yolov10n.pt)'
    )

    args = parser.parse_args()
    
    
    return args

if __name__ == "__main__":
    args = parse_arguments()
    total_time = 0
    model_path = args.model_path
    video_path = args.video_path
    cap = cv2.VideoCapture(video_path)
    width  = cap.get(3)  
    height = cap.get(4)  
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    logger.info('Video is open :' + str(cap.isOpened()))
    model : YOLO = YOLOv10(model=model_path, verbose=False)
    device_name = args.device
    if device_name == "cpu":
        device = platform.processor()
        model.to(device="cpu")
        
    else: 
        device = torch.cuda.get_device_properties(torch.cuda.device(0))
       
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret :
            break
        t = time.time()
        res = model(frame)
        t = time.time() - t
        total_time += t
    report = f"""
    Report
    \tModel : {model_path}
    \tVideo : {video_path}
    \t\t fps : {fps}
    \t\t (width, height) : ({width},{height})
    \t\t Total frame : {length}
    Model inference stats :
    \tDevice : {model.device} {device}
    \tAvg predict time : {(total_time / length):.2f}s
    \tFPS : {100/(total_time / length):.2f}fps


"""
    logger.info(report)
    




