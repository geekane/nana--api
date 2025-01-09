from typing import List
from datetime import datetime
import uuid
from config import Config

class ConversationTurn:
    def __init__(self, ask: str, answer: str):
        self.ask = ask
        self.answer = answer

    def __str__(self):
        return f"user: {self.ask}\nassistant: {self.answer}"


class ConversationHistory:
    def __init__(self, max_turns: int = 20):
        self.turns = []
        self.max_turns = max_turns
        
    def add_dialog(self, user_message: str, assistant_message: str):
        """添加新对话，并在需要时触发自动归档"""
        turn = ConversationTurn(user_message, assistant_message)
        self.turns.append(turn)
        
        # 当对话数量达到最大值时，自动归档一半的对话
        if len(self.turns) >= self.max_turns:
            self._auto_archive()
            
    def _auto_archive(self):
        """自动归档一半的对话"""
        if not self.turns:
            return
            
        # 计算要归档的对话数量
        archive_count = len(self.turns) // 2
        
        # 移除已归档的对话
        self.turns = self.turns[archive_count:]
        
    def get_context(self) -> str:
        """获取格式化后的对话上下文"""
        return "\n".join(str(turn) for turn in self.turns)
        

if __name__ == "__main__":
    async def main():
        conversation_history = ConversationHistory(max_turns=20)
        #conversation_history.add_dialog("广州有什么好吃的", "有烧鹅")
        #conversation_history.add_dialog("最近有什么电影看", "有流浪地球2")
        
        # 使用 await 调用异步方法
        #await conversation_history.archive(1, 1, "电影推荐")
        #await conversation_history.archive(0, 0, "广州有什么好吃的")
        
        #memories = conversation_history.retrieve("广州美食", n_results=1)
        #print("--------------------------------")
        #print(memories)

    # 运行异步主函数
    import asyncio
    asyncio.run(main())
