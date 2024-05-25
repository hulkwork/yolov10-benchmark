# yolov10-benchmark

This project aims to evaluate the performance of the YOLOV10 object detection model. We will measure only the inference speed here different hardware configurations.

- cpu Intel(R) Xeon(R) W-2155 CPU @ 3.30GHz
- cuda:0 _CudaDeviceProperties(name='Quadro P5000', major=6, minor=1, total_memory=16278MB, multi_processor_count=20)

And also this repo provide you a simple code to run yolov10

## Install

Please refer to [Yolov10](https://github.com/THU-MIG/yolov10) implementation

## Usage

```bash
python main.py --video <video_path> --device <cpu/cuda>
```

## Benchmark

I use [Intel IoT Video](https://github.com/intel-iot-devkit/sample-videos?tab=readme-ov-file), exactly this [one](https://github.com/intel-iot-devkit/sample-videos/raw/master/store-aisle-detection.mp4).

### CPU
```
    Report
        Model : yolov10n.pt
        Video : store-aisle-detection.mp4
                 fps : 59
                 (width, height) : (720.0,404.0)
                 Total frame : 3921
    Model inference stats :
        Device : cpu Intel(R) Xeon(R) W-2155 CPU @ 3.30GHz
        Avg predict time : 0.03s
        FPS : 28.63fps
```

### GPU

```
   Report
        Model : yolov10n.pt
        Video : store-aisle-detection.mp4
                 fps : 59
                 (width, height) : (720.0,404.0)
                 Total frame : 3921
    Model inference stats :
        Device : cuda:0 _CudaDeviceProperties(name='Quadro P5000', major=6, minor=1, total_memory=16278MB, multi_processor_count=20)
        Avg predict time : 0.01s
        FPS : 103.38 fps
```

## Citation

```BibTeX
@misc{wang2024yolov10,
      title={YOLOv10: Real-Time End-to-End Object Detection}, 
      author={Ao Wang and Hui Chen and Lihao Liu and Kai Chen and Zijia Lin and Jungong Han and Guiguang Ding},
      year={2024},
      eprint={2405.14458},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
