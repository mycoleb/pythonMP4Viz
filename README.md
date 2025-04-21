# Sine Wave Animation Generator

A Python script that creates smooth animated sine wave visualizations and exports them as MP4 videos.

## Features

- Creates visually appealing sine wave animations with phase shifts
- Exports high-quality MP4 videos
- Customizable duration, frame rate, and quality settings
- Comprehensive error handling and user feedback
- Clean, well-documented code

## Prerequisites

The script requires the following dependencies:

- Python 3.6+
- MoviePy
- Matplotlib
- NumPy
- FFmpeg (external dependency, must be installed separately and available in PATH)

## Installation

1. Create and activate a virtual environment (recommended):

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

2. Install required Python packages:

```bash
pip install moviepy matplotlib numpy
```

3. Install FFmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` or equivalent for your distribution

## Usage

Run the script with default parameters:

```bash
python p.py
```

This will create a 10-second sine wave animation at 20 frames per second and save it as `sine_wave_animation.mp4` in the current directory.

## Customization

To customize the animation, edit the parameters in the main execution block:

```python
# Modify these parameters as needed
output_file = "sine_wave_animation.mp4"  # Output filename
duration = 10  # Duration in seconds
fps = 20       # Frames per second

success = create_sine_wave_animation(output_file, duration, fps)
```

## Troubleshooting

If you encounter import errors related to MoviePy, try:

```bash
pip uninstall moviepy
pip install moviepy --upgrade
```

If FFmpeg is not found in your PATH:

1. Make sure FFmpeg is properly installed
2. Add the FFmpeg binary directory to your system PATH
3. Restart your terminal/command prompt after updating PATH

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.