# import subprocess

# def get_gpu_stats():
#     try:
#         result = subprocess.check_output("lspci | grep -i 'VGA\\|3D controller'", shell=True)
#         gpu_info = result.decode('utf-8').strip()
#         return gpu_info
#     except Exception as e:
#         return {"error": str(e)}

# gpu_stats = get_gpu_stats()
# if "error" in gpu_stats:
#     print("Error:", gpu_stats["error"])
# else:
#     print("GPU Information:\n", gpu_stats)


# import subprocess

# def get_gpu_stats():
#     try:
#         result = subprocess.check_output("lshw -c video", shell=True)
#         gpu_info = result.decode('utf-8').strip()
#         return gpu_info
#     except Exception as e:
#         return {"error": str(e)}

# gpu_stats = get_gpu_stats()
# if "error" in gpu_stats:
#     print("Error:", gpu_stats["error"])
# else:
#     print("GPU Information:\n", gpu_stats)


# import pynvml

# def get_gpu_memory_usage():
#     pynvml.nvmlInit()
#     device_count = pynvml.nvmlDeviceGetCount()
    
#     memory_usage = []

#     for i in range(device_count):
#         handle = pynvml.nvmlDeviceGetHandleByIndex(i)
#         info = pynvml.nvmlDeviceGetMemoryInfo(handle)
#         memory_usage.append(info.used)
    
#     pynvml.nvmlShutdown()

#     return memory_usage

# memory_usage = get_gpu_memory_usage()
# for i, usage in enumerate(memory_usage):
#     print(f"GPU {i}: {usage / 1024**2} MB")


# import subprocess

# # Run the 'glxinfo -B' command and capture the output
# output = subprocess.check_output(['glxinfo', '-B'], universal_newlines=True)

# # Initialize variables to store GPU information
# vendor = None
# device = None
# video_memory = None
# total_available_memory = None

# # Split the output into lines and search for relevant information
# lines = output.split('\n')
# for line in lines:
#     if "Vendor:" in line:
#         vendor = line.split("Vendor:")[1].strip()
#     if "Device:" in line:
#         device = line.split("Device:")[1].strip()
#     if "Video memory:" in line:
#         video_memory = line.split("Video memory:")[1].strip().split()[0]
#     if "Currently available dedicated video memory:" in line:
#         total_available_memory = line.split("Currently available dedicated video memory:")[1].strip().split()[0]

# # Print the retrieved GPU information
# print("Vendor:", vendor)
# print("Device:", device)
# print("Video Memory:", int(video_memory[:-2]))
# print("Total Available Memory:", total_available_memory)


# name of display: :0
# display: :0  screen: 0
# direct rendering: Yes
# Extended renderer info (GLX_MESA_query_renderer):
#     Vendor: AMD (0x1002)
#     Device: REMBRANDT (rembrandt, LLVM 15.0.7, DRM 3.49, 6.2.0-34-generic) (0x1681)
#     Version: 23.0.4
#     Accelerated: yes
#     Video memory: 512MB
#     Unified memory: no
#     Preferred profile: core (0x1)
#     Max core profile version: 4.6
#     Max compat profile version: 4.6
#     Max GLES1 profile version: 1.1
#     Max GLES[23] profile version: 3.2
# Memory info (GL_ATI_meminfo):
#     VBO free memory - total: 93 MB, largest block: 93 MB
#     VBO free aux. memory - total: 6748 MB, largest block: 6748 MB
#     Texture free memory - total: 93 MB, largest block: 93 MB
#     Texture free aux. memory - total: 6748 MB, largest block: 6748 MB
#     Renderbuffer free memory - total: 93 MB, largest block: 93 MB
#     Renderbuffer free aux. memory - total: 6748 MB, largest block: 6748 MB
# Memory info (GL_NVX_gpu_memory_info):
#     Dedicated video memory: 512 MB
#     Total available memory: 8118 MB
#     Currently available dedicated video memory: 93 MB
# OpenGL vendor string: AMD
# OpenGL renderer string: REMBRANDT (rembrandt, LLVM 15.0.7, DRM 3.49, 6.2.0-34-generic)
# OpenGL core profile version string: 4.6 (Core Profile) Mesa 23.0.4-0ubuntu1~22.04.1
# OpenGL core profile shading language version string: 4.60
# OpenGL core profile context flags: (none)
# OpenGL core profile profile mask: core profile

# OpenGL version string: 4.6 (Compatibility Profile) Mesa 23.0.4-0ubuntu1~22.04.1
# OpenGL shading language version string: 4.60
# OpenGL context flags: (none)
# OpenGL profile mask: compatibility profile

# OpenGL ES profile version string: OpenGL ES 3.2 Mesa 23.0.4-0ubuntu1~22.04.1
# OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.20


# import time
# from PIL import Image, ImageFilter

# def image_processing():
#     st = time.time()
#     print(st)
#     image = Image.open('Large_image.jpg')
#     for _ in range(1000):
#         image = image.filter(ImageFilter.GaussianBlur(radius=10))
#         image = image.rotate(30)
#         image = image.convert('L')
#         image = image.resize((2000, 2000), Image.ANTIALIAS)
#         def custom_filter(pixel):
#             return pixel
#         image = image.point(custom_filter)
#     et = time.time()
#     return et - st
# # Call the image processing function to apply the operations
# print(image_processing())

# import time
# from pdfminer.high_level import extract_pages

# def pdf_text_render():
#     start_time = time.time()
#     for page_layout in extract_pages('trial.pdf'):
#         for element in page_layout:
#             continue
#     end_time = time.time()
#     duration = end_time-start_time
#     return (1273/duration)

# print(pdf_text_render())

import psutil
print(psutil.sensors_temperatures())