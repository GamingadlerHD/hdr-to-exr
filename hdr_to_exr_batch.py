import sys
import os
import imageio.v3 as iio
import OpenImageIO as oiio

def convert_hdr_to_exr(input_path, output_path):
    hdr_data = iio.imread(input_path)

    out = oiio.ImageOutput.create(output_path)
    if not out:
        raise RuntimeError(f"Could not create output for {output_path}")

    spec = oiio.ImageSpec(
        hdr_data.shape[1],
        hdr_data.shape[0],
        hdr_data.shape[2] if len(hdr_data.shape) > 2 else 1,
        oiio.TypeDesc("float")
    )

    out.open(output_path, spec)
    out.write_image(hdr_data)
    out.close()
    print(f"[✔] Converted: {input_path} → {output_path}")

def process_folder_or_files(inputs):
    output_dir = os.path.join(os.getcwd(), "output_exr")
    os.makedirs(output_dir, exist_ok=True)

    for path in inputs:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(".hdr"):
                        full_path = os.path.join(root, file)
                        out_name = os.path.splitext(os.path.basename(file))[0] + ".exr"
                        out_path = os.path.join(output_dir, out_name)
                        convert_hdr_to_exr(full_path, out_path)
        elif path.lower().endswith(".hdr"):
            out_name = os.path.splitext(os.path.basename(path))[0] + ".exr"
            out_path = os.path.join(output_dir, out_name)
            convert_hdr_to_exr(path, out_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ziehe .hdr-Dateien oder Ordner hier drauf!")
    else:
        process_folder_or_files(sys.argv[1:])
