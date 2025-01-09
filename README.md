- 修改了调用大模型的方式
- 改成了api请求
去掉了由此带来的失去用处的历史记录功能

### 环境准备

- Node.js: v22.12.0
- Python: 3.10.14

确保你的系统已经安装了以上版本的环境，才能顺利运行本项(或者其他版本也可以，但我没试过)

### 后端配置
- LLM和向量模型的配置见backend/config.py
- 支持用本地大模型或者线上的API
- 如果是本地大模型的话，推荐用lm-studio
- 我测试过的模型组合是qwen2.5-32b-instruct和nomic-embed-text-v1.5-GGUF
- 线上模型推荐用claude-3-5-sonnet
- TTS服务使用了Fish Audio的API，需要注册账号并获取API Key
- https://fish.audio/zh-CN/
- 如果不想使用TTS，可以把FISH_API_KEY设置为空字符串

### 前端安装
```bash
cd frontend
npm install
```

### 后端安装
```bash
cd backend
# 创建虚拟环境
python -m venv venv
# Windows激活虚拟环境
.\venv\Scripts\activate
# Linux/Mac激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install fastapi uvicorn openai python-dotenv
```

## 运行说明

### 启动前端
```bash
cd frontend
npm run dev
```
前端将在 http://localhost:5173 启动

### 启动后端
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
后端API将在 http://localhost:8000 启动
