class Config:
    ''' LLM配置 '''
    LLM_API_URL = "https://api.siliconflow.cn/v1/chat/completions"
    LLM_API_KEY = "sk-nexfkxivirurtdvbpzkjgjcyplorwkssfitcvnppeaclunbe"
    LLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"  # 添加模型名称

    EDGE_TTS_VOICE = "zh-CN-XiaoxiaoNeural"  # 设置默认的 edge_tts 语音
    AUDIO_API_URL = "https://fengmiguoji-0109edgetts.hf.space/v1/audio/speech"  # 修改为你的 API 地址
    AUDIO_API_KEY = "your_api_key_here"  # 替换成你的 API 密钥
    
    ''' 对话历史配置 '''
    MAX_TURNS = 20  # 最多保存20轮对话，超过后自动归档一半
    
    @classmethod
    def is_tts_enabled(cls) -> bool:
        """判断是否启用TTS功能"""
        return True
