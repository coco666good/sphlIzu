import subprocess
import pip
def git_clone(repository_url, target_directory):
    subprocess.run(["git", "clone", repository_url, target_directory])

def download_file(url, target_path):
    subprocess.run(["wget", "-O", target_path, url])

# 克隆项目
git_clone("https://github.com/wage888/roop.git", "/content/roop")
git_clone("https://github.com/wage666/roop_colab.git", "/content/roop_colab")

# 解封nsfw
download_file("https://huggingface.co/wageguagua/facewap/raw/main/wagecore.py", "/content/roop/roop/core.py")

# 下载模型
download_file("https://github.com/wage666/roop_colab/releases/download/v0.0.1/inswapper_128.onnx", "/content/roop/inswapper_128.onnx")

# 安装依赖
requirements_path = "/content/roop/requirements.txt"
pip.main(["install", "-r", requirements_path])


print('请注意，换脸请勿用于非法用途')
print('更多精彩加入群组https://t.me/Aiquyi888')
print('如遇诈骗或盗卖，欢迎到群组举报')