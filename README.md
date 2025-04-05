
### HDR to EXR Batch Converter

Converts `.hdr` image files to `.exr` format – individually or as an entire folder. Perfect for pipelines, CGI, or game asset workflows.

---

#### Installation

```bash
pip install -r requirements.txt
```

---

#### Usage

1. Drag `.hdr` files or entire folders onto the `convert_hdrs.bat` file.  
2. The converted `.exr` files will automatically be placed in the `output_exr` folder.

---

#### Project Structure

```
├── hdr_to_exr_batch.py      # The Python script for conversion
├── convert_hdrs.bat         # For drag-and-drop of files/folders
├── requirements.txt         # Required Python packages
├── output_exr/              # Target folder for EXR files
```

---

#### Prerequisites

- Python 3.7+
- Packages:
    - `imageio`
    - `imageio-ffmpeg`
    - `OpenImageIO`


---