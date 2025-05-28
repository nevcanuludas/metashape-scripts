# 🎞️ Extract Frames from Video using FFmpeg

This script extracts frames from a video file using FFmpeg, with scaling and frame rate settings.

## ✅ Command

```bash
ffmpeg -ss 00:00:00 -t 00:01:23 -i videoName.mov -vf "scale=iw*2:ih*2" -r 10.0 output_image-%04d.jpg
```

## 🔍 Explanation

- `-ss 00:00:00`: Start time in the video.
- `-t 00:01:23`: Duration of the video to process.
- `-i videoName.mov`: Input video file.
- `-vf "scale=iw*2:ih*2"`: Video filter to scale the video by 2x (input width × 2, input height × 2).
- `-r 10.0`: Frame rate — extract 10 frames per second.
- `output_image-%04d.jpg`: Output image files numbered sequentially (`output_image-0001.jpg`, etc.).

## 🧪 Example

```bash
ffmpeg -ss 00:00:00 -t 00:02:59 -i IMG_5902.MOV -vf "scale=iw*2:ih*2" -r 10.0 output_image-%04d.jpg
```
