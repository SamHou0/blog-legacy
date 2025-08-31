import os
import sys
import json
import urllib.parse

def main():
    if len(sys.argv) < 2:
        print("用法: python generate_redirects.py <目录路径>")
        sys.exit(1)

    input_dir = sys.argv[1]
    if not os.path.isdir(input_dir):
        print(f"错误: {input_dir} 不是一个有效目录")
        sys.exit(1)

    base_url = "https://novel.samhou.moe/"
    redirects = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            name = os.path.splitext(filename)[0]

            # 对 source 和 destination 都进行 URL 编码
            encoded_name = urllib.parse.quote(name)

            redirects.append({
                "source": f"/{encoded_name}/",
                "destination": f"{base_url}{encoded_name}/"
            })

    config = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "redirects": redirects
    }

    output_file = os.path.join(input_dir, "vercel.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print(f"已生成 {output_file} ✅")

if __name__ == "__main__":
    main()
