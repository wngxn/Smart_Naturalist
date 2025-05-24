# 非遗文化数字体验系统

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

基于RK3566开发板的非遗文化互动系统，提供在线与离线双模式，集成语音问答、图像识别、智能评分和音乐游戏功能，助力非遗文化数字化传播。

---

## 目录
- [版本特性](#版本特性)
- [硬件配置](#硬件配置)
- [软件依赖](#软件依赖)
- [安装部署](#安装部署)
- [功能模块](#功能模块)
- [API与模型配置](#api与模型配置)
- [使用说明](#使用说明)
- [性能优化](#性能优化)
- [数据准备](#数据准备)
- [测试方案](#测试方案)

- [贡献指南](#贡献指南)
- [许可协议](#许可协议)

---

## 版本特性
### 在线版（网络依赖）
- 集成有道ASR/TTS和DeepSeek API
- 实时云端语义理解与图像识别
- 轻量级部署，适合网络稳定场景

### 离线高精度版
- 本地化模型：Sentence-BERT + EfficientNet-B0量化
- 支持无网络环境运行
- 生产级性能指标：
  | 模块         | 精度指标       | 响应延迟 |
  |--------------|----------------|----------|
  | 知识问答     | 语义召回率92%  | 120ms    |
  | 场景识别     | Top-1准确率76% | 200ms    |
  | 智能评分     | Pearson 0.81   | 300ms    |

---

## 硬件配置
### 基础配置（双版本通用）
| 组件       | 规格               |
|------------|--------------------|
| 主控芯片   | RK3566 (Cortex-A55四核 @1.8GHz) |
| 内存       | ≥2GB LPDDR4       |
| 存储       | ≥16GB eMMC        |
| 摄像头     | 支持V4L2协议      |
| 屏幕       | 480x800电容触摸屏 |

### 推荐扩展
- 离线版建议配置4GB内存以支持本地模型推理
- 专业音频采集设备（SNR ≥ 70dB）

---

## 软件依赖
### 基础环境
- Ubuntu 20.04 LTS
- Python 3.8.10

### 在线版依赖
```bash
pip install pyqt5 opencv-python python-speech-features pygame requests
```

### 离线版依赖
```bash
pip install torch==1.12.1+cpu faiss-cpu sentence-transformers librosa fastdtw
```

---

## 安装部署
### 通用步骤
1. 克隆仓库
```bash
git clone https://github.com/your-repo/non-material-cultural-heritage.git
cd non-material-cultural-heritage
```

2. 配置虚拟环境
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 在线版配置
```bash
pip install -r requirements_online.txt
```

### 离线版配置
```bash
pip install -r requirements_offline.txt

```

---

## 功能模块
### 1. 非遗知识问答
- **在线版**：有道ASR + DeepSeek API + TTS播报
- **离线版**：MiniLM语义模型 + FAISS向量检索
```python
语音输入 → 语义编码 → 知识检索 → 答案输出
```

### 2. 非遗场景识别
- **在线版**：有道图像API + WebP压缩
- **离线版**：EfficientNet-B0量化模型
```python
拍摄图像 → 预处理 → 模型推理 → 分类结果
```

### 3. 非遗智能评分
- 双版本通用MFCC-DTW算法
```python
音频录制 → 特征提取 → 动态时间规整 → 评分输出
```

### 4. 非遗音乐游戏
- PyGame时序引擎
- 支持《二泉映月》《百鸟朝凤》等曲目
```json
{
  "bpm": 120,
  "notes": [{"time": 1.5, "type": "tap"}]
}
```

---

## API与模型配置
### 在线版API密钥
```yaml
# config/api_keys.yaml
youdao:
  image_api_key: "YOUR_KEY"
  asr_api_key: "YOUR_KEY"
deepseek:
  api_key: "YOUR_KEY"
```

### 离线版模型部署
```
models/
├── efficientnet_b0_quant.pth  # 图像模型
├── minilm_l12_zh.pt           # 语义模型
└── music_metadata.faiss       # 知识库索引
```

---

## 使用说明
### 启动命令
```bash
# 在线版
python main.py --mode=full

# 离线版
python offline_main.py --precision=fp16
```

## 性能优化
### 通用策略
```python
# 限制线程数
torch.set_num_threads(2)
cv2.setNumThreads(1)
```

### 存储优化
```bash
# 清理日志文件
find . -name "*.log" -delete
```

---

## 数据准备
### 图像数据集结构
```
dataset/
├── train/
│   └── 类别名称/
│       └── *.jpg
```

### 知识库构建
```python
from knowledge_base import KnowledgeBase
kb.build_index('qa.csv', 'knowledge.faiss')
```

---

## 测试方案
### 压力测试指标
| 测试项         | 阈值     | 实测值    |
|----------------|----------|-----------|
| 内存占用       | <1.5GB   | 1.2GB     |
| 并行任务数     | ≥3       | 4         |

```bash
pytest tests/ --cov=src
```

---

## 贡献指南
1. Fork仓库并创建特性分支
2. 提交代码遵循`feat: 描述`格式
3. 发起Pull Request

---

## 许可协议
- 代码库：MIT License
- 非遗数据：CC BY-NC-SA 4.0
