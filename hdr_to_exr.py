import imageio.v3 as iio
import OpenImageIO as oiio

def convert_hdr_to_exr(input_path, output_path):
    # Read HDR image using imageio (returns float32 numpy array)
    hdr_data = iio.imread(input_path)

    # Create EXR output using OpenImageIO
    out = oiio.ImageOutput.create(output_path)
    if not out:
        raise RuntimeError(f"Could not create output for {output_path}")

    spec = oiio.ImageSpec(
        hdr_data.shape[1],  # width
        hdr_data.shape[0],  # height
        hdr_data.shape[2] if len(hdr_data.shape) > 2 else 1,  # channels
        oiio.TypeDesc("float")
    )

    out.open(output_path, spec)
    out.write_image(hdr_data)
    out.close()

    print(f"✅ Converted '{input_path}' to '{output_path}'")

# Example usage
if __name__ == "__main__":
    convert_hdr_to_exr("input.hdr", "output.exr")
